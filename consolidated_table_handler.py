import logging

class TableHandler:
    def process_df(self, df, extension):
        table_data = df[list(self.df_cols_5.values())]



    def confirm_no_duplicate(self, db_handler, field, value, duplicate_confirm_field, duplicate_confirm_value):
        """
        :param db_handler:
        :param field:
        :param value:
        :param duplicate_confirm_field:
        :param duplicate_confirm_value:
        :return:    0 if there is more than one entry with test field value or if test field and
                    duplicate_confirm_field both match entry in db
                    1 if test field matches an entry but confirm field doesn't
                    2 if there are not matches on test field
        """
        sql = 'SELECT {}, {} '.format(field, duplicate_confirm_field)
        sql += 'FROM {} '.format(self.table_name)
        sql += 'WHERE {} = "{}"'.format(field, value)
        print(sql)
        results = db_handler.query_db(self.db, sql)
        print(results)
        if len(results) > 1:
            print('There were {} results in {} for query {}'.format(len(results), self.db, sql))
            print('Logging error and skipping entry')
            logging.info('There were {} results in {} for query {}:\n\t{}'.format(len(results), self.db,
                                                                                  sql, results))
            return 0
        elif len(results) == 1:
            possible_duplicate_value = results[0][1]
            if possible_duplicate_value == duplicate_confirm_value:
                print('Entry already exists for {} = {} in {}'.format(field, value, self.table_name))
                logging.info('Entry already exists for {} = {} in {}'.format(field, value, self.table_name))
                logging.info('\tTest Field: {}, Test Value: {}'.format(field, value))
                logging.info('\tConfirm Field: {}, Confirm Value: {}'.format(duplicate_confirm_field,
                                                                             duplicate_confirm_value))
                return 0
            else:
                return 1
        elif len(results) == 0:
            return 1
        else:
            logging.info('Error in TableHandler.check_for_entry()')


    class FileHandler:
        def __init__(self, setup_dict):
            for key in setup_dict.keys():
                self.key = setup_dict[key]

    def __init__(self, setup_dict, db):
        self.db = db
        self.table_name = setup_dict['table_name']
        self.sql_cols = setup_dict['sql_cols']
        self.unique = setup_dict['unique_keys']
        self.foreign = setup_dict['foreign_keys']
        self.filetypes = setup_dict['files_to_process']
        self.df_cols_5 = setup_dict['5']['field_mappings']
        # Initialize table
        db.initialize_table(self.table_name, self.sql_cols, self.unique, self.foreign)
