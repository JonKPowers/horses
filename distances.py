import db_handler_persistent as dbh

class AddTimes:

    def race_in_db(self, db_handler=None, table=None):
        """
        Returns True if a particular race (unique track-date-race_num) is in the db; otherwise returns false
        """
        db_handler = db_handler or self.db_consolidated_races
        table = table or self.consolidated_table
        sql = f'SELECT COUNT(*) FROM {table} WHERE '
        sql += f'track = "{self.current_track}" '
        sql += f'AND date = "{self.current_date}" '
        sql += f'AND race_num = "{self.current_race_num}"'
        return db_handler.query_db(sql)[0][0]

    def add_blank_race_entry(self, db_handler, table):
        db_handler.add_to_table(table,
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
        print(sql)
        return db_handler.query_db(sql, return_col_names)

    def where_for_current_race(self, table_index=None, no_table_mapping=False):
        if no_table_mapping:
            return f'track = "{self.current_track}" ' \
                   f'AND date = "{self.current_date}" ' \
                   f'AND race_num = "{self.current_race_num}"'
        else:
            return f'{self.distance_mappings["track"][table_index]}="{self.current_track}" ' \
                   f'AND {self.distance_mappings["date"][table_index]}="{self.current_date}" ' \
                   f'AND {self.distance_mappings["race_num"][table_index]}="{self.current_race_num}"'

    def get_single_race_value(self, db_handler, table, field, no_table_mapping=False):
        table_index = self.table_mappings[table]
        sql = f'SELECT {field} FROM {table} ' + self.where_for_current_race(no_table_mapping=no_table_mapping,
                                                                            table_index=table_index)
        print(sql)
        return db_handler.query_db(sql)[0][0]

    def get_consolidated_value(self, field):
        return self.get_single_race_value(self.db_consolidated_races,
                                          self.consolidated_table,
                                          field,
                                          no_table_mapping=True)

    def get_consolidated_values(self, field_list, table_index):
        return self.query_table(self.db_consolidated_races, self.consolidated_table, field_list,
                                where=self.where_for_current_race(no_table_mapping=True))[0]

    def get_source_value(self, field):
        return self.get_single_race_value(self.db_source, self.source_table, field)

    def get_source_values(self, field_list, table_index):
        return self.query_table(self.db_source, self.source_table, field_list,
                                where=self.where_for_current_race(table_index=table_index))[0]

    def get_value_pairs(self, distance, table_index):
        column_info = [(key, value[table_index]) for key, value in self.distance_mappings[distance].items()]
        consolidated_columns = [item[0] for item in column_info]
        source_columns = [item[1] for item in column_info]
        print(f'Consolidated columns: {consolidated_columns}')
        consolidated_values = self.get_consolidated_values(consolidated_columns, table_index=table_index)
        print(f'Source columns: {source_columns}')
        source_values = self.get_source_values(source_columns, table_index=table_index)
        self.value_pair_zip = zip(consolidated_columns, consolidated_values, source_values)
        return self.value_pair_zip

    def update_single_race_value(self, db_handler, table, field, value):
        sql = f'UPDATE {table} ' \
              f'SET {field}="{value}" ' \
              f'WHERE track="{self.current_track}" ' \
              f'AND date="{self.current_date}" ' \
              f'AND race_num="{self.current_race_num}"'
        print(sql)
        db_handler.update_db(sql)

    def update_consolidated_value(self, field, value):
        self.update_single_race_value(self.db_consolidated_races, self.consolidated_table, field, value)

    def fix_time_value(self, existing_value, new_value, field):
        fix_it_dict = {
            # Key: existing value
            # Value[0]: list of new values that will trigger replacement
            # Value[1]: replacement value
            0.0: [[None], None]
        }
        try:
            if new_value in fix_it_dict[existing_value][0] or \
                    existing_value == (None, None, None, None) or \
                    existing_value == (None, None, None, None, None):
                self.update_consolidated_value(field, new_value)
        except KeyError:
            print('Existing value not found in fix_it_dict')

    def dict_values_match(self, dict_key, dict_1, dict_2):
        if dict_key in self.keys_to_ignore or dict_1[dict_key] == dict_2[dict_key]:
            return True
        else:
            return False

    def add_info(self, source_db, source_table):
        with dbh.QueryDB(db='horses_consolidated_races', initialize_db=False) as db_consolidated_races:
            with dbh.QueryDB(db=source_db, initialize_db=False) as source_db_handler:
                self.db_consolidated_races = db_consolidated_races
                self.db_source = source_db_handler
                self.source_table = source_table
                table_index = self.table_mappings[source_table]

                # Pull list of races to process from source_table
                data = self.query_table(self.db_source,
                                        self.source_table,
                                        [self.distance_mappings['track'][table_index],
                                         self.distance_mappings['date'][table_index],
                                         self.distance_mappings['race_num'][table_index],
                                         self.distance_mappings['distance'][table_index]])
                print(data[:5])

                # Loop over races and process the time data
                i = 0
                total_races = len(data)
                print(f'Total races to process: {total_races}')
                for race, distance in zip([item[:3] for item in data], [int(item[-1]) for item in data]):
                    i += 1
                    # Only process it if we've got the fractional time mappings set up
                    if distance in self.distances:
                        print(f'{i} of {total_races}: {race}')
                        self.current_track, self.current_date, self.current_race_num = race

                        # Confirm that race is in database; if not, add an entry
                        if not self.race_in_db():
                            print('Not found in db')
                            self.add_blank_race_entry(self.db_consolidated_races, 'horses_consolidated_races')

                        # Loop through the fractional times for the given race distance
                        # for fraction in self.distance_mappings[distance]:
                        #     # Grab the existing time value and new time value to be considered
                        #     existing_value = self.get_consolidated_value(fraction)
                        #     new_value = self.get_source_value(
                        #         self.distance_mappings[distance][fraction][table_index])
                        #
                        #     # If there's no time value already, add one to the db
                        #     if existing_value == None:
                        #         self.update_consolidated_value(fraction, new_value)
                        #     # If the current time value matches the new one, leave it alone
                        #     elif existing_value == new_value:
                        #         print(f'Data matches: {race[0]} {race[1]} {race[2]}')
                        #     # If there's a mismatch between the current and new time values, do something
                        #     elif not existing_value == new_value:
                        #         print('Mismatch found!')
                        #         print(f'Date: {race[0]}\nTrack: {race[1]}\nRace num: {race[2]}')
                        #         print(f'Fraction {fraction}. '
                        #               f'Existing value: {existing_value}. '
                        #               f'New value: {new_value}')
                        #         self.fix_time_value(existing_value, new_value, fraction)


                        for fraction, existing_value, new_value in self.get_value_pairs(distance, table_index):
                            print(f'Fraction: {fraction}. Existing value: {existing_value}. New value: {new_value}')
                            # If there's no time value already, add one to the db
                            if existing_value == None:
                                self.update_consolidated_value(fraction, new_value)
                            # If the current time value matches the new one, leave it alone
                            elif existing_value == new_value:
                                print(f'Data matches: {race[0]} {race[1]} {race[2]}')
                            # If there's a mismatch between the current and new time values, do something
                            elif not existing_value == new_value:
                                print('Mismatch found!')
                                print(f'Date: {race[0]}\nTrack: {race[1]}\nRace num: {race[2]}')
                                print(f'Fraction {fraction}. '
                                      f'Existing value: {existing_value}. '
                                      f'New value: {new_value}')
                                self.fix_time_value(existing_value, new_value, fraction)
                            else:
                                raise AssertionError('Something weird happened')







                    else: pass


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
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1100': ['time_fraction_3', '5f_fraction'],
                'time_1210': ['time_final', 'final_time'],
            },

            1320: {  # 6 furlongs
                'time_440': ['time_fraction_1', '2f_fraction'],
                'time_880': ['time_fraction_2', '4f_fraction'],
                'time_1100': ['time_fraction_3', '5f_fraction'],
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
                'time_1650': ['time_final', 'final_time'],
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

            'track': ('track', 'track_code',),
            'date': ('date', 'race_date',),
            'race_num': ('race_num', 'race_num',),
            'distance': ('distance', 'distance')

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
        self.db_consolidated_races = None # dbh.QueryDB(db='horses_consolidated_races', initialize_db=False)
        self.db_horses_data = None # dbh.QueryDB(db='horses_data', initialize_db=False)
        self.db_horses_errata = dbh.QueryDB(db='horses_errata', initialize_db=False)

        # Time table set-up parameters
        self.consolidated_table = 'horses_consolidated_races'










