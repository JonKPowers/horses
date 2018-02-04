import past_perf_db_structure as tables
from def_objects import file_dtypes

pp_tables = [
    tables.horses_info_table,
    tables.trainers_info_table,
    tables.jockey_info_table,
    tables.owner_info_table,
    tables.workouts_table,
    tables.race_info_table,
    tables.horses_race_table,
    tables.horses_pp_table,
    tables.horses_stats_table,
    tables.trainer_stats_table,
    tables.jockey_stats_table,
    tables.tj_combo_stats_table,
    tables.owner_stats_table,
]

class PastPerfData:
    def process_data(self, df, db_handler):
        print('Adding data to {} in {}'.format(self.table_name, db_handler.db))
        table_data = df[self.df_col_names]
        db_handler.initialize_pp_table(self.table_name, self.dtypes, self.unique_key, self.foreign_key)
        if not self.multi_entry_table:
            db_handler.add_to_table2(self.table_name, table_data, self.sql_col_names)
        else:
            

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
        self.unique_key = structure_dict['unique_key']
        self.foreign_key = structure_dict['foreign_key']
        self.extension = structure_dict['extension']
        self.table_structure = structure_dict['db_fields']
        self.sql_col_names = [sql_col for sql_col, df_col in self.table_structure.items()]
        self.df_col_names = [df_col for sql_col, df_col in self.table_structure.items()]
        self.multi_entry_table = any(item for item in self.df_col_names if '{}' in item)
        self.dtypes = self.__create_dtype_info(structure_dict)

