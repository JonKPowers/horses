import tidy_it_up as tidy
import db_functions_refactor as db_functions
from csv_definitions import file_structure as name_files
import table_functions
import features
from progress.bar import Bar

import os
import pathlib
import re
import pandas as pd
import logging

logging.basicConfig(filename='main_py.log', filemode='w', level=logging.INFO)

columns_to_delete = {
    '1': [_ for _ in name_files['1'] if 'reserved' in _],
    '2': [_ for _ in name_files['2'] if 'reserved' in _],
    '3': [_ for _ in name_files['3'] if 'reserved' in _],
    '4': [_ for _ in name_files['4'] if 'reserved' in _],
    '5': [_ for _ in name_files['5'] if 'reserved' in _],
    '6': [_ for _ in name_files['6'] if 'reserved' in _],
    'DRF': [_ for _ in name_files['DRF'] if 'reserved' in _]
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


def main(file_to_process='', path='data', verbose=False, move_files=True):
    logging.debug(f'Beginning main() in path {path}')

    # Make the list of files to process
    if file_to_process:
        file_paths = [pathlib.Path(path, file_to_process)]
    else:
        file_paths = [pathlib.Path(path, file) for file in os.listdir(path)]
        file_paths = [file for file in file_paths if file.is_file()]

    # Spin up db handler and create a connection to the db; initialize the db if it doesn't already exist
    db = db_functions.DbHandler(db='horses_test', initialize_db=True, verbose=False)
    db.connect()

    # table_functions.py contains information about all the tables that will be created for the database
    # along with information about what files they are associated with. It also contains "handlers" that deal with
    # the specifics of those tables during the process of adding information to the database.
    for table in table_functions.tables:
        handler = table_functions.TableHandler(table, db)
        table_handlers[handler.extension].append(handler)

    # Initialize some counter/tracking and control variables
    valid_extensions = ['1', '2', '3', '4', '5', '6', 'DRF']
    check_for_duplicates = True
    skip_duplicates = False
    num_of_files = len(file_paths)
    bar = Bar(f'Processing files:', max=num_of_files, suffix='%(percent).3f%% - %(index)d/%(max)d - %(eta)s secs.')

    # Process each csv file, then run it through the table handlers to add to db
    for file in file_paths:
        bar.next()
        if not file.exists():
            logging.info(f'File {file.name} does not exist--skipping')
            continue

        # Only process the file if it's a valid file type
        if file.suffix[1:] not in valid_extensions:
            logging.info(f'File {file.name} not a valid file type--skipping')
            continue

        # Check if file has already been processed; if so, ask whether to process it again
        if check_for_duplicates:
            file_already_processed = (file.parent / 'processed_files' / file.name).exists()
            if file_already_processed and not skip_duplicates:
                logging.debug(f'File {file.name} has already been processed--skipping.')
        logging.debug(f'Processing {file}')
        if verbose: print(f'Processing {file}')

        # Put the csv data into a dataframe
        table_data, extension = process_csv_file(file)

        # For each file, run it through the handlers for its file type
        if verbose: print(f'Adding {file} info to database ...')
        for handler in table_handlers[extension]:
            handler.process_data(table_data, db, file.name)

        # Move the processed file to a processed-file directory
        if move_files:
            processed_dir = file.parent / ('processed_files')
            processed_dir.mkdir(exist_ok=True)
            if verbose: print(f'Moving {file.name} to {processed_dir}')
            file.rename(processed_dir / file.name)

    bar.finish()
    db.connection.commit()
    db.close()


def process_csv_file(file, tidy_file=True, add_features=False):
    extension = re.search(r'(?<=\.).+$', str(file))[0]
    #   Read the data in and run it through the cleaner
    table_data = pd.read_csv(file, header=None, names=name_files[str(extension)])
    if tidy_file:
        table_data = tidy.tidy_it_up(table_data, extension)
    if add_features:
        table_data = features.add_features(table_data, extension)
    #   Strip out unused columns
    for column in columns_to_delete[str(extension)]:
        del table_data[column]
    return table_data, extension


if __name__ == '__main__':
    main()
