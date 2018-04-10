import db_handler as dbh

class AddTimes:

    def race_in_db(self, db_handler, table):
        """
        Returns True if a particular race (unique track-date-race_num) is in the db; otherwise returns false
        """
        sql = f'SELECT COUNT(*) FROM {table} WHERE '
        sql += f'track = "{self.current_track}" '
        sql += f'AND date = "{self.current_date}" '
        sql += f'AND race_num = "{self.current_race_num}"'
        return db_handler.query_db(sql)[0][0]

    def add_blank_race_entry(self, db_handler, table):
        # Add blank row into aggregation_notes for current race if it doesn't already exist
        if not self.race_in_db(db_handler, table):
            db_handler.add_to_table('aggregation_notes',
                                    [[self.current_track, self.current_date, self.current_race_num]],
                                    ['track', 'date', 'race_num'])

    def query_table(self, db_handler, table_name, fields, where='', other='', return_col_names=False):
        sql = 'SELECT '
        for field in fields:
            sql += f'{field}, '
        sql = sql[:-2]                          # Chop off last ', '
        sql += f' FROM {table_name}'
        if where:
            sql += f' WHERE {where}'
        if other:
            sql += f' {other}'
        return db_handler.query_db(sql, return_col_names)

    def get_single_race_value(self, db_handler, table, field, no_table_mapping=False):
        if no_table_mapping:
            sql = f'SELECT {field} ' \
                  f'FROM {table} ' \
                  f'WHERE track = "{self.current_track}" ' \
                  f'AND date = "{self.current_date}" ' \
                  f'AND race_num = "{self.current_race_num}"'
        else:
            table_index = self.table_mappings[table]
            sql = f'SELECT {field} FROM {table} ' \
                  f'WHERE {self.distance_mappings["track"][table_index]}="{self.current_track}" ' \
                  f'AND {self.distance_mappings["date"][table_index]}="{self.current_date}" ' \
                  f'AND {self.distance_mappings["race_num"][table_index]}="{self.current_race_num}"'
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
        if dict_key in self.keys_to_ignore or dict_1[dict_key] == dict_2[dict_key]:
            return True
        else:
            return False

    def seed_initial_info(self, source_db_handler, source_table):
        column_dict = {key: value}


    def __init__(self):
        self.distances = [
            1100,  # 5 furlongs
            1210,  # 5.5 furlongs
            1320,  # 6 furlongs
            1430,  # 5.5 furlongs
            1540,  # 7 furlongs
            1650,  # 7.5 furlongs
            1760,  # 1 mile
            1830,  # 1 mile, 70 yards
            1870,  # 1 1/8 mile
            1980,  # 1 1/4 mile
        ]
        self.distance_mappings = {
            # race_distance: {
            #   fractional_distance_1: [race_general_results, horse_pps]
            #   fractional_distance_2: [race_general results, horse_pps]
            #   ...
            # }

            1100: {  # 5 furlongs
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1100': ['time_final', 'final_time'],

            },

            1210: {  # 5.5 furlongs
                'time_440': ['time_fraction_1' '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1110': ['time_fraction_3', '5f_fraction'],
                'time_1210': ['time_final', 'final_time'],
            },

            1320: {  # 6 furlongs
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1110': ['time_fraction_3', '5f_fraction'],
                'time_1320': ['time_final', 'final_time'],
            },

            1430: {  # 6.5 furlongs
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1320': ['time_fraction_3', '6f_fraction'],
                'time_1430': ['time_final', 'final_time'],
            },

            1540: {  # 7 furlongs
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1320': ['time_fraction_3', '6f_fraction'],
                'time_1540': ['time_final', 'final_time'],
            },

            1650: {  # 7.5 furlongs
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1320': ['time_fraction_3', '6f_fraction'],
                'time_1650': ['time_final', 'time_final'],
            },

            1760: {  # 1 mile
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1320': ['time_fraction_3', '6f_fraction'],
                'time_1760': ['time_final', 'final_time'],
            },

            1830: {  # 1 mile, 70 yards
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1320': ['time_fraction_3', '6f_fraction'],
                'time_1760': ['time_fraction_4', '8f_fraction'],
                'time_1830': ['time_final', 'final_time'],
            },

            1870: {  # 1 1/8 mile
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1320': ['time_fraction_3', '6f_fraction'],
                'time_1760': ['time_fraction_4', '8f_fraction'],
                'time_1870': ['time_final', 'final_time'],
            },

            1980: {  # 1 1/4 mile
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1320': ['time_fraction_3', '6f_fraction'],
                'time_1760': ['time_fraction_4', '8f_fraction'],
                'time_1980': ['time_final', 'final_time'],
            },

        }
        self.table_mappings = {
            'race_general_results': 0,
            'horse_pps': 1,
        }

        # State variables
        self.current_track = None
        self.current_date = None
        self.current_race_num = None
        self.keys_to_ignore = ['source_file', 'race_conditions_text_1', 'race_conditions_text_2',
                               'race_conditions_text_3', 'race_conditions_text_4', 'race_conditions_text_5',
                               'race_conditions_text_6',]

        # Set up database handlers
        self.db_consolidated_races = dbh.QueryDB(db='horses_consolidated_races', initialize_db=False)
        self.db_horses_data = dbh.QueryDB(db='horses_data', initialize_db=False)
        self.db_horses_errata = dbh.QueryDB(db='horses_errata', initialize_db=False)

        # Time table set-up parameters
        self.times_dtypes =










