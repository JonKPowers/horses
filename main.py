import csv_processing_functions as processor
import df_preprocessing as cleaner
import database_functions
import file_definitions

import os
import pathlib
import re
import pandas as pd

name_files = {
    '1': file_definitions.file_1_columns,
    '2': file_definitions.file_2_columns,
    '3': file_definitions.file_3_columns,
    '4': file_definitions.file_4_columns,
    '5': file_definitions.file_5_columns,
    '6': file_definitions.file_6_columns,
    'drf': file_definitions.past_perf_columns,
}

def get_file_list(extension, path='data'):
    print('Generating list of .{} files.'.format(str(extension)))
    extension = str(extension)
    return processor.generate_file_list(extension, path)

def generate_df(files, extension, path='data'):
    print('Generating dataframe for .{} files ({} files to process).'.format(str(extension), len(files)))
    df_list = processor.process_csv_file(files, extension, path)
    combined_df = processor.strip_table_data(df_list, extension)
    column_dtypes = combined_df.dtypes
    return cleaner.tidy_it_up(combined_df, extension), column_dtypes

def build_db(table_data, extension, column_dtypes, db='horses_test'):
    print('Building db and table for .{} files'.format(str(extension)))
    extension = str(extension)
    db = database_functions.DbHandler()
    db.initialize_db()
    db.initialize_table(extension + '_data', table_data, column_dtypes)
    db.add_to_table(extension + '_data', table_data, column_dtypes)


def process_file(file, path='data'):
    table_data, extension, processed_file_path = processor.process_csv_file(file, path)
    table_data = processor.strip_table_data(table_data,extension)
    column_dtypes = table_data.dtypes
    try:
        path = pathlib.Path(path)
        (path / file).rename(processed_file_path)
    except PermissionError:
        print('Permission denied while moving {} to {}'.format(file, processed_file_path))

    return cleaner.tidy_it_up(table_data, extension), column_dtypes


if __name__ == '__main__':
    for i in range(1, 7):
        print('Main function started for .{} files.'.format(str(i)))
        file_list = get_file_list(i)
        if file_list:
            table_data, column_dtypes = generate_df(file_list, i)
            build_db(table_data, i, column_dtypes)
        else:
            print("No .{} files--skipping.".format(i))


