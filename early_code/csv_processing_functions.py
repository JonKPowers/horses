import os
import re
import pathlib
import pandas as pd

import file_definitions

name_files = {
    '1': file_definitions.file_1_columns,
    '2': file_definitions.file_2_columns,
    '3': file_definitions.file_3_columns,
    '4': file_definitions.file_4_columns,
    '5': file_definitions.file_5_columns,
    '6': file_definitions.file_6_columns,
    'drf': file_definitions.past_perf_columns,
}


def generate_file_list(extension, path='data'):
    """Creates list of files with a particular extension"""

    returned_files = []
    for file in list(os.listdir(path)):
        if re.search(r'\.' + str(extension) + '$', file):
            returned_files.append(file)
    return returned_files


def process_csv_file(file, path='data'):
    """Reads CSV files into pandas dataframes and returns a list of dataframes"""

    extension = re.search(r'(?<=\.).+$', file)[0]
    table_data = []
    # Create the processed dir if it's not already there
    path = pathlib.Path(path)
    processed_dir = path / (str(extension) + '_files')
    processed_dir.mkdir(exist_ok=True)

    # Process that file!
    # Check if file is in processed dir
    processed_file_path = processed_dir / file
    move_on = 'n'
    if processed_file_path.exists():
        print('It looks like {} has already been processed.'.format(file))
        move_on = input('Should we skip this file? [Y/n]').lower()
    if move_on == 'y':
        pass
    else:
        print('Reading {} into dataframe'.format(file))
        table_data = pd.read_csv(path / file, header=None, names=name_files[str(extension)])
    return table_data, extension, processed_file_path


def strip_table_data(table_data, extension):
    """Takes list of pd.DataFrames as an input, combines them vertically,
    and strips out unused columns that are marked as reserved"""

    column_numbers_to_remove = [i for i, s in enumerate(name_files[str(extension)]) if 'reserved' in s]
    print('working out column_names to delete')
    column_names_to_remove = [s for i, s in enumerate(name_files[str(extension)]) if 'reserved' in s]
    print('Pulling out unused columns')
    for column in column_names_to_remove:
        del table_data[column]
    return table_data