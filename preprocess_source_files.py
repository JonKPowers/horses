class TidyFile:
    replacement_dict_1_file = {
        'about_dist_flag': ['A', 1],
        'all_weather_flag': ['A', 1],
        'state_bred_flag': ['S', 1],
        'chute_start_flag': ['C', 1],
        'chute_start_flag': ['N', 1],
        'off_turf_flag': ['O', 1],
        'off_turf_dist_change': ['Y', 1],
        'off_turf_dist_change': ['N', 0],
        'race_grade': [0, 'NULL']
    }

    replacement_dict_2_file = {
        'nonbetting_flag': ['Y', 1],
        'disqualified_flag': ['Y', 1],
        'corrected_weight': ['Y', 1],
        'claimed_flag': ['Y', 1],
        'claimed_flag': ['N', 0],
        'dead_heat_flag': ['DH', 1],
    }

    replacement_dict_3_file = {}

    replacement_dict_4_file = {}

    replacement_dict_5_file = {}

    replacement_dict_6_file = {}

    replacement_dict_DRF_file = {
        'statebread_flag': ['s', 1],
        'today_nasal_strip_chg': [9, 'NULL'],
        'todays_meds_new': [9, 'NULL'],
        'todays_meds_old': [9, 'NULL'],
        'equipment_change': [9, 'NULL'],
        'allweather_surface': ['A', 1],
        'bris_run_style': ['NA', None],
        'past_special_chute_{i}': ['c', 1],
        'past_bar_shoe_{i}': ['r', 1],
        'past_start_code_{i}': ['X', 1],
        'past_sealed_track_indicator_{i}': ['s', 1],
        'past_all_weather_flag_{i}': ['A', 1],
        'past_equipment_{i}': ['b', 1],
        'past_entry_{i}': ['e', 1],
        'past_claimed_code_{i}': ['c', 1],
        'past_claimed_code_{i}': ['v', 1],
        'past_statebred_flag_{i}': ['s', 1],
        'past_restricted_or_qualified_{i}': ['R', 1],
    }

    replacement_dict_DRF_file_regex = {
        'past_call_pos_start_{i}': [r'[A-Za-z?*]+', 'NULL'],
        'past_call_pos_first_{i}': [r'[A-Za-z?*]+', 'NULL'],
        'past_call_pos_second_{i}': [r'[A-Za-z?*]+', 'NULL'],
        'past_call_pos_stretch_{i}': [r'[A-Za-z?*]+', 'NULL'],
        'past_call_pos_finish_{i}': [r'[A-Za-z?*]+', 'NULL'],
        # 'past_start_code_{i}': [r'[A-Za-z?*]+', 'NULL'],      # This will break the off_turf dis change feature to NULL this out
        'past_company_line_{i}': [r' ', 'X'],

    }

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
        'past_special_chute_{i}': 0,
        'past_bar_shoe_{i}': 0,
        'past_start_code_{i}': 0,
        'past_sealed_track_indicator_{i}': 0,
        'past_all_weather_flag_{i}': 0,
        'past_weight_allowance_{i}': 0,
        'past_equipment_{i}': 0,
        'past_entry_{i}': 0,
        'past_claimed_code_{i}': 0,
        'past_statebred_flag_{i}': 0,
        'past_restricted_or_qualified_{i}': 0

    }

    def __init__(self, verbose=False):
        self.verbose = verbose

    def replace_items(self, df, replacement_dict):
        for column, params in replacement_dict.items():
            if '{' in column:
                for i in range(1, 11):
                    df[column.format(i)].replace(params[0], params[1], inplace=True)
            else:
                df[column].replace(params[0], params[1], inplace=True)

    def replace_items_regex(self, df, replacement_dict):
        for column, params in replacement_dict.items():
            if '{' in column:
                for i in range(1, 11):
                    df[column.format(i)].replace(params[0], params[1], inplace=True, regex=True)
            else:
                df[column].replace(params[0], params[1], inplace=True, regex=True)

    def fill_blanks(self, df, fill_dict):
        for column, fill in fill_dict.items:
            if '{' in column:
                for i in range(1, 11):
                    df[column.format(i)].fillena(fill, inplace=True)
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

        df.fillna('NULL', inplace=True)
        return df
