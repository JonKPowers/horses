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
    sql = sql[:-2]          # Chop off last ', '
    sql += " FROM {}".format(table_name)
    if where:
        sql += " WHERE {}".format(where)
    if other:
        sql += " {}".format(other)
    print(sql)
    return db_handler.query_db(sql)


def get_8f_races(db_handler):
    horse_pps_fields = [
        'source_file',
        'track_code',
        'race_date',
        'race_num',

        'race_class',
        'race_type',
        'equibase_race_conditions',
        'age_sex_restrictions',
        'statebred_race',
        'restricted_qualified_claimer',

        'num_of_horses',

        'distance',
        'surface',
        'track_condition',
        'sealed_track',
        'all_weather_track',
        
        '2f_fraction',
        '4f_fraction',
        '6f_fraction',
        'final_time',
    ]

    race_general_results_fields = [
        'source_file',
        'track',
        'date',
        'race_num',

        'race_grade',
        'race_class',
        'age_sex_restrictions',
        'race_restrictions',
        'statebred_race',

        'run_up_dist',
        'distance',
        'about_distance',
        'temp_rail_dist',

        'time_fraction_1',
        'time_fraction_2',
        'time_fraction_3',
        'time_fraction_4',
        'time_fraction_5',
        'time_final',

        'distance_fraction_1',
        'distance_fraction_2',
        'distance_fraction_3',
        'distance_fraction_4',
        'distance_fraction_5',

        'distance_first_call',
        'distance_second_call',
        'distance_third_call',

        'race_conditions_1',
        'race_conditions_2',
        'race_conditions_3',
        'race_conditions_4',
        'race_conditions_5',

        'surface_new',
        'track_condition',
        'chute_start',
    ]

    values, column_names = query_table(db_handler, 'horse_pps', horse_pps_fields, where="distance = '1760'")
    print('Making dataframe')
    df_pps = pd.DataFrame(values, columns=column_names)

    values, column_names = query_table(db_handler, 'race_general_results', race_general_results_fields, where="distance = '1760'")
    print('Making dataframe')
    df_results = pd.DataFrame(values, columns=column_names)

    return df_pps, df_results


class df_results_8f:
    def __init__(self, df_pps, df_results):
        self.df_results = df_results
        self.df_pps = df_pps
        self.processed_data = []
        self.processed_column_names = [
            'source_file',
            'track',
            'date',
            'race_num',
            'race_class',
            'race_grade',
            'race_restrictions',
            'age_sex_restrictions',
            'statebred_race',
            'run_up_dist',
            'distance',
            'about_distance_flag',
            'temp_rail_dist',
            'chute_start',
            'surface',
            'sealed_flag',
            'track_condition',
            '2f_time',
            '4f_time',
            '6f_time',
            'stretch_time',
            'final_time',
            'race_conditions',

            'num_of_horses',
        ]
        self.process_results_data()
        self.process_pp_data()
        self.processed_df = pd.DataFrame(self.processed_data, columns=self.processed_column_names)

    def process_results_data(self):
        for i in range(len(self.df_results)):
            processed_row_data = []

            # **************Assumptions*******************
            #
            #   (1) time_fraction_4 is a stretch call time
            #   (2) time_fraction_5 is always None
            #   (3) distance_fraction_4 and distance_fraction_5 are always None
            #

            # **************General race info ********************
            #
            #
            processed_row_data.append(self.df_results['source_file'][i])                # source_file
            processed_row_data.append(self.df_results['track'][i])                      # track
            # NOTE: Date is inserted into df as a datetime.date.
            #       Consider changing to a pd.to_datetime
            processed_row_data.append(self.df_results['date'][i])                       # date
            processed_row_data.append(self.df_results['race_num'][i])                   # race_num

            # **********Race classification fields***************
            #
            #   This will likely need a lot of parsing to be added
            processed_row_data.append(self.df_results['race_class'][i])                 # race_class
            processed_row_data.append(self.df_results['race_grade'][i])                 # race_grade
            processed_row_data.append(self.df_results['race_restrictions'][i])          # race_restrictions
            processed_row_data.append(self.df_results['age_sex_restrictions'][i])       # age_sex_restrictions
            processed_row_data.append(self.df_results['statebred_race'][i])             # statebred_race

            # **************Distance fields***********************
            processed_row_data.append(self.df_results['run_up_dist'][i])                # run_up_dist
            processed_row_data.append(self.df_results['distance'][i])                   # distance
            processed_row_data.append(self.df_results['about_distance'][i])             # about_distance_flag
            processed_row_data.append(self.df_results['temp_rail_dist'][i])             # temp_rail_dist
            processed_row_data.append(self.df_results['chute_start'][i])                # chute_start


            # *************Track conditions************************
            processed_row_data.append(self.df_results['surface_new'][i])                # surface
            processed_row_data.append(None)                                             # sealed_flag
            processed_row_data.append(self.df_results['track_condition'][i])            # track_condition

            # ************Time information*************************
            # Function for logging weirdnesses:
            def log_bad_distance(field, dist, value, i):
                bad_race = f"{self.df_results['track'][i]} {self.df_results['date'][i]} race {self.df_results['race_num'][i]}"
                print(f'ISSUE({bad_race}): {field} isn\'t at {dist}. Value: {value}')
                logging.info(f'ISSUE({bad_race}): {field} isn\'t at {dist}')
                logging.info(f'\tValue: {value}')

            # Confirm that the fractions are at 2f, 4f, and 6f and log errors:
            if self.df_results['distance_fraction_1'][i] != 440 and not np.isnan(self.df_results['distance_fraction_1'][i]):
                log_bad_distance('Fraction 1','440 yards', self.df_results['distance_fraction_1'][i], i)

            if self.df_results['distance_fraction_2'][i] != 880 and not np.isnan(self.df_results['distance_fraction_2'][i]):
                log_bad_distance('Fraction 2', '880 yards', self.df_results['distance_fraction_2'][i], i)

            if self.df_results['distance_fraction_3'][i] != 1320 and not np.isnan(self.df_results['distance_fraction_3'][i]):
                log_bad_distance('Fraction 3', '1320 yards', self.df_results['distance_fraction_3'][i], i)

            # Confirm that call distances are what we expect and log any errors:
            if self.df_results['distance_first_call'][i] != 440 and not np.isnan(self.df_results['distance_first_call'][i]):
                log_bad_distance('distance_first_call', '440 yards', self.df_results['distance_first_call'][i], i)

            if self.df_results['distance_second_call'][i] != 880 and not np.isnan(self.df_results['distance_second_call'][i]):
                log_bad_distance('distance_second_call', '880 yards', self.df_results['distance_second_call'][i], i)

            if self.df_results['distance_third_call'][i] != 1320 and not np.isnan(self.df_results['distance_third_call'][i]):
                log_bad_distance('distance_third_call', '1320 yards', self.df_results['distance_third_call'][i], i)

            # Drop in the times
            processed_row_data.append(self.df_results['time_fraction_1'][i])            # 2f_time
            processed_row_data.append(self.df_results['time_fraction_2'][i])            # 4f_time
            processed_row_data.append(self.df_results['time_fraction_3'][i])            # 6f_time
            processed_row_data.append(self.df_results['time_fraction_4'][i])            # stretch_time
            processed_row_data.append(self.df_results['time_final'][i])                 # final_time

            # ************Extended race conditions*****************
            race_conditions = ''
            for j in range(1, 6):
                if self.df_results['race_conditions_' + str(j)][i]:
                    race_conditions += self.df_results['race_conditions_' + str(j)][i]
            processed_row_data.append(race_conditions)                                  # race_conditions

            processed_row_data.append(None)                                             # num_of_horses
                                                                                        # need to add this
                                                                                        # as a feature

            # **********Add the row data to the master list******
            #
            #
            self.processed_data.append(processed_row_data)

    def process_pp_data(self):
        for i in range(len(self.df_pps)):
            processed_row_data = []

            # ************Assumptions********************
            #   (1) restricted_qualified_claimer is never 1 (field doesn't seem to be used for anything)
            #   (2) 1st_call_fraction always equals 2f_fraction
            #   (3) 2d_call_fraction always equals 4f_fraction
            #   (4) 3d_call_fraction always equals 6f_fraction
            #
            processed_row_data.append(self.df_pps['source_file'][i])                    # source_file
            processed_row_data.append(self.df_pps['track_code'][i])                     # track
            processed_row_data.append(self.df_pps['race_date'][i])                      # date
            processed_row_data.append(self.df_pps['race_num'][i])                       # race_num
            processed_row_data.append(self.df_pps['equibase_race_conditions'][i])       # race_class
                                                                                        # maybe race_class would
                                                                                        # be better for this one
            processed_row_data.append(None)                                             # race_grade
            processed_row_data.append(None)                                             # race_restrictions
            processed_row_data.append(self.df_pps['age_sex_restrictions'][i])           # age_sex_restrictions
            processed_row_data.append(self.df_pps['statebred_race'][i])                 # statebred_race
            processed_row_data.append(None)                                             # run_up_dist
            processed_row_data.append(self.df_pps['distance'][i])                       # distance
            processed_row_data.append(None)                                             # about_distance_flag
                                                                                        # Need to add this once
                                                                                        # tidy_it_up is updated.
            processed_row_data.append(None)                                             # temp_rail_dist
            processed_row_data.append(None)                                             # chute_start
            processed_row_data.append(self.df_pps['surface'][i])                        # surface
            processed_row_data.append(self.df_pps['sealed_track'][i])                   # sealed_track
            processed_row_data.append(self.df_pps['track_condition'][i])                # track_condition
            processed_row_data.append(self.df_pps['2f_fraction'][i])                    # 2f_time
            processed_row_data.append(self.df_pps['4f_fraction'][i])                    # 4f_time
            processed_row_data.append(self.df_pps['6f_fraction'][i])                    # 6f_time
            processed_row_data.append(None)                                             # stretch_time
            processed_row_data.append(self.df_pps['final_time'][i])                     # final_time
            processed_row_data.append(None)                                             # race_conditions

            processed_row_data.append(self.df_pps['num_of_horses'])                     # num_of_horses

            # TO ADD:
            #   race_type
            #   race_class? Probably can delete this from fields to grab off MYSQL

            self.processed_data.append(processed_row_data)


def get_8f_horse_pps(db_handler):
    horse_pps_fields = [
        'source_file',
        'track_code',
        'race_date',
        'race_num',

        'horse_name',
        'post_position',
        'odds',
        'favorite',

        'trainer',
        'jockey',

        'blinkers',
        'medication',
        'medication_lasix',
        'medication_bute',
        'front_wraps',
        'bar_shoe',
        'start_code',

        'weight',
        'weight_allowance',

        'days_since_last_race',
        'num_of_horses',

        'trip_comment',
        'trip_comment_extra',
        'extended_start_comment',

        'BRIS_speed_rating',
        'speed_rating',

        'start_call_position',
        '1st_call_position',
        '2d_call_position',
        'gate_call_position',
        'stretch_call_position',
        'finish_call_position',

        'start_call_lead_or_beaten_margin',
        '1st_call_lead_or_beaten_margin',
        '2d_call_lead_or_beaten_margin',
        'stretch_call_lead_or_beaten_margin',
        'finish_call_lead_or_beaten_margin',

        'start_call_beaten_lengths',
        '1st_call_beaten_lengths',
        '2d_call_beaten_lengths',
        'stretch_call_beaten_lengths',
        'finish_call_beaten_lengths',
    ]

    race_horse_info_fields = [
        'source_file',
        'track',
        'date',
        'race_num',
        'horse_name',
        'program_number',
        'post_position',
        'coupled_entry',

        'disqualified',
        'disqualified_placing',
        'weight',
        'weight_corrected',
        'weight_overweight_amt',
        'medication',
        'adjunct_bleeder_meds',
        'bute',
        'lasix',

        'equipment',
        'equip_running_ws',
        'equip_screens',
        'equip_shields',
        'equip_aluminum_pads',
        'equip_blinkers',
        'equip_mud_calks',
        'equip_glued_shoes',
        'equip_inner_rims',
        'equip_front_bandages',
        'equip_goggles',
        'equip_outer_rims',
        'equip_inserts',
        'equip_aluminum_pad',
        'equip_flipping_halter',
        'equip_bar_shoes',
        'equip_blocks',
        'equip_no_whip',
        'equip_blinkers_off',
        'equip_pads',
        'equip_nasal_strip_off',
        'equip_bar_shoe',
        'equip_nasal_strip',
        'equip_turndowns',
        'equip_spurs',
        'equip_equipment_item',
        'equip_queens_plates',
        'equip_no_shoes',
        'equip_tongue_tie',

        'jockey',
        'trainer_name',
        'jockey_id',
        'trainer_id',

        'position_start_call',
        'position_1st_call',
        'position_2d_call',
        'position_3d_call',
        'position_stretch_call',
        'position_finish_unofficial',
        'position_finish_official',
        'dead_heat_finish',

        'lead_start_call',
        'lead_1st_call',
        'lead_2d_call',
        'lead_3d_call',
        'lead_stretch_call',
        'lead_finish_call',

        'beaten_start_call',
        'beaten_1st_call',
        'beaten_2d_call',
        'beaten_3d_call',
        'beaten_stretch_call',
        'beaten_finish_call',

        'margin_start_call',
        'margin_1st_call',
        'margin_2d_call',
        'margin_3d_call',
        'margin_stretch_call',
        'margin_finish_call',

        'trip_comment',

    ]


    values, column_names = query_table(db_handler, 'horse_pps', horse_pps_fields)
    print('Making dataframe')
    df_pps = pd.DataFrame(values, columns=column_names)

    values, column_names = query_table(db_handler, 'race_horse_info', race_horse_info_fields)
    print('Making dataframe')
    df_results = pd.DataFrame(values, columns=column_names)

    return df_pps, df_results


class df_pps:
    def __init__(self, df_pps, df_results):
        self.df_pps = df_pps
        self.df_results = df_results
        self.processed_pps_data = []
        self.processed_result_data = []
        self.processed_data = []
        self.processed_column_names = [
            'source_file',
            'track',
            'date',
            'race_num',

            'horse_name',
            'program_num',
            'post_position',
            'coupled_entry',

            'days_since_last_race',

            'odds',
            'favorite',

            'disqualified',
            'disqualified_placing',


            'weight',
            'weight_corrected_flag',
            'overweight_amount',
            'weight_allowance',

            'medication',
            'bute',
            'lasix',
            'adjunct_bleeder_meds',

            'equipment',
            'equip_running_ws',
            'equip_screens',
            'equip_shields',
            'equip_aluminum_pads',
            'equip_blinkers',
            'equip_mud_calks',
            'equip_glued_shoes',
            'equip_inner_rims',
            'equip_front_bandages',
            'equip_goggles',
            'equip_outer_rims',
            'equip_inserts',
            'equip_aluminum_pad',
            'equip_flipping_halter',
            'equip_bar_shoes',
            'equip_blocks',
            'equip_no_whip',
            'equip_blinkers_off',
            'equip_pads',
            'equip_nasal_strip_off',
            'equip_bar_shoe',
            'equip_nasal_strip',
            'equip_turndowns',
            'equip_spurs',
            'equip_equipment_item',
            'equip_queens_plates',
            'equip_no_shoes',
            'equip_tongue_tie',

            'jockey',
            'trainer',

            'BRIS_speed_rating',
            'speed_rating',

            'position_start_call',
            'position_1st_call',
            'position_2d_call',
            'position_3d_call',
            'position_gate_call',
            'position_stretch_call',
            'position_finish_unofficial',
            'position_finish_official',
            'dead_heat_flag',

            'lead_beaten_lengths_start_call',
            'lead_beaten_lengths_1st_call',
            'lead_beaten_lengths_2d_call',
            'lead_beaten_lengths_3d_call',
            'lead_beaten_lengths_gate_call',
            'lead_beaten_lengths_stretch_call',
            'lead_beaten_lengths_finish',

            'margin_start',
            'margin_1st_call',
            'margin_2d_call',
            'margin_3d_call',
            'margin_gate_call',
            'margin_stretch_call',
            'margin_finish',

            'trip_comment',
            'trip_comment_extra',
            'extended_start_comment',
        ]
        self.process_pp_data()
        self.process_results_data()
        self.processed_df = pd.DataFrame(self.processed_data, columns=self.processed_column_names)

    def process_results_data(self):
            for i in range(len(self.df_results)):
                row_data = []

                row_data.append(self.df_results['source_file'][i])              # source_file
                row_data.append(self.df_results['track'][i])                    # track
                row_data.append(self.df_results['date'][i])                     # date
                row_data.append(self.df_results['race_num'][i])                 # race_num

                row_data.append(self.df_results['horse_name'][i])               # horse_name
                row_data.append(self.df_results['program_number'][i])           # program_num
                row_data.append(self.df_results['post_position'][i])            # post_position
                row_data.append(self.df_results['coupled_entry'][i])            # coupled_entry

                row_data.append(None)                                           # days_since_last_race


                row_data.append(None)                                           # odds
                row_data.append(None)                                           # favorite

                row_data.append(self.df_results['disqualified'][i])             # disqualified
                row_data.append(self.df_results['disqualified_placing'][i])     # disqualified_placing

                row_data.append(self.df_results['weight'][i])                   # weight
                row_data.append(self.df_results['weight_corrected'][i])         # weight_corrected_flag
                row_data.append(self.df_results['weight_overweight_amt'][i])    # overweight_amount
                row_data.append(None)                                           # weight_allowance

                row_data.append(self.df_results['medication'][i])               # medication
                row_data.append(self.df_results['bute'][i])                     # bute
                row_data.append(self.df_results['lasix'][i])                    # lasix
                row_data.append(None)                                           # adjunct_bleeder_meds

                row_data.append(self.df_results['equipment'][i])                # equipment
                equipment_list = ['equip_running_ws', 'equip_screens', 'equip_shields', 'equip_aluminum_pads',
                                  'equip_blinkers', 'equip_mud_calks', 'equip_glued_shoes', 'equip_inner_rims',
                                  'equip_front_bandages', 'equip_goggles', 'equip_outer_rims', 'equip_inserts',
                                  'equip_aluminum_pad', 'equip_flipping_halter', 'equip_bar_shoes', 'equip_blocks',
                                  'equip_no_whip', 'equip_blinkers_off', 'equip_pads', 'equip_nasal_strip_off',
                                  'equip_bar_shoe', 'equip_nasal_strip', 'equip_turndowns', 'equip_spurs',
                                  'equip_equipment_item', 'equip_queens_plates', 'equip_no_shoes', 'equip_tongue_tie']
                for item in equipment_list:                                     # equip_running_ws
                    row_data.append(self.df_results[item][i])                   # equip_screens
                                                                                # equip_shields
                                                                                # equip_aluminum_pads
                                                                                # equip_blinkers
                                                                                # equip_mud_calks
                                                                                # equip_glued_shoes
                                                                                # equip_inner_rims
                                                                                # equip_front_bandages
                                                                                # equip_goggles
                                                                                # equip_outer_rims
                                                                                # equip_inserts
                                                                                # equip_aluminum_pad
                                                                                # equip_flipping_halter
                                                                                # equip_bar_shoes
                                                                                # equip_blocks
                                                                                # equip_no_whip
                                                                                # equip_blinkers_off
                                                                                # equip_pads
                                                                                # equip_nasal_strip_off
                                                                                # equip_bar_shoe
                                                                                # equip_nasal_strip
                                                                                # equip_turndowns
                                                                                # equip_spurs
                                                                                # equip_equipment_item
                                                                                # equip_queens_plates
                                                                                # equip_no_shoes
                                                                                # equip_tongue_tie

                row_data.append(self.df_results['jockey'][i])                   # jockey
                row_data.append(self.df_results['trainer_name'][i])             # trainer

                row_data.append(None)                                           # BRIS_speed_rating
                row_data.append(None)                                           # speed_rating

                row_data.append(self.df_results['position_start_call'][i])      # position_start_call
                row_data.append(self.df_results['position_1st_call'][i])        # position_1st_call
                row_data.append(self.df_results['position_2d_call'][i])         # position_2d_call
                row_data.append(self.df_results['position_3d_call'][i])         # position_3d_call
                row_data.append(None)                                           # position_gate_call
                row_data.append(self.df_results['position_stretch_call'][i])    # position_stretch_call
                row_data.append(self.df_results['position_finish_unofficial'][i])# position_finish_unofficial
                row_data.append(self.df_results['position_finish_official'][i]) # position_finish_official
                row_data.append(self.df_results['dead_heat_finish'][i])         # dead_heat_flag

                # Loop through these lead/beaten columns to generate a lead/beaten lengths number.
                # A negative number indicates beaten lengths; a positive number indicates the leader.
                calls = ['start', '1st', '2d', '3d']
                for call in calls:
                    if self.df_results[f'lead_{call}_call'][i]:
                        row_data.append(self.df_results[f'lead_{call}_call'][i])
                    else:
                        row_data.append(self.df_results[f'beaten_{call}_call'][i] * -1)
                                                                                    # lead_beaten_lengths_start_call
                                                                                    # lead_beaten_lengths_1st_call
                                                                                    # lead_beaten_lengths_2d_call
                                                                                    # lead_beaten_lengths_3d_call

                row_data.append(None)                                               # lead_beaten_lengths_gate_call

                calls = ['stretch', 'finish']
                for call in calls:
                    if self.df_results[f'lead_{call}_call'][i]:
                        row_data.append(self.df_results[f'lead_{call}_call'][i])
                    else:
                        row_data.append(self.df_results[f'beaten_{call}_call'][i] * -1)
                                                                                    # lead_beaten_lengths_stretch_call
                                                                                    # lead_beaten_lengths_finish
                calls = ['start', '1st', '2d', '3d']
                for call in calls:
                    row_data.append(self.df_results[f'margin_{call}_call'])         # margin_start
                                                                                    # margin_1st_call
                                                                                    # margin_2d_call
                                                                                    # margin_3d_call

                row_data.append(None)                                               # margin_gate_call

                calls = ['stretch', 'finish']                                       # margin_stretch_call
                for call in calls:                                                  # margin_finish
                    row_data.append(self.df_results[f'margin_{call}_call'])

                row_data.append(self.df_results['trip_comment'])                    # trip_comment
                row_data.append(None)                                               # trip_comment_extra
                row_data.append(None)                                               # extended_start_comment





                # Add the data to the main data list
                self.processed_data.append(row_data)

    def process_pp_data(self):
            # ***************Assumptions***************************
            #
            #   (1) finish_call_position is the unofficial finishing position. (The trip_comment_extra field
            #       seems to have info on official finish changes due to disqualification.)
            #

            for i in range(len(self.df_pps)):
                row_data = []
                row_data.append(self.df_pps['source_file'][i])                  # source_file
                row_data.append(self.df_pps['track_code'][i])                   # track
                row_data.append(self.df_pps['race_date'][i])                    # date
                row_data.append(self.df_pps['race_num'][i])                     # race_num

                row_data.append(self.df_pps['horse_name'][i])                   # horse_name
                row_data.append(None)                                           # program_num
                row_data.append(self.df_pps['post_position'][i])                # post_position
                row_data.append(None)                                           # coupled_entry

                row_data.append(self.df_pps['days_since_last_race'][i])         # days_since_last_race


                row_data.append(self.df_pps['odds'][i])                         # odds
                row_data.append(self.df_pps['favorite'][i])                     # favorite

                row_data.append(None)                                           # disqualified
                row_data.append(None)                                           # disqualified_placing

                row_data.append(self.df_pps['weight'][i])                       # weight
                row_data.append(None)                                           # weight_corrected
                row_data.append(None)                                           # overweight_amount
                row_data.append(self.df_pps['weight_allowance'][i])             # weight_allowance

                row_data.append(self.df_pps['medication'][i])                   # medication
                row_data.append(self.df_pps['medication_bute'][i])              # bute
                row_data.append(self.df_pps['medication_lasix'][i])             # lasix
                row_data.append(None)                                           # adjunct_bleeder_meds

                row_data.append(None)                                           # equipment
                row_data.append(None)                                           # equip_running_ws
                row_data.append(None)                                           # equip_screens
                row_data.append(None)                                           # equip_shields
                row_data.append(None)                                           # equip_aluminum_pads
                row_data.append(self.df_pps['blinkers'][i])                     # equip_blinkers
                row_data.append(None)                                           # equip_mud_calks
                row_data.append(None)                                           # equip_glued_shoes
                row_data.append(None)                                           # equip_inner_rims
                row_data.append(self.df_pps['front_wraps'][i])                  # equip_front_bandages
                row_data.append(None)                                           # equip_goggles
                row_data.append(None)                                           # equip_outer_rims
                row_data.append(None)                                           # equip_inserts
                row_data.append(None)                                           # equip_aluminum_pad
                row_data.append(None)                                           # equip_flipping_halter
                row_data.append(self.df_pps['bar_shoe'][i])                     # equip_bar_shoes
                row_data.append(None)                                           # equip_blocks
                row_data.append(None)                                           # equip_no_whip
                row_data.append(None)                                           # equip_blinkers_off
                row_data.append(None)                                           # equip_pads
                row_data.append(None)                                           # equip_nasal_strip_off
                row_data.append(None)                                           # equip_bar_shoe
                row_data.append(None)                                           # equip_nasal_strip
                row_data.append(None)                                           # equip_turndowns
                row_data.append(None)                                           # equip_spurs
                row_data.append(None)                                           # equip_equipment_item
                row_data.append(None)                                           # equip_queens_plates
                row_data.append(None)                                           # equip_no_shoes
                row_data.append(None)                                           # equip_tongue_tie

                row_data.append(self.df_pps['jockey'][i])                       # jockey
                row_data.append(self.df_pps['trainer'][i])                      # trainer

                row_data.append(self.df_pps['BRIS_speed_rating'][i])            # BRIS_speed_rating
                row_data.append(self.df_pps['speed_rating'][i])                 # speed_rating

                calls = ['start', '1st', '2d']
                for call in calls:
                    row_data.append(self.df_pps[f'{call}_call_position'][i])    # position_start_call
                                                                                # position_1st_call
                                                                                # position_2d_call

                row_data.append(None)                                           # position_3d_call

                calls = ['gate', 'stretch', 'finish']                           # position_gate_call
                for call in calls:                                              # position_stretch_call
                    row_data.append(self.df_pps[f'{call}_call_position'][i])    # position_finish_unofficial

                row_data.append(None)                                           # position_finish_official
                row_data.append(None)                                           # dead_heat_flag

                calls = ['start', '1st', '2d']
                for call in calls:
                    lead_beaten_col = self.df_pps.columns.get_loc(f'{call}_call_lead_or_beaten_margin')
                    beaten_only_col = self.df_pps.columns.get_loc(f'{call}_call_beaten_lengths')
                    if np.isnan(self.df_pps.iloc[i, lead_beaten_col]):
                        row_data.append(self.df_pps.iloc[i, beaten_only_col] * -1)
                    else:
                        row_data.append(self.df_pps.iloc[i, lead_beaten_col])
                                                                                # lead_beaten_lengths_start_call
                                                                                # lead_beaten_lengths_1st_call
                                                                                # lead_beaten_lengths_2d_call

                row_data.append(None)                                           # lead_beaten_lengths_3d_call

                calls = ['gate', 'stretch', 'finish']
                for call in calls:
                    if np.isnan(self.df_pps.iloc[i, lead_beaten_col]):
                        row_data.append(self.df_pps.iloc[i, beaten_only_col] * -1)
                    else:
                        row_data.append(self.df_pps.iloc[i, lead_beaten_col])
                                                                                # lead_beaten_length_gate_call
                                                                                # lead_beaten_lengths_stretch_call
                                                                                # lead_beaten_lengths_finish

                row_data.append(None)                                           # margin_start
                row_data.append(None)                                           # margin_1st_call
                row_data.append(None)                                           # margin_2d_call
                row_data.append(None)                                           # margin_3d_call
                row_data.append(None)                                           # margin_gate_call
                row_data.append(None)                                           # margin_stretch_call
                row_data.append(None)                                           # margin_finish

                row_data.append(self.df_pps['trip_comment'][i])                 # trip_comment
                row_data.append(self.df_pps['trip_comment_extra'][i])           # trip_comment_extra

                row_data.append(self.df_pps['extended_start_comment'][i])       # extended_start_comment

                self.processed_data.append(row_data)





