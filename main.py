import df_preprocessing as cleaner
import database_functions
from def_objects import file_structure as name_files
import past_perf_functions as pp

import os
import pathlib
import re
import pandas as pd
import logging

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

def main(file_to_process='', path='data'):
    logging.debug('main() started with file_to_process={} and path={}'.format(file_to_process, path))
    if file_to_process:
        file_paths = []
        file_paths.append(pathlib.Path(path, file_to_process))
    else:
        file_paths = [pathlib.Path(path, file) for file in os.listdir(path)]
        file_paths = [file for file in file_paths if file.is_file()]
    db = database_functions.DbHandler()
    i = 1
    for file in file_paths:
        logging.debug('Processing {} ({} of {})'.format(file, i, len(file_paths)))
        # print('Processing {} ({} of {})'.format(file, i, len(file_paths)))
        try:
            table_data, extension = process_csv_file(file)
        except FileNotFoundError as e:
            print('There was a problem finding the file {}:'.format(file))
            print('\t', e)
            continue
        db.initialize_table(extension+'_data', extension)
        db.add_to_table(extension+'_data', table_data, column_names=list(table_data))
        i += 1
        processed_dir = file.parent / (extension+'_file')
        processed_dir.mkdir(exist_ok = True)
        print('Moving {} to {}\n'.format(file.name, processed_dir))
        file.rename(processed_dir / file.name)

def process_csv_file(file):
    extension = re.search(r'(?<=\.).+$', str(file))[0]
    #   Read the data in and run it through the cleaner
    table_data = pd.read_csv(file, header=None, names=name_files[str(extension)])
    table_data = cleaner.tidy_it_up(table_data, extension)
    #   Strip out unused columns
    for column in columns_to_delete[str(extension)]:
        del table_data[column]
    return table_data, extension

def process_drf_files(file_to_process='', path='data'):
    logging.debug('process_drf_files() started with file_to_process={} and path={}'.format(file_to_process, path))
    if file_to_process:
        file_paths = []
        file_paths.append(pathlib.Path(path, file_to_process))
    else:
        file_paths = [pathlib.Path(path, file) for file in os.listdir(path)]
        file_paths = [file for file in file_paths if re.search(r'\.DRF$', file.name)]
    db = database_functions.DbHandler('horses_pp')
    pp_handlers = []
    for table in pp.pp_tables:
        pp_handlers.append(pp.PastPerfData(table))
    i = 1
    for file in file_paths:
        logging.info('Processing {} ({} of {})'.format(file, i, len(file_paths)))
        print('Processing {} ({} of {})'.format(file, i, len(file_paths)))
        try:
            table_data, extension = process_csv_file(file)
        except FileNotFoundError as e:
            print('There was a problem finding the file {}:'.format(file))
            print('\t', e)
            continue
        for handler in pp_handlers:
            handler.process_data(table_data, db)
        processed_dir = file.parent / (extension+'_file')
        processed_dir.mkdir(exist_ok = True)
        logging.info('Moving {} to {}\n'.format(file.name, processed_dir))
        file.rename(processed_dir / file.name)
        i += 1




