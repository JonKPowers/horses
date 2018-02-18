import tidy_it_up as tidy
import db_functions
from csv_definitions import file_structure as name_files
import table_functions as tbl

import os
import pathlib
import re
import pandas as pd
import logging
import datetime

logging.basicConfig(filename='main_py.log', filemode='w', level=logging.INFO)

columns_to_delete = {
    '1': [s for s in name_files['1'] if 'reserved' in s],
    '2': [s for s in name_files['2'] if 'reserved' in s],
    '3': [s for s in name_files['3'] if 'reserved' in s],
    '4': [s for s in name_files['4'] if 'reserved' in s],
    '5': [s for s in name_files['5'] if 'reserved' in s],
    '6': [s for s in name_files['6'] if 'reserved' in s],
    'DRF': [s for s in name_files['DRF'] if 'reserved' in s]
}

df_handlers = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    'DRF': []
}


def main(file_to_process='', path='data'):
    logging.debug('main() started with file_to_process={} and path={}'.format(file_to_process, path))
    start_time = datetime.datetime.now()

    # Make the list of files to process
    if file_to_process:
        file_paths = []
        file_paths.append(pathlib.Path(path, file_to_process))
    else:
        file_paths = [pathlib.Path(path, file) for file in os.listdir(path)]
        file_paths = [file for file in file_paths if file.is_file()]

    # Create the database handler
    db = db_functions.DbHandler(db='horses_data')

    # Create the table handlers
    for table in tbl.tables:
        handler = tbl.TableHandler(table)
        df_handlers[handler.extension].append(handler)

    # Initialize some counter/tracking variables
    i = 1
    valid_extensions = ['1', '2', '3', '4', '5', '6', 'DRF']
    check_for_duplicates = True

    # Process each csv file, then run it through its table handler to add to db
    for file in file_paths:
        file_start = datetime.datetime.now()

        # Only process the file if it's a valid file type
        if file.suffix[1:] not in valid_extensions:
            logging.info('File {} not a valid file type--skipping'.format(file.name))
            continue

        # Check if file has already been processed; if so, ask whether to process it again
        if check_for_duplicates:
            file_already_processed = (file.parent / (file.suffix[1:] + '_file') /
                                      file.name).exists()
            if file_already_processed:
                print('It looks like {} has already been processed.'.format(file.name))
                move_on = input('Should we skip this file? [Y/n/no to (a)ll duplicates] ').lower()
                if move_on == 'n':
                    pass
                if move_on == 'a':
                    check_for_duplicates = False
                else:
                    print('Skipping {} ... '.format(file.name))
                    continue

        logging.info('Processing {} ({} of {})'.format(file, i, len(file_paths)))
        print('Processing {} ({} of {})'.format(file, i, len(file_paths)))

        # Put the csv data into a dataframe
        try:
            table_data, extension = process_csv_file(file)
        except FileNotFoundError as e:
            logging.info('File {} not found during process_csv_file()'.format(e))
            print('There was a problem finding the file {}:'.format(file))
            print('\t', e)
            continue

        # For each file, run it through the handlers for its file type
        print('Adding {} info to database ...'.format(file))
        for handler in df_handlers[extension]:
            handler.process_data(table_data, db, file.name)

        # Move the processed file to its processed-file directory
        processed_dir = file.parent / (extension+'_file')
        processed_dir.mkdir(exist_ok=True)
        print('Moving {} to {}'.format(file.name, processed_dir))
        file.rename(processed_dir / file.name)

        # Increment our progress-tracking counter
        print('Time to process {}: {}'.format(file.name, str(datetime.datetime.now() - file_start)))
        print('Elapsed time:', str(datetime.datetime.now() - start_time), '\n')
        i += 1

    end_time = datetime.datetime.now()

    print("Start time:", str(start_time))
    print("End time:", str(end_time))
    print("Total time:", str(end_time - start_time))





def process_csv_file(file):
    extension = re.search(r'(?<=\.).+$', str(file))[0]
    #   Read the data in and run it through the cleaner
    table_data = pd.read_csv(file, header=None, names=name_files[str(extension)])
    table_data = tidy.tidy_it_up(table_data, extension)
    #   Strip out unused columns
    for column in columns_to_delete[str(extension)]:
        del table_data[column]
    return table_data, extension




