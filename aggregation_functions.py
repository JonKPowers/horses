import pymysql
import pandas as pd
import numpy as np
import logging


class SQLConnection:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user=self.user,
            password=self.password
        )

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


class QueryDB:
    def query_db(self, sql_query):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self._use_db(db, cursor)
            print('Sending SQL query')
            cursor.execute(sql_query)
            print('Processing response')
            results = list(cursor)
            results_cols = [item[0] for item in cursor.description]
        return results, results_cols

    def _use_db(self, db, cursor):
        cursor.execute('USE {}'.format(self.db))
        db.commit()

    def __init__(self, db, username='codelou', password='ABCabc123!'):
        self.db = db
        self.user = username
        self.password = password


def query_table(db_handler, table_name, fields, where='', other=''):
    sql = "SELECT "
    for item in fields:
        sql += item + ', '
    sql = sql[:-2]  # Chop off last ', '
    sql += " FROM {}".format(table_name)
    if where:
        sql += " WHERE {}".format(where)
    if other:
        sql += " {}".format(other)
    print(sql)
    return db_handler.query_db(sql)


def get_8f_races(db_handler):
    sql_map = {
        # df_col: (horse_pps_field, race_general_results_field)
        'source_file': ['source_file', 'source_file'],
        'track': ['track_code', 'track'],
        'date': ['race_date', 'date'],
        'race_num': ['race_num', 'race_num'],
        'race_class': ['equibase_race_conditions', 'race_class'],
        'race_grade': [None, 'race_grade'],
        'race_restrictions': [None, 'race_restrictions'],
        'age_sex_restrictions': ['age_sex_restrictions', None],
        'statebred_race': ['statebred_race', 'statebred_race'],
        'run_up_dist': [None, 'run_up_dist'],
        'distance': ['distance', 'distance'],
        'about_distance_flag': [None, 'about_distance'],
        'temp_rail_dist': [None, 'temp_rail_dist'],
        'chute_start': [None, 'chute_start'],
        'surface': ['surface', 'surface_new'],
        'sealed_flag': ['sealed_track', None],
        'track_condition': ['track_condition', 'track_condition'],
        '2f_time': ['2f_fraction', 'time_fraction_1'],
        '4f_time':['4f_fraction', 'time_fraction_2'],
        '6f_time': ['6f_fraction', 'time_fraction_3'],
        'stretch_time': [None, 'time_fraction_4'],
        'final_time': ['final_time', 'time_final'],
        'race_conditions': [None, None],
        'num_of_horses': ['num_of_horses', None],
        'other_needed_fields': [None, ['race_conditions_1', 'race_conditions_2', 'race_conditions_3',
                                       'race_conditions_4', 'race_conditions_5''distance_fraction_1',
                                       'distance_fraction_2', 'distance_fraction_3', 'distance_fraction_4',
                                       'distance_fraction_5', 'distance_first_call', 'distance_second_call',
                                       'distance_third_call', ]]
    }
    raw_horse_pps_fields = [sql_map[item][0] for item in sql_map if sql_map[item][0]]
    horse_pps_fields = [item for item in raw_horse_pps_fields if type(item) != list]
    horse_pps_fields.extend([item for sublist in raw_horse_pps_fields for item in sublist if type(sublist) == list])

    raw_race_general_results_fields = [sql_map[item][1] for item in sql_map if sql_map[item][1]]
    race_general_results_fields = [item for item in raw_race_general_results_fields if type(item) != list]
    race_general_results_fields.extend([item for sublist in raw_race_general_results_fields
                                        for item in sublist if type(item) == list])

    values, column_names = query_table(db_handler, 'horse_pps', horse_pps_fields, where="distance = '1760'")
    print('Making dataframe')
    df_pps = pd.DataFrame(values, columns=column_names)

    values, column_names = query_table(db_handler, 'race_general_results', race_general_results_fields,
                                       where="distance = '1760'")
    print('Making dataframe')
    df_results = pd.DataFrame(values, columns=column_names)

    return df_pps, df_results, sql_map


def get_horse_pps(db_handler):
    sql_map = {
        # df_col: (horse_pps_field, race_general_results_field)
        'source_file': ['source_file', 'source_file'],
        'track': ['track_code', 'track'],
        'date': ['race_date', 'date'],
        'race_num': ['race_num','race_num'],

        'horse_name': ['horse_name', 'horse_name'],
        'program_num': [None, 'program_number'],
        'post_position': ['post_position', 'post_position'],
        'coupled_entry': [None, 'coupled_entry'],
        'number_of_horses': ['num_of_horses', None],

        'days_since_last_race': ['days_since_last_race', None],

        'odds': ['odds', None],
        'favorite': ['favorite', None],

        'disqualified': [None, 'disqualified'],
        'disqualified_placing': [None, 'disqualified_placing'],

        'weight': ['weight', 'weight'],
        'weight_corrected_flag': [None, 'weight_corrected'],
        'overweight_amount': [None, 'weight_overweight_amt'],
        'weight_allowance': ['weight_allowance', None],

        'medication': ['medication', 'medication'],
        'bute': ['medication_bute', 'bute'],
        'lasix': ['medication_lasix', 'lasix'],
        'adjunct_bleeder_meds': [None, 'adjunct_bleeder_meds'],

        'equipment': [None, 'equipment'],
        'equip_running_ws': [None, 'equip_running_ws'],
        'equip_screens': [None, 'equip_screens'],
        'equip_shields': [None, 'equip_shields'],
        'equip_aluminum_pads': [None, 'equip_aluminum_pads'],
        'equip_blinkers': ['blinkers', 'equip_blinkers'],
        'equip_mud_calks': [None, 'equip_mud_calks'],
        'equip_glued_shoes': [None, 'equip_glued_shoes'],
        'equip_inner_rims': [None, 'equip_inner_rims'],
        'equip_front_bandages': ['front_wraps', 'equip_front_bandages'],
        'equip_goggles': [None, 'equip_goggles'],
        'equip_outer_rims': [None, 'equip_outer_rims'],
        'equip_inserts': [None, 'equip_inserts'],
        'equip_aluminum_pad': [None, 'equip_aluminum_pad'],
        'equip_flipping_halter': [None, 'equip_flipping_halter'],
        'equip_bar_shoes': ['bar_shoe', 'equip_bar_shoes'],
        'equip_blocks': [None, 'equip_blocks'],
        'equip_no_whip': [None, 'equip_no_whip'],
        'equip_blinkers_off': [None, 'equip_blinkers_off'],
        'equip_pads': [None, 'equip_pads'],
        'equip_nasal_strip_off': [None, 'equip_nasal_strip_off'],
        'equip_bar_shoe': [None, 'equip_bar_shoe'],
        'equip_nasal_strip': [None, 'equip_nasal_strip'],
        'equip_turndowns': [None, 'equip_turndowns'],
        'equip_spurs': [None, 'equip_spurs'],
        'equip_equipment_item_V': [None, 'equip_equipment_item_V'],
        'equip_queens_plates': [None, 'equip_queens_plates'],
        'equip_equipment_item_X': [None, 'equip_equipment_item_X'],
        'equip_no_shoes': [None, 'equip_no_shoes'],
        'equip_tongue_tie': [None, 'equip_tongue_tie'],

        'jockey': ['jockey', 'jockey'],
        'jockey_id': [None, 'jockey_id'],
        'trainer': ['trainer', 'trainer_name'],
        'trainer_id': [None, 'trainer_id'],

        'BRIS_speed_rating': ['BRIS_speed_rating', None],
        'speed_rating': ['speed_rating', None],

        'position_start_call': ['start_call_position', 'position_start_call'],
        'position_1st_call': ['1st_call_position', 'position_1st_call'],
        'position_2d_call': ['2d_call_position', 'position_2d_call'],
        'position_3d_call': [None, 'position_3d_call'],
        'position_gate_call': ['gate_call_position', None],
        'position_stretch_call': ['stretch_call_position', 'position_stretch_call'],
        'position_finish_unofficial': ['finish_call_position', 'position_finish_unofficial'],
        'position_finish_official': [None, 'position_finish_official'],
        'dead_heat_flag': [None, 'dead_heat_finish'],

        'lead_or_beaten_lengths_start_call': ['start_call_lead_or_beaten_lengths', 'lead_or_beaten_lengths_start_call'],
        'lead_or_beaten_lengths_1st_call': ['1st_call_lead_or_beaten_lengths', 'lead_or_beaten_lengths_1st_call'],
        'lead_or_beaten_lengths_2d_call': ['2d_call_lead_or_beaten_lengths', 'lead_or_beaten_lengths_2d_call'],
        'lead_or_beaten_lengths_3d_call': [None, 'lead_or_beaten_lengths_3d_call'],
        'lead_or_beaten_lengths_gate_call': [None, None],
        'lead_or_beaten_lengths_stretch_call': ['stretch_call_lead_or_beaten_lengths', 'lead_or_beaten_lengths_stretch_call'],
        'lead_or_beaten_lengths_finish_call': ['finish_call_lead_or_beaten_lengths', 'lead_or_beaten_lengths_finish'],

        'margin_start': [None, 'margin_start_call'],
        'margin_1st_call': [None, 'margin_1st_call'],
        'margin_2d_call': [None, 'margin_2d_call'],
        'margin_3d_call': [None, 'margin_3d_call'],
        'margin_gate_call': [None, None],
        'margin_stretch_call': [None, 'margin_stretch_call'],
        'margin_finish_call': [None, 'margin_finish_call'],

        'trip_comment': ['trip_comment', 'trip_comment'],
        'trip_comment_extra': ['trip_comment_extra', None],
        'extended_start_comment': ['extended_start_comment', None],
    }

    raw_horse_pps_fields = [sql_map[key][0] for key in sql_map if sql_map[key][0]]
    horse_pps_fields = [item for item in raw_horse_pps_fields if type(item) != list]
    horse_pps_fields.extend([item for sublist in raw_horse_pps_fields
                             for item in sublist if type(sublist) == list])
    values, column_names = query_table(db_handler, 'horse_pps', horse_pps_fields)
    print('Making dataframe')
    df_pps = pd.DataFrame(values, columns=column_names)

    raw_race_horse_info_fields = [sql_map[key][1] for key in sql_map if sql_map[key][1]]
    race_horse_info_fields = [item for item in raw_race_horse_info_fields if type(item) != list]
    race_horse_info_fields.extend([item for sublist in raw_race_horse_info_fields
                                   for item in sublist if type(sublist) == list])
    values, column_names = query_table(db_handler, 'race_horse_info', race_horse_info_fields)
    print('Making dataframe')
    df_results = pd.DataFrame(values, columns=column_names)

    return df_pps, df_results, sql_map


class results_post_processing_functions:

    def log_bad_distance(self, df_results, field, dist, value, i):
        bad_race = f"{df_results['track'][i]} {df_results['date'][i]} race {df_results['race_num'][i]}"
        print(f'ISSUE({bad_race}): {field} isn\'t at {dist}. Value: {value}')
        logging.info(f'ISSUE({bad_race}): {field} isn\'t at {dist}')
        logging.info(f'\tValue: {value}')

    def check_8f_calls_and_fractions(self, df_results):
        for i in range(len(df_results)):
            # Confirm that the fractions are at 2f, 4f, and 6f and log errors:
            if df_results['distance_fraction_1'][i] != 440 and not np.isnan(
                    df_results['distance_fraction_1'][i]):
                self.log_bad_distance(df_results, 'Fraction 1', '440 yards', df_results['distance_fraction_1'][i], i)

            if df_results['distance_fraction_2'][i] != 880 and not np.isnan(
                    df_results['distance_fraction_2'][i]):
                self.log_bad_distance(df_results, 'Fraction 2', '880 yards', df_results['distance_fraction_2'][i], i)

            if df_results['distance_fraction_3'][i] != 1320 and not np.isnan(
                    df_results['distance_fraction_3'][i]):
                self.log_bad_distance(df_results, 'Fraction 3', '1320 yards', df_results['distance_fraction_3'][i], i)

            # Confirm that call distances are what we expect and log any errors:
            if df_results['distance_first_call'][i] != 440 and not np.isnan(
                    df_results['distance_first_call'][i]):
                self.log_bad_distance(df_results, 'distance_first_call', '440 yards',
                                      df_results['distance_first_call'][i], i)

            if df_results['distance_second_call'][i] != 880 and not np.isnan(
                    df_results['distance_second_call'][i]):
                self.log_bad_distance(df_results, 'distance_second_call', '880 yards',
                                      df_results['distance_second_call'][i], i)

            if df_results['distance_third_call'][i] != 1320 and not np.isnan(
                    df_results['distance_third_call'][i]):
                self.log_bad_distance(df_results, 'distance_third_call', '1320 yards',
                                      df_results['distance_third_call'][i], i)

    def consolidate_race_conditions(self, df_results):
        race_conditions = ''
        for i in range(len(df_results)):
            for j in range(1, 6):
                if df_results['race_conditions_' + str(j)][i]:
                    race_conditions += df_results['race_conditions_' + str(j)][i]
            df_results['race_conditions'][i] = race_conditions



class race:
    def __init__(self):
        pass
    # race_info
    # horses racing (organized by post position) (these might be horse objects)
    # time fractions
    # lead/beaten lengths (organized by post position)