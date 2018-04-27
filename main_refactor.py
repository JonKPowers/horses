import tidy_it_up as tidy
import db_functions_refactor as db_functions
from csv_definitions import file_structure as name_files
import table_functions as tbl
import features
from progress.bar import Bar

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

table_handlers = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    'DRF': [],
}

processing_times = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    'DRF': [],
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
    db = db_functions.DbHandler(db='horses_data', initialize_db=True)
    db.connect_db()

    # Create the table handlers
    for table in tbl.tables:
        handler = tbl.TableHandler(table, db)
        table_handlers[handler.extension].append(handler)

    # Initialize some counter/tracking variables
    i = 1
    valid_extensions = ['1', '2', '3', '4', '5', '6', 'DRF']
    check_for_duplicates = True
    num_of_files = len(file_paths)

    # Process each csv file, then run it through the table handlers to add to db
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
                print(f'It looks like {file.name} has already been processed.')
                move_on = input('Should we skip this file? [Y/n/no to (a)ll duplicates] ').lower()
                if move_on == 'n':
                    pass
                if move_on == 'a':
                    check_for_duplicates = False
                else:
                    print('Skipping {} ... '.format(file.name))
                    continue

        logging.info(f'Processing {file} ({i} of {num_of_files})')
        print(f'Processing {file} ({i} of {num_of_files})')

        # Put the csv data into a dataframe
        try:
            table_data, extension = process_csv_file(file)
        except FileNotFoundError as e:
            logging.info(f'File {e} not found during process_csv_file()')
            print(f'There was a problem finding the file {file}')
            print('\t', e)
            continue

        # For each file, run it through the handlers for its file type
        bar = Bar('Adding to db:', max = len(table_handlers[extension]))
        print(f'Adding {file} info to database ...')
        for handler in table_handlers[extension]:
            handler.process_data(table_data, db, file.name)
            bar.next()
        bar.finish()

        # Move the processed file to its processed-file directory
        processed_dir = file.parent / (extension + '_file')
        processed_dir.mkdir(exist_ok=True)
        print(f'Moving {file.name} to {processed_dir}')
        file.rename(processed_dir / file.name)

        # Increment our progress-tracking counter
        time_to_process = datetime.datetime.now() - file_start
        processing_times[extension].append(time_to_process)
        print(f'Time to process {file.name}: {str(datetime.datetime.now() - file_start)}')
        print(f'Average time to process {extension} files: {sum(processing_times[extension]) / len(processing_times[extension])}')
        print(f'Elapsed time: {str(time_to_process)}\n')
        i += 1

    db.close_db()
    end_time = datetime.datetime.now()

    print(f'Start time: {str(start_time)}')
    print(f'End time: {str(end_time)}')
    print(f'Average times:')
    for file_type in processing_times:
        print(f'\t{file_type} files: {sum(processing_times[file_type]) / len(processing_times[file_type])}')
    print(f'Total time: {str(end_time - start_time)}')


def process_csv_file(file, add_features=True):
    extension = re.search(r'(?<=\.).+$', str(file))[0]
    #   Read the data in and run it through the cleaner
    table_data = pd.read_csv(file, header=None, names=name_files[str(extension)])
    table_data = tidy.tidy_it_up(table_data, extension)
    if add_features:
        table_data = features.add_features(table_data, extension)
    #   Strip out unused columns
    for column in columns_to_delete[str(extension)]:
        del table_data[column]
    return table_data, extension

if __name__ == '__main__':
    main()



