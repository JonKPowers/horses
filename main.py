import csv_processing_functions as processor
import df_preprocessing as cleaner
import database_functions

import pandas as pd

def get_file_list(extension, path='data'):
    print('Generating list of .{} files.'.format(str(extension)))
    extension = str(extension)
    return processor.generate_file_list(extension, path)

def generate_df(files, extension, path='data'):
    print('Generating dataframe for .{} files.'.format(str(extension)))
    df_list = processor.process_csv_files(files, extension, path)
    combined_df = processor.merge_and_strip_dfs(df_list, extension)
    column_dtypes = combined_df.dtypes
    return cleaner.tidy_it_up(combined_df, extension), column_dtypes

def build_db(table_data, extension, column_dtypes, db='horses_test'):
    print('Building db and table for .{} files'.format(str(extension)))
    extension = str(extension)
    db = database_functions.DbHandler()
    db.initialize_db()
    db.initialize_table(extension + '_data', table_data, column_dtypes)
    db.add_to_table(extension + '_data', table_data, column_dtypes)


if __name__ == '__main__':
    for i in range(1, 7):
        print('Main function started for .{} files.'.format(str(i)))
        file_list = get_file_list(i)
        if file_list:
            table_data, column_dtypes = generate_df(file_list, i)
            build_db(table_data, i, column_dtypes)
        else:
            print("No .{} files--skipping.".format(i))


