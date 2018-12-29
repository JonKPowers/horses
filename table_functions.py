import db_structure_past_perf as tables0
import db_structure_results as tables1
from csv_definitions import file_dtypes

import logging
import pandas as pd

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
    def __init__(self, structure_dict, db):
        self.table_name = structure_dict['table_name']
        self.unique_key = structure_dict['unique_key']
        self.foreign_key = structure_dict['foreign_key']
        self.not_null = structure_dict['not_null']
        self.extension = structure_dict['extension']
        self.table_structure = structure_dict['db_fields']
        self.sql_col_names = [sql_col for sql_col, _ in self.table_structure.items()]
        self.df_col_names = [df_col for _, df_col in self.table_structure.items()]
        self.multi_entry_table = any(item for item in self.df_col_names if '{}' in item)
        self.dtypes = self.__create_dtype_info()
        db.initialize_table(self.table_name, self.dtypes, self.unique_key, self.foreign_key)

    def process_data(self, df, db_handler, file_name=''):

        def empty_not_null_fields():
            if len(self.not_null) != 0:
                for col in self.not_null:
                    if pd.isnull(subrow_data[col.format(i)]):
                        return True
            return False

        # Set up cursor for the db to use.
        db_handler.cursor = db_handler.set_up_cursor()

        # Trim the dataframe down to the columns relevant to this table type
        drop_cols = [col for col in df.columns if col not in self.expand_multi_entry_fields(self.df_col_names)]
        trimmed_df = df.drop(drop_cols, axis=1)

        # Loop through each row of the trimmed df and add the info to the table.
        for _, row_data in trimmed_df.iterrows():
            if not self.multi_entry_table:
                values = row_data[self.df_col_names].values
                sql_col_names = self.sql_col_names
                db_handler.add_new_entry(self.table_name, sql_col_names, values, commit=False)
            else:
                # For multi-entry tables, create each "subrow" and check if any of the not_null columns are null.
                # If they're not there, skip to the next "subrow"; otherwise proceed as normal and add entry to db.
                for i in range(1, 11):
                    subrow_data = row_data[[column.format(i) for column in self.df_col_names]]
                    if empty_not_null_fields(): continue
                    values = subrow_data.values
                    sql_col_names = self.sql_col_names
                    db_handler.add_new_entry(self.table_name, sql_col_names, values, commit=False)
        db_handler.cursor = None
        db_handler.connection.commit()

    def expand_multi_entry_fields(self, df_cols):
        expanded_list = list()
        for item in df_cols:
            if '{}' not in item:
                expanded_list.append(item)
            else:
                for i in range(1, 11):
                    expanded_list.append(item.format(i))
        return expanded_list

    def __create_dtype_info(self):
        """This takes in a dict with information about how a table should be constructed
        and outputs a dict with the keys being the column name and the values being
        the SQL data type that the columns should have."""

        dtype_info = {}
        extension = self.extension
        fields = self.table_structure
        for key, value in fields.items():
            dtype_info[key] = file_dtypes[extension][value.format('1') if self.multi_entry_table else value]
        return dtype_info




