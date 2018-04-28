    import logging
import db_handler_persistent as dbh

import numpy as np
import pandas as pd
import datetime
import re
from progress.bar import Bar

class AddHorsePerformances:
    def __init__(self):
        self.db_consolidated_races = dbh.QueryDB(db='horses_consolidated_races', initialize_db=True)
        self.db_horses_data = dbh.QueryDB(db='horses_data')
        self.db_errata = dbh.QueryDB(db='horses_errata', initialize_db=True)
        self.db_handlers = [
            self.db_consolidated_races,
            self.db_horses_data,
            self.db_errata,
        ]

        self.consolidated_table = 'horses_consolidated_performances'
        self.consolidated_table_structure = {
            # Format 'sql_col_name': ('sql_datatype', 'horses_consolidated_performances_col', 'race_horse_info_col', 'horse_pps col')
            'source_file': ('VARCHAR(255)', 'source_file', 'source_file', 'source_file', 'source_file',),
            'track': ('VARCHAR(255)', 'track', 'track', 'track', 'track_code',),
            'date': ('DATE', 'date', 'date', 'date', 'race_date',),
            'race_num': ('TINYINT', 'race_num', 'race_num', 'race_num', 'race_num',),

            'horse_name': ('VARCHAR(255)', 'horse_name', 'horse_name', None),
            'horse_id': ('VARCHAR(255)', 'horse_id', 'horse_id', None),
            'post_position':('TINYINT', 'post_position', 'post_position', None),
            'coupled_entry': ('VARCHAR(255)', 'coupled_entry', 'coupled_entry', None),
            'days_old': ('INT', 'days_old', None, None),
            'favorite': ('INT', 'favorite', 'favorite', None),

                                            
            
            'race_name': ('VARCHAR(255)', 'race_name', 'race_name', None, None,),
            'time_local': ('INT', 'time_local', 'off_time', None, None,),
            'time_zone':('VARCHAR(255)', 'time_zone', None, None, None,),

            'temperature': ('INT', 'temperature', 'race_temp', None, None,),
            'weather': ('VARCHAR(255)', 'weather', 'weather', None, None,),

            'distance': ('INT', 'distance', 'distance', 'distance', 'distance',),
            'run_up_distance': ('INT', 'run_up_distance', 'run_up_dist', None, None,),
            'temp_rail_distance': ('INT', 'temp_rail_distance', 'temp_rail_dist', None, None),
            'about_distance_flag': ('TINYINT', 'about_distance_flag', 'about_distance', None, None,),

            'surface': ('VARCHAR(255)', 'surface', 'surface_new', 'surface', 'surface',),
            # 'sealed_track'
            'track_condition': ('VARCHAR(255)', 'track_condition', 'track_condition', None, 'track_condition',),
            'chute_start': ('TINYINT', 'chute_start', 'chute_start', None, 'special_chute',),

            'off_turf': ('TINYINT', 'off_turf', 'off_turf', None, None,),
            'off_turf_dist_change': ('TINYINT', 'off_turf_dist_change', 'off_turf_distance_change', None, None),

            'field_size': ('INT', 'field_size', 'field_size', None, 'num_of_horses',),
            'breed': ('VARCHAR(255)', 'breed', 'breed', 'breed', None),

            'purse': ('INT', 'purse', 'purse', 'purse', 'race_purse',),

            'race_type': ('VARCHAR(255)', 'race_type', 'race_type_BRIS', 'race_type', 'race_type',),

            'claiming_price_base': ('INT', 'claiming_price_base', 'max_claim', 'claiming_price', 'highest_claim_price',),
            'optional_claiming_price': ('INT', 'optional_claiming_price', 'optional_claiming_price', 'optional_claiming_price', None),

            'time_440': ('FLOAT', 'time_440', None, None, None),        # 2 furlongs
            'time_660': ('FLOAT', 'time_660', None, None, None),        # 3_furlongs
            'time_880': ('FLOAT', 'time_880', None, None, None),        # 4 furlongs
            'time_1100': ('FLOAT', 'time_1100', None, None, None),       # 5 furlongs
            'time_1210': ('FLOAT', 'time_1210', None, None, None),       # 5.5 furlongs
            'time_1320': ('FLOAT', 'time_1320', None, None, None),       # 6 furlongs
            'time_1430': ('FLOAT', 'time_1430', None, None, None),       # 6.5 furlongs
            'time_1540': ('FLOAT', 'time_1540', None, None, None),       # 7 furlongs
            'time_1650': ('FLOAT', 'time_1650', None, None, None),       # 7.5 furlongs
            'time_1760': ('FLOAT', 'time_1760', None, None, None),       # 1 mile
            'time_1830': ('FLOAT', 'time_1830', None, None, None),       # 1 mile, 70 yards
            'time_1870': ('FLOAT', 'time_1870', None, None, None),       # 1 1/8 miles (9 furlongs)
            'time_1980': ('FLOAT', 'time_1980', None, None, None),       # 1 1/4 miles (10 furlongs)


            'allowed_age_two': ('TINYINT', 'allowed_age_two', 'allowed_age_two', 'allowed_age_two', 'allowed_age_two',),
            'allowed_age_three': ('TINYINT', 'allowed_age_three', 'allowed_age_three', 'allowed_age_three', 'allowed_age_three',),
            'allowed_age_four': ('TINYINT', 'allowed_age_four', 'allowed_age_four', 'allowed_age_four', 'allowed_age_four',),
            'allowed_age_five': ('TINYINT', 'allowed_age_five', 'allowed_age_five', 'allowed_age_five', 'allowed_age_five',),
            'allowed_age_older': ('TINYINT', 'allowed_age_older', 'allowed_age_older', 'allowed_age_older', 'allowed_age_older',),

            'allowed_fillies': ('TINYINT', 'allowed_fillies', 'allowed_fillies', 'allowed_fillies', 'allowed_fillies',),
            'allowed_mares': ('TINYINT', 'allowed_mares', 'allowed_mares', 'allowed_mares', 'allowed_mares',),
            'allowed_colts_geldings': ('TINYINT', 'allowed_colts_geldings', 'allowed_colts_geldings', 'allowed_colts_geldings', 'allowed_colts_geldings',),

            'statebred_race': ('TINYINT', 'statebred_race', 'statebred_race', 'statebred_race', 'statebred_race',),

            'race_conditions_1_claim_start_req_price': ('INT', 'race_conditions_1_claim_start_req_price', 'condition_1_claim_start_required_price', 'condition_1_claim_start_required_price', None,),
            'race_conditions_1_claim_start_time_limit': ('INT', 'race_conditions_1_claim_start_time_limit', 'condition_1_claim_start_required_months', 'condition_1_claim_start_required_months', None,),
            'race_conditions_1_not_won_limit': ('INT', 'race_conditions_1_not_won_limit', 'condition_1_number_limit', 'condition_1_number_limit', None,),
            'race_conditions_1_money_limit': ('INT', 'race_conditions_1_money_limit', 'condition_1_money_limit', 'condition_1_money_limit', None,),
            'race_conditions_1_time_limit': ('FLOAT', 'race_conditions_1_time_limit', 'condition_1_time_limit_months', 'condition_1_time_limit_months', None,),
            'race_conditions_1_excluded_claiming': ('TINYINT', 'race_conditions_1_excluded_claiming', 'condition_1_excluded_claiming', 'condition_1_excluded_claiming', None,),
            'race_conditions_1_excluded_maiden': ('TINYINT', 'race_conditions_1_excluded_maiden', 'condition_1_excluded_maiden', 'condition_1_excluded_maiden', None,),
            'race_conditions_1_excluded_optional': ('TINYINT', 'race_conditions_1_excluded_optional', 'condition_1_excluded_optional', 'condition_1_excluded_optional', None,),
            'race_conditions_1_excluded_restricted': ('TINYINT', 'race_conditions_1_excluded_restricted', 'condition_1_excluded_restricted', 'condition_1_excluded_restricted', None,),
            'race_conditions_1_excluded_restricted_allowance': ('TINYINT', 'race_conditions_1_excluded_restricted_allowance', 'condition_1_excluded_restricted_allowance', 'condition_1_excluded_restricted_allowance', None,),
            'race_conditions_1_excluded_starter': ('TINYINT', 'race_conditions_1_excluded_starter', 'condition_1_excluded_starter', 'condition_1_excluded_starter', None,),
            'race_conditions_1_excluded_state_sired': ('TINYINT', 'race_conditions_1_excluded_state_sired', 'condition_1_excluded_state_sired', 'condition_1_excluded_state_sired', None),
            'race_conditions_1_excluded_state_sired_stakes': ('TINYINT', 'race_conditions_1_excluded_state_sired_stakes', 'condition_1_excluded_state_sired_stakes', 'condition_1_excluded_state_sired_stakes', None,),
            'race_conditions_1_excluded_statebred': ('TINYINT', 'race_conditions_1_excluded_statebred', 'condition_1_excluded_statebred', 'condition_1_excluded_statebred', None,),
            'race_conditions_1_excluded_statebred_allowance': ('TINYINT', 'race_conditions_1_excluded_statebred_allowance', 'condition_1_excluded_statebred_allowance', 'condition_1_excluded_statebred_allowance', None,),
            'race_conditions_1_excluded_statebred_stakes': ('TINYINT', 'race_conditions_1_excluded_statebred_stakes', 'condition_1_excluded_statebred_stakes', 'condition_1_excluded_statebred_stakes', None,),
            'race_conditions_1_excluded_trial': ('TINYINT', 'race_conditions_1_excluded_trial', 'condition_1_excluded_trial', 'condition_1_excluded_trial', None,),
            'race_conditions_1_excluded_waiver': ('TINYINT', 'race_conditions_1_excluded_waiver', 'condition_1_excluded_waiver', 'condition_1_excluded_waiver', None,),
            'race_conditions_1_excluded_waiver_claiming': ('TINYINT', 'race_conditions_1_excluded_waiver_claiming', 'condition_1_excluded_waiver_claiming', 'condition_1_excluded_waiver_claiming', None,),

            'race_conditions_2_claim_start_req_price': ('INT', 'race_conditions_2_claim_start_req_price', 'condition_2_claim_start_required_price', 'condition_2_claim_start_required_price', None,),
            'race_conditions_2_claim_start_time_limit': ('INT', 'race_conditions_2_claim_start_time_limit', 'condition_2_claim_start_required_months', 'condition_2_claim_start_required_months', None,),
            'race_conditions_2_not_won_limit': ('INT', 'race_conditions_2_not_won_limit', 'condition_2_number_limit', 'condition_2_number_limit', None,),
            'race_conditions_2_money_limit': ('INT', 'race_conditions_2_money_limit', 'condition_2_money_limit', 'condition_2_money_limit', None,),
            'race_conditions_2_time_limit': ('FLOAT', 'race_conditions_2_time_limit', 'condition_2_time_limit_months', 'condition_2_time_limit_months', None,),
            'race_conditions_2_excluded_claiming': ('TINYINT', 'race_conditions_2_excluded_claiming', 'condition_2_excluded_claiming', 'condition_2_excluded_claiming', None,),
            'race_conditions_2_excluded_maiden': ('TINYINT', 'race_conditions_2_excluded_maiden', 'condition_2_excluded_maiden', 'condition_2_excluded_maiden', None,),
            'race_conditions_2_excluded_optional': ('TINYINT', 'race_conditions_2_excluded_optional', 'condition_2_excluded_optional', 'condition_2_excluded_optional', None,),
            'race_conditions_2_excluded_restricted': ('TINYINT', 'race_conditions_2_excluded_restricted', 'condition_2_excluded_restricted', 'condition_2_excluded_restricted', None,),
            'race_conditions_2_excluded_restricted_allowance': ('TINYINT', 'race_conditions_2_excluded_restricted_allowance', 'condition_2_excluded_restricted_allowance', 'condition_2_excluded_restricted_allowance', None,),
            'race_conditions_2_excluded_starter': ('TINYINT', 'race_conditions_2_excluded_starter', 'condition_2_excluded_starter', 'condition_2_excluded_starter', None,),
            'race_conditions_2_excluded_state_sired': ('TINYINT', 'race_conditions_2_excluded_state_sired', 'condition_2_excluded_state_sired', 'condition_2_excluded_state_sired', None),
            'race_conditions_2_excluded_state_sired_stakes': ('TINYINT', 'race_conditions_2_excluded_state_sired_stakes', 'condition_2_excluded_state_sired_stakes', 'condition_2_excluded_state_sired_stakes', None,),
            'race_conditions_2_excluded_statebred': ('TINYINT', 'race_conditions_2_excluded_statebred', 'condition_2_excluded_statebred', 'condition_2_excluded_statebred', None,),
            'race_conditions_2_excluded_statebred_allowance': ('TINYINT', 'race_conditions_2_excluded_statebred_allowance', 'condition_2_excluded_statebred_allowance', 'condition_2_excluded_statebred_allowance', None,),
            'race_conditions_2_excluded_statebred_stakes': ('TINYINT', 'race_conditions_2_excluded_statebred_stakes', 'condition_2_excluded_statebred_stakes', 'condition_2_excluded_statebred_stakes', None,),
            'race_conditions_2_excluded_trial': ('TINYINT', 'race_conditions_2_excluded_trial', 'condition_2_excluded_trial', 'condition_2_excluded_trial', None,),
            'race_conditions_2_excluded_waiver': ('TINYINT', 'race_conditions_2_excluded_waiver', 'condition_2_excluded_waiver', 'condition_2_excluded_waiver', None,),
            'race_conditions_2_excluded_waiver_claiming': ('TINYINT', 'race_conditions_2_excluded_waiver_claiming', 'condition_2_excluded_waiver_claiming', 'condition_2_excluded_waiver_claiming', None,),

            'race_conditions_3_claim_start_req_price': ('INT', 'race_conditions_3_claim_start_req_price', 'condition_3_claim_start_required_price', 'condition_3_claim_start_required_price', None,),
            'race_conditions_3_claim_start_time_limit': ('INT', 'race_conditions_3_claim_start_time_limit', 'condition_3_claim_start_required_months', 'condition_3_claim_start_required_months', None,),
            'race_conditions_3_not_won_limit': ('INT', 'race_conditions_3_not_won_limit', 'condition_3_number_limit', 'condition_3_number_limit', None,),
            'race_conditions_3_money_limit': ('INT', 'race_conditions_3_money_limit', 'condition_3_money_limit', 'condition_3_money_limit', None,),
            'race_conditions_3_time_limit': ('FLOAT', 'race_conditions_3_time_limit', 'condition_3_time_limit_months', 'condition_3_time_limit_months', None,),
            'race_conditions_3_excluded_claiming': ('TINYINT', 'race_conditions_3_excluded_claiming', 'condition_3_excluded_claiming', 'condition_3_excluded_claiming', None,),
            'race_conditions_3_excluded_maiden': ('TINYINT', 'race_conditions_3_excluded_maiden', 'condition_3_excluded_maiden', 'condition_3_excluded_maiden', None,),
            'race_conditions_3_excluded_optional': ('TINYINT', 'race_conditions_3_excluded_optional', 'condition_3_excluded_optional', 'condition_3_excluded_optional', None,),
            'race_conditions_3_excluded_restricted': ('TINYINT', 'race_conditions_3_excluded_restricted', 'condition_3_excluded_restricted', 'condition_3_excluded_restricted', None,),
            'race_conditions_3_excluded_restricted_allowance': ('TINYINT', 'race_conditions_3_excluded_restricted_allowance', 'condition_3_excluded_restricted_allowance', 'condition_3_excluded_restricted_allowance', None,),
            'race_conditions_3_excluded_starter': ('TINYINT', 'race_conditions_3_excluded_starter', 'condition_3_excluded_starter', 'condition_3_excluded_starter', None,),
            'race_conditions_3_excluded_state_sired': ('TINYINT', 'race_conditions_3_excluded_state_sired', 'condition_3_excluded_state_sired', 'condition_3_excluded_state_sired', None),
            'race_conditions_3_excluded_state_sired_stakes': ('TINYINT', 'race_conditions_3_excluded_state_sired_stakes', 'condition_3_excluded_state_sired_stakes', 'condition_3_excluded_state_sired_stakes', None,),
            'race_conditions_3_excluded_statebred': ('TINYINT', 'race_conditions_3_excluded_statebred', 'condition_3_excluded_statebred', 'condition_3_excluded_statebred', None,),
            'race_conditions_3_excluded_statebred_allowance': ('TINYINT', 'race_conditions_3_excluded_statebred_allowance', 'condition_3_excluded_statebred_allowance', 'condition_3_excluded_statebred_allowance', None,),
            'race_conditions_3_excluded_statebred_stakes': ('TINYINT', 'race_conditions_3_excluded_statebred_stakes', 'condition_3_excluded_statebred_stakes', 'condition_3_excluded_statebred_stakes', None,),
            'race_conditions_3_excluded_trial': ('TINYINT', 'race_conditions_3_excluded_trial', 'condition_3_excluded_trial', 'condition_3_excluded_trial', None,),
            'race_conditions_3_excluded_waiver': ('TINYINT', 'race_conditions_3_excluded_waiver', 'condition_3_excluded_waiver', 'condition_3_excluded_waiver', None,),
            'race_conditions_3_excluded_waiver_claiming': ('TINYINT', 'race_conditions_3_excluded_waiver_claiming', 'condition_3_excluded_waiver_claiming', 'condition_3_excluded_waiver_claiming', None,),

            'race_conditions_text_1': ('VARCHAR(255)', 'race_conditions_text_1', 'race_conditions_1', 'race_cond_1', None,),
            'race_conditions_text_2': ('VARCHAR(255)', 'race_conditions_text_2', 'race_conditions_2', 'race_cond_2', None,),
            'race_conditions_text_3': ('VARCHAR(255)', 'race_conditions_text_3', 'race_conditions_3', 'race_cond_3', None,),
            'race_conditions_text_4': ('VARCHAR(255)', 'race_conditions_text_4', 'race_conditions_4', 'race_cond_4', None,),
            'race_conditions_text_5': ('VARCHAR(255)', 'race_conditions_text_5', 'race_conditions_5', 'race_cond_5', None,),
            'race_conditions_text_6': ('VARCHAR(255)', 'race_conditions_text_6', None, 'race_cond_6', None,),

            # 'race_notes': (),
}

        self.errata_table = 'aggregation_notes'
        self.errata_table_structure = {
            'notes_on_data': ('TEXT',),
            'looks_like_bad_data': ('TINYINT',),
        }
        self.errata_table_structure.update(self.consolidated_table_structure)

        self.table_to_index_mappings = {
            'horses_consolidated_races': 1,
            'race_general_results' : 2,
            'race_info': 3,
            'horse_pps': 4,
        }
        self.table_to_db_mappings = {
            'race_general_results': self.db_horses_data,
            'horse_pps': self.db_horses_data,
            'horses_consolidated_races': self.db_consolidated_races,
            self.errata_table: self.db_errata,
        }
        self.column_mappings = {
            'track': ('track', 'track', 'track_code',),
            'date': ('date', 'date', 'race_date',),
            'race_num': ('race_num', 'race_num', 'race_num',),
            'distance': ('distance', 'distance', 'distance'),
        }

        # Processing variables
        self.tables_to_process = [
            'race_general_results',
            'horse_pps',
        ]
        self.tables_to_attach = [
            'race_general_results',
            'horse_pps',
            'horses_consolidated_races',
            # 'horses_errata',
        ]

        # State variables
        self.current_date = None
        self.current_track = None
        self.current_race_num = None

        self.df = {
            'race_general_results': None,
            'horse_pps': None,
            'horses_errata': None,
            'consolidated': None,
        }

        # Initialize tables
        unique = ['track', 'date', 'race_num']

        consolidated_races_dtypes = {key: value[0] for key, value in self.consolidated_table_structure.items()}
        self.db_consolidated_races.initialize_table(self.consolidated_table, consolidated_races_dtypes,
                                                    unique_key=unique, foreign_key=None)

        errata_dtypes = {key: value[0] for key, value in self.errata_table_structure.items()}
        self.db_errata.initialize_table(self.errata_table, errata_dtypes, unique_key=unique, foreign_key=None)

    def query_table(self, db_handler, table_name, fields, where='', other='', return_col_names=False):
        sql = f'SELECT {", ".join(fields)}'
        sql += f' FROM {table_name}'
        if where:
            sql += f' WHERE {where}'
        if other:
            sql += f' {other}'
        # print(sql)
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
        db_handler.add_to_table(table,
                                [[self.current_track, self.current_date, self.current_race_num]],
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

    def set_current_race_info(self, source_df, i):
        date_col = source_df.columns.get_loc('date')
        track_col = source_df.columns.get_loc('track')
        race_num_col = source_df.columns.get_loc('race_num')

        self.current_date = source_df.iloc[i, date_col]
        self.current_track = source_df.iloc[i, track_col]
        self.current_race_num = source_df.iloc[i, race_num_col]

    def update_single_race_value(self, db_handler, table, field, value):
        sql = f'UPDATE {table} ' \
              f'SET {field}="{value}" ' \
              f'WHERE track="{self.current_track}" ' \
              f'AND date="{self.current_date}" ' \
              f'AND race_num="{self.current_race_num}"'
        # print(sql)
        db_handler.update_db(sql)

    def update_race_values(self, db_handler, table, field_list, value_list, new_entry=False):
        sql = f'UPDATE {table} SET {self.concatenate_field_value_pairs(field_list, value_list)} ' \
              f'WHERE track="{self.current_track}" ' \
              f'AND date="{self.current_date}" ' \
              f'AND race_num="{self.current_race_num}"'

        if new_entry: self.add_blank_race_entry(db_handler, table)
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

    def get_time_data(self, db_handler, table):
        if table == self.errata_table:
            source_fields = self.errata_table_structure.keys()
            consolidated_fields = self.errata_table_structure.keys()
        else:
            table_index = self.table_to_index_mappings[table]
            field_dict = {key: value[table_index] for key, value in self.consolidated_table_structure.items()
                          if value[table_index]}
            source_fields = field_dict.values()
            consolidated_fields = field_dict.keys()
        data = self.query_table(db_handler, table, source_fields)
        return pd.DataFrame(data, columns=consolidated_fields)

    def attach_dfs(self, tables_to_attach=None):
        tables_to_attach = tables_to_attach or self.tables_to_attach
        # Pull each table and put data into a df located at self.df[table]
        for table in tables_to_attach:
            print(f'Attaching {table}...')
            self.df[table] = self.get_time_data(self.table_to_db_mappings[table], table)

    def add_race_ids(self):
        for table in self.tables_to_attach:
            # Gather some processing variables
            table_index = self.table_to_index_mappings[table]
            date_column = self.consolidated_table_structure['date'][table_index]
            track_column = self.consolidated_table_structure['track'][table_index]
            race_num_column = self.consolidated_table_structure['race_num'][table_index]
            df = self.df[table]

            # Zip up date, track, and race_num for races in the df being processed.
            column_data = zip(df['date'], df['track'], df['race_num'])

            # Concatenate them, add them as a column to the df, and set that as the df's index
            race_ids = [str(item[0]) + str(item[1]) + str(item[2]) for item in column_data]
            df['race_id'] = race_ids
            df.set_index('race_id', inplace=True)

    def all_consolidated_fields_blank(self,  race_id, fields):
        data = self.df[self.consolidated_table].loc[race_id, fields]
        if all([item == None or (type(item) != str and not isinstance(item, datetime.date) and np.isnan(item)) for item in data]):
            return True
        else:
            return False

    def any_consolidated_fields_blank(self,  race_id, fields):
        data = self.df[self.consolidated_table].loc[race_id, fields]
        if any([item == None or (type(item) != str and not isinstance(item, datetime.date) and np.isnan(item)) for item in data]):
            return True
        else:
            return False

    def consolidated_field_blank(self, race_id, field):
        data = self.df['consolidated'].loc[race_id, field]
        if np.isnan(data) or data == None:
            return True
        else:
            return False

    def escape_and_clean(self, item):
        escaped_item = re.sub(r"(['\\])", r'\\\1', str(item))   # Escape textual backslashes and tick marks
        cleaned_item = re.sub(u"\uFFFD", "", escaped_item)      # Fix oddball <?> character
        return cleaned_item.strip()                             # Strip off any leading or trailing whitespace

    def concatenate_field_value_pairs(self, field_list, value_list):
        value_list = [self.escape_and_clean(item) for item in value_list]
        pairs = [f'{field} = \'{value}\'' for field, value in zip(field_list, value_list)]
        return ', '.join(pairs)

    def connect_dbs(self):
        for db in self.db_handlers:
            db.connect()

    def close_dbs(self):
        for db in self.db_handlers:
            db.close()

    def process_dfs(self, table=None):
        # Allow processing of a single table if passed as an argument
        tables = table or self.tables_to_process
        print(tables)

        # Iterate through the tables to process
        for source_table in tables:
            print(f'Processing {source_table}')
            df = self.df[source_table]
            bar = Bar('Processing existing data', max=len(df))
            columns = df.columns.tolist()
            consolidated_df = self.df[self.consolidated_table]
            for i in range(len(df)):
                bar.next()
                # Get the race_id from the current row (which is the row index)
                race_id = df.iloc[i].name
                try:
                    consolidated_df.loc[race_id]    # Will fail if race_id isn't in conoslidated df,
                                                    #  so triggers exception handling

                    self.set_current_race_info(df, i)
                    # If race is in the consolidated db, check to make sure entries are not blank.
                    if self.all_consolidated_fields_blank(race_id, columns):
                        print(f'Race entry found in consolidated_df. Race id :{race_id}')
                        print(f'All fields found blank. Race id: {race_id}')
                        self.update_race_values(self.db_consolidated_races, self.consolidated_table,
                                                columns, df.iloc[i].tolist())

                    elif self.any_consolidated_fields_blank(race_id, columns):
                        race_data = df.iloc[i]
                        for column in columns:
                            column_data = consolidated_df.loc[race_id, column]
                            self.current_col_data = column_data
                            self.current_col = column
                            # If the consolidated table is missing data, try to fill it in
                            if column_data == None or (type(column_data) != str and not isinstance(column_data, datetime.date) and np.isnan(column_data)):
                                source_data = race_data[column]
                                self.current_source_data = source_data
                                # Only replace the data if the source table has data to stick in there
                                if source_data is not None and not (type(source_data) != str and not isinstance(source_data, datetime.date) and np.isnan(source_data)):
                                    print(f'Race entry found in consolidated_df. Race id :{race_id}')
                                    print(f'Updating {race_id} b/c column was empty.\n\tColumn: {column}\n\tOld Data: {column_data}. New data: {source_data}')
                                    self.update_single_race_value(self.db_consolidated_races, self.consolidated_table,
                                                                  column, source_data)
                except KeyError:
                    print(f'i: {i}--Race not in consolidated races ({race_id})')

                    self.set_current_race_info(df, i)
                    self.update_race_values(self.db_consolidated_races, self.consolidated_table,
                                            columns, df.iloc[i].tolist(), new_entry=True)
        bar.finish()

    def add_to_consolidated_table(self):
        self.connect_dbs()
        print('Attaching dfs to AddRacesInfo instance ...')
        self.attach_dfs()
        self.add_race_ids()
        print('Processing source tables ...')
        self.process_dfs()
        self.close_dbs()
        print('Done')
