import past_perf_db_structure as db_struct
import database_functions as db_functions
from def_objects import file_dtypes

def create_db_schema(structure_object):
    """This takes in a dict with information about how a table should be constructed
    and outputs a dict with the keys being the column name and the values being
    the SQL data type that the columns should have."""
    schema_object = {}
    extension = structure_object['extension']
    fields = structure_object['db_fields']
    multi_entry_table = any(item for item in list(fields.values()) if '{}' in item)
    for key, value in fields.items():
        schema_object[key] = file_dtypes[extension][value.format('1') if multi_entry_table else value]
    return schema_object

class PastPerfData:
    def __create_dtype_info(self, structure_dict):
        """This takes in a dict with information about how a table should be constructed
        and outputs a dict with the keys being the column name and the values being
        the SQL data type that the columns should have."""
        dtype_info = {}
        extension = self.extension
        fields = self.sql_table_cols
        for key, value in fields.items():
            dtype_info[key] = file_dtypes[extension][value.format('1') if self.multi_entry_table else value]
        return dtype_info

    def __init__(self, structure_dict):
        self.table_name = structure_dict['table_name']
        self.unique_key = structure_dict['unique_key']
        self.foreign_key = structure_dict['foreign_key']
        self.extension = structure_dict['extension']
        self.sql_table_cols = structure_dict['db_fields']
        self.df_table_cols = list(self.sql_table_cols.values())
        self.multi_entry_table = any(item for item in list(self.sql_table_cols.values()) if '{} in item')
        self.dtypes = self.__create_dtype_info(structure_dict)

