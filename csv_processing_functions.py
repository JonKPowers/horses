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


def process_csv_files(file_list, extension='', path='data'):
    """Reads CSV files into pandas dataframes and returns a list of dataframes"""

    path = pathlib.Path(path)
    # Create the processed dir if it's not already there
    processed_dir = path / (str(extension) + '_files')
    processed_dir.mkdir(exist_ok=True)

    data_frames = []

    # Process those files!
    for file in file_list:
        file_path = processed_dir / file
        # Check if file is in processed dir
        if file_path.exists():
            print('It looks like {} has already been processed.'.format(file))
            move_on = input('Should we skip this file?')
        # Read csv into a pd.df
        data_frames.append(pd.read_csv(path / file, header=None, names=name_files[str(extension)]))
        # Move file into processed dir
        try:
            (path / file).rename(file_path)
        except PermissionError:
            print('Permission denied while moving {} to {}'.format(file, file_path))
    return data_frames


def merge_and_strip_dfs(df_list, extension):
    """Takes list of pd.DataFrames as an input, combines them vertically,
    and strips out unused columns that are marked as reserved"""

    column_numbers_to_remove = [i for i, s in enumerate(name_files[str(extension)]) if 'reserved' in s]
    column_names_to_remove = [s for i, s in enumerate(name_files[str(extension)]) if 'reserved' in s]
    combined_df = pd.DataFrame()
    for df in df_list:
        combined_df = combined_df.append(df)
    for column in column_names_to_remove:
        del combined_df[column]
    return combined_df