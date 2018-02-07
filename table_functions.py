import past_perf_db_structure as tables0
import db_structure_results as tables1
from def_objects import file_dtypes

import logging

tables = [
    tables1.race_general_results_table,
    tables1.race_notes_table,
    tables1.race_horse_info_table,
    tables1.horse_breeding_info_table,
    tables1.race_payoffs_itm_table,
    tables1.race_payoffs_exotic_table,
    tables0.horses_info_table,
    tables0.trainers_info_table,
    tables0.jockey_info_table,
    tables0.owner_info_table,
    tables0.workouts_table,
    tables0.race_info_table,
    tables0.horses_race_table,
    tables0.horses_pp_table,
    tables0.horses_stats_table,
    tables0.switches_table,
    tables0.trainer_stats_table,
    tables0.jockey_stats_table,
    tables0.tj_combo_stats_table,
    tables0.owner_stats_table,
]

class TableHandler:
    def process_data(self, df, db_handler):
        logging.debug('Adding data to {} in {}'.format(self.table_name, db_handler.db))
        if not self.table_initialized:
            db_handler.initialize_pp_table(self.table_name, self.dtypes, self.unique_key, self.foreign_key)
            self.table_initialized = True
        if self.multi_entry_table:
            for i in range(1, 11):
                col_names = [item.format(i) for item in self.df_col_names]
                table_data = df[col_names]
                db_handler.add_to_table2(self.table_name, table_data, self.sql_col_names)
        else:
            table_data = df[self.df_col_names]
            db_handler.add_to_table2(self.table_name, table_data, self.sql_col_names)


    def __create_dtype_info(self, structure_dict):
        """This takes in a dict with information about how a table should be constructed
        and outputs a dict with the keys being the column name and the values being
        the SQL data type that the columns should have."""
        dtype_info = {}
        extension = self.extension
        fields = self.table_structure
        for key, value in fields.items():
            dtype_info[key] = file_dtypes[extension][value.format('1') if self.multi_entry_table else value]
        return dtype_info

    def __init__(self, structure_dict):
        self.table_name = structure_dict['table_name']
        self.table_initialized = False
        self.unique_key = structure_dict['unique_key']
        self.foreign_key = structure_dict['foreign_key']
        self.extension = structure_dict['extension']
        self.table_structure = structure_dict['db_fields']
        self.sql_col_names = [sql_col for sql_col, df_col in self.table_structure.items()]
        self.df_col_names = [df_col for sql_col, df_col in self.table_structure.items()]
        self.multi_entry_table = any(item for item in self.df_col_names if '{}' in item)
        self.dtypes = self.__create_dtype_info(structure_dict)

