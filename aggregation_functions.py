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
            # Source file can be appended with no modification
            processed_row_data.append(self.df_results['source_file'][i])
            # Track can be appended with no modification
            processed_row_data.append(self.df_results['track'][i])
            # Date can be appended with no modificaiton
            # NOTE: Date is inserted into df as a datetime.date.
            #       Consider changing to a pd.to_datetime
            processed_row_data.append(self.df_results['date'][i])
            #race_num can be appended with no modification
            processed_row_data.append(self.df_results['race_num'][i])

            # **********Race classification fields***************
            #
            #   This will likely need a lot of parsing to be added
            processed_row_data.append(self.df_results['race_class'][i])
            processed_row_data.append(self.df_results['race_grade'][i])
            processed_row_data.append(self.df_results['race_restrictions'][i])
            processed_row_data.append(self.df_results['age_sex_restrictions'][i])
            processed_row_data.append(self.df_results['statebred_race'][i])

            # **************Distance fields***********************
            processed_row_data.append(self.df_results['run_up_dist'][i])
            processed_row_data.append(self.df_results['distance'][i])
            processed_row_data.append(self.df_results['about_distance'][i])
            processed_row_data.append(self.df_results['temp_rail_dist'][i])
            processed_row_data.append(self.df_results['chute_start'][i])


            # *************Track conditions************************
            processed_row_data.append(self.df_results['surface_new'][i])
            processed_row_data.append(None)                                             # Placeholder for 'sealed_flag'
            processed_row_data.append(self.df_results['track_condition'][i])

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
            processed_row_data.append(self.df_results['time_fraction_1'][i])
            processed_row_data.append(self.df_results['time_fraction_2'][i])
            processed_row_data.append(self.df_results['time_fraction_3'][i])
            processed_row_data.append(self.df_results['time_fraction_4'][i])
            processed_row_data.append(self.df_results['time_final'][i])

            # ************Extended race conditions*****************
            race_conditions = ''
            for j in range(1, 6):
                if self.df_results['race_conditions_' + str(j)][i]:
                    race_conditions += self.df_results['race_conditions_' + str(j)][i]
            processed_row_data.append(race_conditions)

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
            processed_row_data.append(self.df_pps['race_num'][i])                       #race_num
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
            # race_conditions

            # TO ADD:
            #   race_type
            #   race_class? Probably can delete this from fields to grab off MYSQL

            self.processed_data.append(processed_row_data)







