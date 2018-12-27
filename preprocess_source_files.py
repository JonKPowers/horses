import pathlib
import os
import re
import logging
from collections import namedtuple

import pandas as pd
from progress.bar import Bar

from csv_definitions import file_structure as name_files
import features

logging.basicConfig(filename='preprocess_source_files.log', filemode='w', level=logging.INFO)

class TidyFile:

    Replacement = namedtuple('Replacement', ['field', 'base_value', 'replacement_value'])

    columns_to_delete = {
        '1': [_ for _ in name_files['1'] if 'reserved' in _],
        '2': [_ for _ in name_files['2'] if 'reserved' in _],
        '3': [_ for _ in name_files['3'] if 'reserved' in _],
        '4': [_ for _ in name_files['4'] if 'reserved' in _],
        '5': [_ for _ in name_files['5'] if 'reserved' in _],
        '6': [_ for _ in name_files['6'] if 'reserved' in _],
        'DRF': [_ for _ in name_files['DRF'] if 'reserved' in _]
    }

    replacement_dict_1_file = [
        Replacement('about_dist_flag', 'A', 1),
        Replacement('all_weather_flag', 'A', 1),
        Replacement('state_bred_flag', 'S', 1),
        Replacement('chute_start_flag', 'C', 1),
        Replacement('chute_start_flag', 'N', 1),
        Replacement('off_turf_flag', 'O', 1),
        Replacement('off_turf_dist_change', 'Y', 1),
        Replacement('off_turf_dist_change', 'N', 0),
        Replacement('race_grade', 0, 'NULL'),
    ]

    replacement_dict_2_file = [
        Replacement('nonbetting_flag', 'Y', 1),
        Replacement('disqualified_flag', 'Y', 1),
        Replacement('corrected_weight', 'Y', 1),
        Replacement('claimed_flag', 'Y', 1),
        Replacement('claimed_flag', 'N', 0),
        Replacement('dead_heat_flag', 'DH', 1),
    ]

    replacement_dict_3_file = {}

    replacement_dict_4_file = {}

    replacement_dict_5_file = {}

    replacement_dict_6_file = {}

    replacement_dict_DRF_file = [
        Replacement('statebread_flag', 's', 1),
        Replacement('today_nasal_strip_chg', 9, 'NULL'),
        Replacement('todays_meds_new', 9, 'NULL'),
        Replacement('todays_meds_old', 9, 'NULL'),
        Replacement('equipment_change', 9, 'NULL'),
        Replacement('allweather_surface', 'A', 1),
        Replacement('bris_run_style', 'NA', None),
        Replacement('past_special_chute_{}', 'c', 1),
        Replacement('past_bar_shoe_{}', 'r', 1),
        Replacement('past_start_code_{}', 'X', 1),
        Replacement('past_sealed_track_indicator_{}', 's', 1),
        Replacement('past_all_weather_flag_{}', 'A', 1),
        Replacement('past_equipment_{}', 'b', 1),
        Replacement('past_entry_{}', 'e', 1),
        Replacement('past_claimed_code_{}', 'c', 1),
        Replacement('past_claimed_code_{}', 'v', 1),
        Replacement('past_statebred_flag_{}', 's', 1),
        Replacement('past_restricted_or_qualified_{}', 'R', 1),
    ]

    replacement_dict_DRF_file_regex = [
        Replacement('past_call_pos_start_{}', r'[A-Za-z?*]+', 'NULL'),
        Replacement('past_call_pos_first_{}', r'[A-Za-z?*]+', 'NULL'),
        Replacement('past_call_pos_second_{}', r'[A-Za-z?*]+', 'NULL'),
        Replacement('past_call_pos_stretch_{}', r'[A-Za-z?*]+', 'NULL'),
        Replacement('past_call_pos_finish_{}', r'[A-Za-z?*]+', 'NULL'),
        # Replacement('past_start_code_{}', r'[A-Za-z?*]+', 'NULL'),      # This will break the off_turf dis change feature to NULL this out
        Replacement('past_company_line_{}', r' ', 'X'),
        ]

    fill_dict_1_file = {
        'about_dist_flag': 0,
        'all_weather_flag': 0,
        'state_bred_flag': 0,
        'chute_start_flag': 0,
        'off_turf_flag': 0,
    }

    fill_dict_2_file = {
        'nonbetting_flag': 0,
        'disqualified_flag': 0,
        'corrected_weight': 0,
        'dead_heat_flag': 0,

    }

    fill_dict_3_file = {}

    fill_dict_4_file = {}

    fill_dict_5_file = {}

    fill_dict_6_file = {}

    fill_dict_DRF_file = {
        'apprentice_wgt_alw': 0,
        'statebread_flag': 0,
        'allweather_surface': 0,
        'claiming_price': 0,
        'past_special_chute_{}': 0,
        'past_bar_shoe_{}': 0,
        'past_start_code_{}': 0,
        'past_sealed_track_indicator_{}': 0,
        'past_all_weather_flag_{}': 0,
        'past_weight_allowance_{}': 0,
        'past_equipment_{}': 0,
        'past_entry_{}': 0,
        'past_claimed_code_{}': 0,
        'past_statebred_flag_{}': 0,
        'past_restricted_or_qualified_{}': 0

    }

    def __init__(self, verbose=False):
        self.verbose = verbose

    def replace_items(self, df, replacement_dict):
        if not replacement_dict:
            return
        for column, base_value, replacement_value in replacement_dict:
            if '{' in column:
                for i in range(1, 11):
                    df[column.format(i)].replace(base_value, replacement_value, inplace=True)
            else:
                df[column].replace(base_value, replacement_value, inplace=True)

    def replace_items_regex(self, df, replacement_dict):
        for column, base_value, replacement_value in replacement_dict:
            if '{' in column:
                for i in range(1, 11):
                    df[column.format(i)].replace(base_value, replacement_value, inplace=True, regex=True)
            else:
                df[column].replace(base_value, replacement_value, inplace=True, regex=True)

    def fill_blanks(self, df, fill_dict):
        if not fill_dict:
            return
        for column, fill in fill_dict.items():
            if '{' in column:
                for i in range(1, 11):
                    df[column.format(i)].fillna(fill, inplace=True)
            else:
                df[column].fillna(fill, inplace=True)

    def clean_table(self, df, extension, verbose=False):
        if extension == '1':
            self.replace_items(df, self.replacement_dict_1_file)
            self.fill_blanks(df, self.fill_dict_1_file)
        elif extension == '2':
            self.replace_items(df, self.replacement_dict_2_file)
            self.fill_blanks(df, self.fill_dict_2_file)
        elif extension == '3':
            self.replace_items(df, self.replacement_dict_3_file)
            self.fill_blanks(df, self.fill_dict_3_file)
        elif extension == '4':
            self.replace_items(df, self.replacement_dict_4_file)
            self.fill_blanks(df, self.fill_dict_4_file)
        elif extension == '5':
            self.replace_items(df, self.replacement_dict_5_file)
            self.fill_blanks(df, self.fill_dict_5_file)
        elif extension == '6':
            self.replace_items(df, self.replacement_dict_6_file)
            self.fill_blanks(df, self.fill_dict_6_file)
        elif extension == 'DRF':
            self.replace_items(df, self.replacement_dict_DRF_file)
            self.replace_items_regex(df, self.replacement_dict_DRF_file_regex)
            self.fill_blanks(df, self.fill_dict_DRF_file)
            # Convert surface-type field in PP data to "new" surface-type style
            # (code is 'A' for all-weather dirt track and 'D' for non-all-weather)
            for i in range(1, 11):
                surface_field = df.columns.get_loc(f'past_surface_{i}')
                all_weather_field = df.columns.get_loc(f'past_all_weather_flag_{i}')
                for j in range(len(df)):
                    if df.iloc[j, all_weather_field] == 1:
                        df.iloc[j, surface_field] = 'A'

            # Convert surface-type field DRF race info to "new surface-type style
            # (code is 'A' for all-weather dirt track and 'D' for non-all-weather

            surface_field = df.columns.get_loc('surface')
            all_weather_field = df.columns.get_loc('allweather_surface')
            for i in range(len(df)):
                if df.iloc[i, all_weather_field] == 1:
                    df.iloc[i, surface_field] = 'A'


        return df

    def remove_reserved_columns(self, df, extension):
        for column in self.columns_to_delete[str(extension)]:
            del df[column]
        return column

def main(path='data/raw_files', file_to_process=None):
    valid_extensions = ['1', '2', '3', '4', '5', '6', 'DRF']
    preprocessor = TidyFile()

    if file_to_process:
        file_paths = [pathlib.Path(path, file_to_process)]
    else:
        file_paths = [pathlib.Path(path, file) for file in os.listdir(path)]
        file_paths = [file for file in file_paths if file.is_file()]

    bar = Bar(f'Processing files:', max=len(file_paths), suffix='%(percent).3f%% - %(index)d/%(max)d - %(eta)s secs.')

    for file in file_paths:
        bar.next()
        logging.info(f'Processing {file.name}')

        # Only process the file if it's a valid file type
        if file.suffix[1:] not in valid_extensions:
            logging.info(f'File {file.name} not a valid file type--skipping')
            continue

        file_already_processed = (file.parent.parent / 'preprocessed_files' / (file.stem + '_processed' + file.suffix)).exists()
        if file_already_processed: continue
        extension = re.search(r'(?<=\.).+$', str(file))[0]
        table_data = pd.read_csv(file, header=None, names=name_files[str(extension)])
        table_data = preprocessor.clean_table(table_data, extension, verbose=False)
        table_data = features.add_features(table_data, extension, verbose=False)

        table_data.fillna('NULL', inplace=True)
        output_file = file.stem + '_processed' + file.suffix
        table_data.to_csv('data/preprocessed_files/' + output_file, header=True, index=False)
    bar.finish()

if __name__ == '__main__':
    main()