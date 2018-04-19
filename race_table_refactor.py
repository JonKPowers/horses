import logging
import db_handler as dbh


class AddRacesInfo:
    def __init__(self):
        self.db_consolidated_races = dbh.QueryDB(db='horses_consolidated_races', initialize_db=True)
        self.db_horses_data = dbh.QueryDB(db='horses_data')
        self.db_errata = dbh.QueryDB(db='horses_errata', initialize_db=True)

        self.consolidated_table = 'horses_consolidated_races'
        self.consolidated_table_structure = {
            # Format 'sql_col_name': ('sql_datatype', 'race_general_results_col', 'race_info col', 'horse_pps col')
            'source_file': ('VARCHAR(255)', 'source_file', 'source_file', 'source_file',),
            'track': ('VARCHAR(255)', 'track', 'track', 'track_code',),
            'date': ('DATE', 'date', 'date', 'race_date',),
            'race_num': ('TINYINT', 'race_num', 'race_num', 'race_num',),
            'race_name': ('VARCHAR(255)', 'race_name', None, None,),
            'time_local': ('INT', 'off_time', None, None,),
            'time_zone':('VARCHAR(255)', None, None, None,),

            'temperature': ('INT', 'race_temp', None, None,),
            'weather': ('VARCHAR(255)', 'weather', None, None,),

            'distance': ('INT', 'distance', 'distance', 'distance',),
            'run_up_distance': ('INT', 'run_up_dist', None, None,),
            'temp_rail_distance': ('INT', 'temp_rail_dist', None, None),
            'about_distance_flag': ('TINYINT', 'about_distance', None, None,),

            'surface': ('VARCHAR(255)', 'surface_new', 'surface', 'surface',),
            # 'sealed_track'
            'track_condition': ('VARCHAR(255)', 'track_condition', None, 'track_condition',),
            'chute_start': ('TINYINT', 'chute_start', None, 'special_chute',),

            'off_turf': ('TINYINT', 'off_turf', None, None,),
            'off_turf_dist_change': ('TINYINT', 'off_turf_distance_change', None, None),

            'field_size': ('INT', 'field_size', None, 'num_of_horses',),
            'breed': ('VARCHAR(255)', 'breed', 'breed', None),

            'purse': ('INT', 'purse', 'purse', 'race_purse',),

            'race_type': ('VARCHAR(255)', 'race_type_BRIS', 'race_type', 'race_type',),

            'claiming_price_base': ('INT', 'max_claim', 'claiming_price', 'highest_claim_price',),
            'optional_claiming_price': ('INT', 'optional_claiming_price', 'optional_claiming_price', None),

            'time_440': ('FLOAT', None, None, None),        # 2 furlongs
            'time_660': ('FLOAT', None, None, None),        # 3_furlongs
            'time_880': ('FLOAT', None, None, None),        # 4 furlongs
            'time_1100': ('FLOAT', None, None, None),       # 5 furlongs
            'time_1210': ('FLOAT', None, None, None),       # 5.5 furlongs
            'time_1320': ('FLOAT', None, None, None),       # 6 furlongs
            'time_1430': ('FLOAT', None, None, None),       # 6.5 furlongs
            'time_1540': ('FLOAT', None, None, None),       # 7 furlongs
            'time_1650': ('FLOAT', None, None, None),       # 7.5 furlongs
            'time_1760': ('FLOAT', None, None, None),       # 1 mile
            'time_1830': ('FLOAT', None, None, None),       # 1 mile, 70 yards
            'time_1870': ('FLOAT', None, None, None),       # 1 1/8 miles (9 furlongs)
            'time_1980': ('FLOAT', None, None, None),       # 1 1/4 miles (10 furlongs)


            'allowed_age_two': ('TINYINT', 'allowed_age_two', 'allowed_age_two', 'allowed_age_two',),
            'allowed_age_three': ('TINYINT', 'allowed_age_three', 'allowed_age_three', 'allowed_age_three',),
            'allowed_age_four': ('TINYINT', 'allowed_age_four', 'allowed_age_four', 'allowed_age_four',),
            'allowed_age_five': ('TINYINT', 'allowed_age_five', 'allowed_age_five', 'allowed_age_five',),
            'allowed_age_older': ('TINYINT', 'allowed_age_older', 'allowed_age_older', 'allowed_age_older',),

            'allowed_fillies': ('TINYINT', 'allowed_fillies', 'allowed_fillies', 'allowed_fillies',),
            'allowed_mares': ('TINYINT', 'allowed_mares', 'allowed_mares', 'allowed_mares',),
            'allowed_colts_geldings': ('TINYINT', 'allowed_colts_geldings', 'allowed_colts_geldings', 'allowed_colts_geldings',),

            'statebred_race': ('TINYINT', 'statebred_race', 'statebred_race', 'statebred_race',),

            'race_conditions_1_claim_start_req_price': ('INT', 'condition_1_claim_start_required_price', 'condition_1_claim_start_required_price', None,),
            'race_conditions_1_claim_start_time_limit': ('INT', 'condition_1_claim_start_required_months', 'condition_1_claim_start_required_months', None,),
            'race_conditions_1_not_won_limit': ('INT', 'condition_1_number_limit', 'condition_1_number_limit', None,),
            'race_conditions_1_money_limit': ('INT', 'condition_1_money_limit', 'condition_1_money_limit', None,),
            'race_conditions_1_time_limit': ('FLOAT', 'condition_1_time_limit_months', 'condition_1_time_limit_months', None,),
            'race_conditions_1_excluded_claiming': ('TINYINT', 'condition_1_excluded_claiming', 'condition_1_excluded_claiming', None,),
            'race_conditions_1_excluded_maiden': ('TINYINT', 'condition_1_excluded_maiden', 'condition_1_excluded_maiden', None,),
            'race_conditions_1_excluded_optional': ('TINYINT', 'condition_1_excluded_optional', 'condition_1_excluded_optional', None,),
            'race_conditions_1_excluded_restricted': ('TINYINT', 'condition_1_excluded_restricted', 'condition_1_excluded_restricted', None,),
            'race_conditions_1_excluded_restricted_allowance': ('TINYINT', 'condition_1_excluded_restricted_allowance', 'condition_1_excluded_restricted_allowance', None,),
            'race_conditions_1_excluded_starter': ('TINYINT', 'condition_1_excluded_starter', 'condition_1_excluded_starter', None,),
            'race_conditions_1_excluded_state_sired': ('TINYINT', 'condition_1_excluded_state_sired', 'condition_1_excluded_state_sired', None),
            'race_conditions_1_excluded_state_sired_stakes': ('TINYINT', 'condition_1_excluded_state_sired_stakes', 'condition_1_excluded_state_sired_stakes', None,),
            'race_conditions_1_excluded_statebred': ('TINYINT', 'condition_1_excluded_statebred', 'condition_1_excluded_statebred', None,),
            'race_conditions_1_excluded_statebred_allowance': ('TINYINT', 'condition_1_excluded_statebred_allowance', 'condition_1_excluded_statebred_allowance', None,),
            'race_conditions_1_excluded_statebred_stakes': ('TINYINT', 'condition_1_excluded_statebred_stakes', 'condition_1_excluded_statebred_stakes', None,),
            'race_conditions_1_excluded_trial': ('TINYINT', 'condition_1_excluded_trial', 'condition_1_excluded_trial', None,),
            'race_conditions_1_excluded_waiver': ('TINYINT', 'condition_1_excluded_waiver', 'condition_1_excluded_waiver', None,),
            'race_conditions_1_excluded_waiver_claiming': ('TINYINT', 'condition_1_excluded_waiver_claiming', 'condition_1_excluded_waiver_claiming', None,),

            'race_conditions_2_claim_start_req_price': ('INT', 'condition_2_claim_start_required_price', 'condition_2_claim_start_required_price', None,),
            'race_conditions_2_claim_start_time_limit': ('INT', 'condition_2_claim_start_required_months', 'condition_2_claim_start_required_months', None,),
            'race_conditions_2_not_won_limit': ('INT', 'condition_2_number_limit', 'condition_2_number_limit', None,),
            'race_conditions_2_money_limit': ('INT', 'condition_2_money_limit', 'condition_2_money_limit', None,),
            'race_conditions_2_time_limit': ('FLOAT', 'condition_2_time_limit_months', 'condition_2_time_limit_months', None,),
            'race_conditions_2_excluded_claiming': ('TINYINT', 'condition_2_excluded_claiming', 'condition_2_excluded_claiming', None,),
            'race_conditions_2_excluded_maiden': ('TINYINT', 'condition_2_excluded_maiden', 'condition_2_excluded_maiden', None,),
            'race_conditions_2_excluded_optional': ('TINYINT', 'condition_2_excluded_optional', 'condition_2_excluded_optional', None,),
            'race_conditions_2_excluded_restricted': ('TINYINT', 'condition_2_excluded_restricted', 'condition_2_excluded_restricted', None,),
            'race_conditions_2_excluded_restricted_allowance': ('TINYINT', 'condition_2_excluded_restricted_allowance', 'condition_2_excluded_restricted_allowance', None,),
            'race_conditions_2_excluded_starter': ('TINYINT', 'condition_2_excluded_starter', 'condition_2_excluded_starter', None,),
            'race_conditions_2_excluded_state_sired': ('TINYINT', 'condition_2_excluded_state_sired', 'condition_2_excluded_state_sired', None),
            'race_conditions_2_excluded_state_sired_stakes': ('TINYINT', 'condition_2_excluded_state_sired_stakes', 'condition_2_excluded_state_sired_stakes', None,),
            'race_conditions_2_excluded_statebred': ('TINYINT', 'condition_2_excluded_statebred', 'condition_2_excluded_statebred', None,),
            'race_conditions_2_excluded_statebred_allowance': ('TINYINT', 'condition_2_excluded_statebred_allowance', 'condition_2_excluded_statebred_allowance', None,),
            'race_conditions_2_excluded_statebred_stakes': ('TINYINT', 'condition_2_excluded_statebred_stakes', 'condition_2_excluded_statebred_stakes', None,),
            'race_conditions_2_excluded_trial': ('TINYINT', 'condition_2_excluded_trial', 'condition_2_excluded_trial', None,),
            'race_conditions_2_excluded_waiver': ('TINYINT', 'condition_2_excluded_waiver', 'condition_2_excluded_waiver', None,),
            'race_conditions_2_excluded_waiver_claiming': ('TINYINT', 'condition_2_excluded_waiver_claiming', 'condition_2_excluded_waiver_claiming', None,),

            'race_conditions_3_claim_start_req_price': ('INT', 'condition_3_claim_start_required_price', 'condition_3_claim_start_required_price', None,),
            'race_conditions_3_claim_start_time_limit': ('INT', 'condition_3_claim_start_required_months', 'condition_3_claim_start_required_months', None,),
            'race_conditions_3_not_won_limit': ('INT', 'condition_3_number_limit', 'condition_3_number_limit', None,),
            'race_conditions_3_money_limit': ('INT', 'condition_3_money_limit', 'condition_3_money_limit', None,),
            'race_conditions_3_time_limit': ('FLOAT', 'condition_3_time_limit_months', 'condition_3_time_limit_months', None,),
            'race_conditions_3_excluded_claiming': ('TINYINT', 'condition_3_excluded_claiming', 'condition_3_excluded_claiming', None,),
            'race_conditions_3_excluded_maiden': ('TINYINT', 'condition_3_excluded_maiden', 'condition_3_excluded_maiden', None,),
            'race_conditions_3_excluded_optional': ('TINYINT', 'condition_3_excluded_optional', 'condition_3_excluded_optional', None,),
            'race_conditions_3_excluded_restricted': ('TINYINT', 'condition_3_excluded_restricted', 'condition_3_excluded_restricted', None,),
            'race_conditions_3_excluded_restricted_allowance': ('TINYINT', 'condition_3_excluded_restricted_allowance', 'condition_3_excluded_restricted_allowance', None,),
            'race_conditions_3_excluded_starter': ('TINYINT', 'condition_3_excluded_starter', 'condition_3_excluded_starter', None,),
            'race_conditions_3_excluded_state_sired': ('TINYINT', 'condition_3_excluded_state_sired', 'condition_3_excluded_state_sired', None),
            'race_conditions_3_excluded_state_sired_stakes': ('TINYINT', 'condition_3_excluded_state_sired_stakes', 'condition_3_excluded_state_sired_stakes', None,),
            'race_conditions_3_excluded_statebred': ('TINYINT', 'condition_3_excluded_statebred', 'condition_3_excluded_statebred', None,),
            'race_conditions_3_excluded_statebred_allowance': ('TINYINT', 'condition_3_excluded_statebred_allowance', 'condition_3_excluded_statebred_allowance', None,),
            'race_conditions_3_excluded_statebred_stakes': ('TINYINT', 'condition_3_excluded_statebred_stakes', 'condition_3_excluded_statebred_stakes', None,),
            'race_conditions_3_excluded_trial': ('TINYINT', 'condition_3_excluded_trial', 'condition_3_excluded_trial', None,),
            'race_conditions_3_excluded_waiver': ('TINYINT', 'condition_3_excluded_waiver', 'condition_3_excluded_waiver', None,),
            'race_conditions_3_excluded_waiver_claiming': ('TINYINT', 'condition_3_excluded_waiver_claiming', 'condition_3_excluded_waiver_claiming', None,),

            'race_conditions_text_1': ('VARCHAR(255)', 'race_conditions_1', 'race_cond_1', None,),
            'race_conditions_text_2': ('VARCHAR(255)', 'race_conditions_2', 'race_cond_2', None,),
            'race_conditions_text_3': ('VARCHAR(255)', 'race_conditions_3', 'race_cond_3', None,),
            'race_conditions_text_4': ('VARCHAR(255)', 'race_conditions_4', 'race_cond_4', None,),
            'race_conditions_text_5': ('VARCHAR(255)', 'race_conditions_5', 'race_cond_5', None,),
            'race_conditions_text_6': ('VARCHAR(255)', None, 'race_cond_6', None,),

            # 'race_notes': (),
}

        self.errata_table = 'aggregation_notes'
        self.errata_table_structure = {
            'notes_on_data': ('TEXT',),
            'looks_like_bad_data': ('TINYINT',),
        }
        self.errata_table_structure.update(self.consolidated_table_structure)

        self.table_to_index_mappings = {
            'race_general_results' : 1,
            'race_info': 2,
            'horse_pps': 3,
        }
        self.column_mappings = {
            'track': ('track', 'track', 'track_code',),
            'date': ('date', 'date', 'race_date',),
            'race_num': ('race_num', 'race_num', 'race_num',),
            'distance': ('distance', 'distance', 'distance'),
        }

        # State variables
        self.current_date = None
        self.current_track = None
        self.current_race_num = None

        # Initialize tables
        unique = ['track', 'date', 'race_num']

        consolidated_races_dtypes = {key: value[0] for key, value in self.consolidated_table_structure.items()}
        self.db_consolidated_races.initialize_table(self.consolidated_table, consolidated_races_dtypes,
                                                    unique_key=unique, foreign_key=None)

        errata_dtypes = {key: value[0] for key, value in self.errata_table_structure.items()}
        self.db_errata.initialize_table(self.errata_table, errata_dtypes, unique_key=unique, foreign_key=None)

    def query_table(db_handler, table_name, fields, where='', other='', return_col_names=False):
        sql = f'SELECT {", ".join(fields)}'
        sql += f' FROM {table_name}'
        if where:
            sql += f' WHERE {where}'
        if other:
            sql += f' {other}'
        return db_handler.query_db(sql, return_col_names)

    def race_in_db(self, db_handler=None, table=None):
        """
        Returns True if a particular race (unique track-date-race_num) is in the db; otherwise returns false.
        If no db_handler is provided, self.db_consolidated_races will be used.
        If no table is provided, self.consolidated_table will be used.
        For race info, self.current_date, self.current_track, and self.current_race_num will be used.
        """
        db_handler = db_handler or self.db_consolidated_races
        table = table or self. consolidated_table
        sql = f'SELECT COUNT(*) FROM {table} WHERE '
        sql += f'track = "{self.current_track}" '
        sql += f'AND date = "{self.current_date}" '
        sql += f'AND race_num = "{self.current_race_num}"'
        return db_handler.query_db(sql)[0][0]

    def add_blank_race_entry(self, db_handler, table):
        db_handler.add_to_table(table, [self.current_track, self.current_date, self.current_race_num],
                                ['track', 'date', 'race_num'])

    def where_for_current_race(self, table_index=None, no_table_mapping=False):
        if no_table_mapping:
            return f'track = "{self.current_track}" ' \
                   f'AND date = "{self.current_date}" ' \
                   f'AND race_num = "{self.current_race_num}"'
        else:
            return f'{self.column_mappings["track"][table_index]}="{self.current_track}" ' \
                   f'AND {self.column_mappings["date"][table_index]}="{self.current_date}" ' \
                   f'AND {self.column_mappings["race_num"][table_index]}="{self.current_race_num}"'

    def get_single_race_value(self, db_handler, table, field, no_table_mapping=False):
        table_index = self.table_to_index_mappings[table]
        sql = f'SELECT {field} from {table}' + self.where_for_current_race(table_index=table_index,
                                                                           no_table_mapping=no_table_mapping)
        print(sql)
        return db_handler.query_db(sql)[0][0]

    def update_single_race_value(self, db_handler, table, field, value):
        sql = f'UPDATE {table} ' \
              f'SET {field}="{value}" ' \
              f'WHERE track="{self.current_track}" ' \
              f'AND date="{self.current_date}" ' \
              f'AND race_num="{self.current_race_num}"'
        print(sql)
        db_handler.update_db(sql)

    def dict_values_match(self, dict_key, dict_1, dict_2):
        keys_to_ignore= ['source_file', 'race_conditions_text_1', 'race_conditions_text_2', 'race_conditions_text_3',
                         'race_conditions_text_4', 'race_conditions_text_5', 'race_conditions_text_6',]
        if dict_key in keys_to_ignore:
            return True
        elif dict_1[dict_key] == dict_2[dict_key]:
            return True
        else:
            return False

    def fix_race_type(self, db_handler, race_info_type, race_general_results_type, mismatch_category, track, date, race_num):
        fix_it_dict = {
            # Format: fix_name: race_general_results_type, race_info_type, equibase_race_type, replacement_value
            'SOC_fix': ['N', 'CO', 'SOC', 'SOC'],
            'WCL_fix': ['N', 'C', 'WCL', 'WCL'],
            'MDT_fix': ['S', 'N', 'MDT', 'MDT'],
            'STR_fix': ['R', 'N', 'STR', 'STR'],
            'HCP_fix': ['A', 'N', 'HCP', 'HCP'],
        }

        # Dict for items to ignore b/c they've already been fixed
        already_fixed_dict = {key: [value[2], value[1]] for key, value in fix_it_dict.items()}

        equibase_race_type = self.get_single_race_value(self.db_horses_data, 'race_general_results', 'race_type_equibase',
                                                   track, date,race_num)
        print(f'race_general_results data: {race_general_results_type}')
        print(f'race_info data: {race_info_type}')
        print(f'equibase_race_type: {equibase_race_type}')

        for fix in fix_it_dict:
            values = fix_it_dict[fix]
            if race_general_results_type == values[0] and race_info_type == values[1] and equibase_race_type == values[2]:
                self.update_single_race_value(db_handler, 'horses_consolidated_races', mismatch_category,
                                         values[3], track, date, race_num)
                self.add_blank_race_entry(self.db_errata, 'aggregation_notes', track, date, race_num)
                self. update_single_race_value(self.db_errata, 'aggregation_notes', mismatch_category,
                                         values[3], track, date, race_num)
                return 1

        for fixed in already_fixed_dict:
            values = already_fixed_dict[fixed]
            if race_general_results_type == values[0] and race_info_type == values[1]:
                print('No change needed--already processed')
                return 1

        return 0

    def prompt_for_user_correction_input(self, key, race):
        print('Unable to fix this issue.')
        user_input = input('(s)kip this mismatch category/mark as (b)ad/'
                           'add (n)ote/(e)nter new value/(q)uit/(C)ontinue: ').lower()
        if user_input == 'q':
            return user_input
        elif user_input == 's':
            return user_input
        elif user_input == 'b':
            self.add_blank_race_entry(self.db_errata, 'aggregation_notes', *race)
            self.update_single_race_value(self.db_errata,
                                     'aggregation_notes',
                                     'looks_like_bad_data',
                                     '1',
                                     *race)
        elif user_input == 'n':
            note = input('Enter note: ')
            self.add_blank_race_entry(self.db_errata, 'aggregation_notes', *race)
            old_note = self.get_single_race_value(self.db_errata,
                                             'aggregation_notes',
                                             'notes_on_data',
                                             *race,
                                             no_table_mapping=True)
            self.update_single_race_value(self.db_errata,
                                     'aggregation_notes',
                                     'notes_on_data',
                                     (str(old_note) + ' NEW NOTE: ' + note).strip(),
                                     *race)
        elif user_input == 'e':
            new_value = input('Enter new value: ')
            self.add_blank_race_entry(self.db_errata, 'aggregation_notes', *race)
            self.update_single_race_value(self.db_consolidated_races,
                                     'horses_consolidated_races',
                                     key,
                                     new_value,
                                     *race)
            self.update_single_race_value(self.db_errata, 'aggregation_notes', key, new_value, *race)

def process_race_general_results():
    # Create dict with sql column names and corresponding race_general_results column names
    db_dict = {key: value[table_to_index_mapping['race_general_results']] for key, value in table_structure.items()
               if value[table_to_index_mapping['race_general_results']]}
    sql_columns = [key for key, _ in db_dict.items()]
    source_columns = [db_dict[column] for column in sql_columns]

    # Pull list of race identifiers stored in race_general_results.
    list_of_races  = query_table(db_horses_data, 'race_general_results', ['track', 'date', 'race_num'])

    # For each race, pull info from db and add it to new table:
    i = 0
    for race in list_of_races:
        total_num = len(list_of_races)
        print(f'i: {i} of {total_num}. {race}')
        race_data = query_table(db_horses_data,
                                             'race_general_results',
                                             source_columns,
                                             where='track="{}" AND date="{}" AND race_num="{}"'.format(*race))
        db_consolidated_races.add_to_table(table_name, race_data, sql_columns)
        i += 1





def process_race_info(table_to_process):
    # Create dict with sql col names and corresponding columns in table_to_process
    db_dict = {key: value[table_to_index_mapping[table_to_process]] for key, value in table_structure.items()
               if value[table_to_index_mapping[table_to_process]]}
    sql_columns = [key for key, _ in db_dict.items()]
    source_columns = [db_dict[column] for column in sql_columns]

    # Pull list of race identifiers stored in table_to_process
    list_of_races = query_table(db_horses_data, table_to_process, ['track', 'date', 'race_num'])

    # Variable to hold race identifiers for data issues and UX
    races_with_inconsistent_data = []
    races_added=  []
    temp_skip_keys = []

    i = 0
    total_num = len(list_of_races)

    for race in list_of_races:
        print(f'i: {i} of {total_num}. {race}')
        in_db = race_in_db(db_consolidated_races, table_name, *race)
        race_data = query_table(db_horses_data,
                                table_to_process,
                                source_columns,
                                where='track="{}" AND date="{}" AND race_num="{}"'.format(*race))

        # If the race isn't in the db, add in data from race_info:
        if not in_db:
            print('Not in db')
            races_added.append(race)
            db_consolidated_races.add_to_table(table_name, race_data, sql_columns)
        # If it is in the db, check that values match
        else:
            print('Is in db')
            # Pull info on race from database
            data_in_db = query_table(db_consolidated_races,
                                     table_name,
                                     sql_columns,
                                     where='track="{}" AND date="{}" AND race_num="{}"'.format(*race))
            # Generate dict for each database column showing whether database info matches new info
            info_in_db = dict(zip(sql_columns, data_in_db[0]))
            new_info = dict(zip(sql_columns, race_data[0]))
            info_matches = {key: dict_values_match(key, info_in_db, new_info) for key in sql_columns}

            # Do nothing if all the info matches
            if all(info_matches.values()):
                print('All the info matches')

            # If the info doesn't all match, try to fix it. If can't, then prompt the user for what to do.
            if not all(info_matches.values()):
                races_with_inconsistent_data.append(race)
                inconsistent_keys = [key for key in info_matches.keys() if info_matches[key] == False]
                for key in inconsistent_keys:
                    if key not in temp_skip_keys:
                        print(f'**********\nMismatch ({race[0]}, {str(race[1])}, {str(race[2])})'
                              f' : {key}')
                        print(f'horse_consolidated_races: {info_in_db[key]}')
                        print(f'race_info: {new_info[key]}')

                        if fix_race_type(db_consolidated_races, new_info[key], info_in_db[key], key, *race):
                            print('Successfully fixed!')
                        else:
                            user_input = prompt_for_user_correction_input(key, race)
                            if  user_input == 'q':
                                return races_with_inconsistent_data, races_added
                            elif user_input == 's':
                                temp_skip_keys.append(key)

        i += 1
    return races_with_inconsistent_data, races_added












