import pymysql.cursors
import re
import logging

class DbHandler:
    def __init__(self, db='horses_test', username='codelou', password='ABCabc123!', initialize_db=False):
        self.db = db
        self.user = username
        self.password = password
        self.connection = None
        if initialize_db == True:
            self.connect_db()
            self.initialize_db()

    def connect_db(self):
        if not self.connection:
            self.connection = pymysql.connect(
                host='localhost',
                user=self.user,
                password=self.password
            )

    def close_db(self):
        if self.connection:
            self.connection.close()

    def query_db(self, sql_query):
        cursor = self.connection.cursor()
        self.__use_db(cursor)
        cursor.execute(sql_query)
        results = list(cursor)
        results_cols = [item[0] for item in cursor.description]
        return results, results_cols

    def update_db(self, sql_query):
        cursor = self.connection.cursor()
        self.__use_db(cursor)
        print('Sending SQL update query')
        print(sql_query)
        cursor.execute(sql_query)
        self.connection.commit()
        print('Update query sent; change committed')
        return None

    def initialize_db(self):
        """Checks to see if db exists. If not, creates it."""
        cursor = self.connection.cursor()
        sql = f'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = "{self.db}"'
        db_exists = cursor.execute(sql)
        if db_exists:
            print(f'Database {self.db} already exists--skipping create step')
        elif db_exists == 0:
            self.__create_db(cursor)
            print(f'Created new database {self.db}')
        else:
            print(f'There was a problem checking whether {self.db} exists--unexpected db_exists value.')

    def initialize_table(self, table_name, dtypes, unique_key, foreign_key):
        """Checks to see if a table exists. If not, creates it."""
        cursor = self.connection.cursor()
        self.__use_db(cursor)
        sql = 'SELECT count(*) FROM information_schema.TABLES '
        sql += f'WHERE (TABLE_SCHEMA = "{self.db}") AND (TABLE_NAME = "{table_name}")'
        cursor.execute(sql)
        table_exists = [item for item in cursor][0][0]
        if table_exists:
            logging.info("Table {} already exists--skipping creation step.".format(table_name))
        elif table_exists == 0:
            self.__create_table(cursor, table_name, dtypes, unique_key, foreign_key)
        else:
            print("There was a problem checking whether {} exists".format(table_name), end="")
            print("--unexpected table_exists value.")
        # TO DO
        # Check whether table looks like it has the right number of columns and column names

    def add_to_table(self, table_name, table_data, sql_col_names, file_name):
        cursor = self.connection.cursor()
        self.__use_db(cursor)
        self.__insert_records(cursor, table_name, table_data, sql_col_names, file_name)

    def __create_db(self, cursor):
        sql = 'CREATE DATABASE {}'.format(self.db)
        cursor.execute(sql)
        self.connection.commit()

    def __use_db(self, cursor):
        sql = 'USE {}'.format(self.db)
        cursor.execute(sql)
        self.connection.commit()

    def __create_table(self, cursor, table_name, dtypes, unique_key, foreign_key):
        logging.info('Creating table {}'.format(table_name))
        sql = "CREATE TABLE {} (".format(table_name)
        sql += "id INT NOT NULL AUTO_INCREMENT, "
        sql += "source_file VARCHAR(255), "
        for column_name, column_dtype in dtypes.items():
            sql += "{} {}, ".format(column_name, column_dtype)
        sql += "PRIMARY KEY (id)"
        if unique_key:
            sql += ", UNIQUE ("
            for key in unique_key:
                sql += key + ', '
            sql = sql[:-2]  # Chop off last ', '
            sql += ")"
        if foreign_key:
            for constraint in foreign_key:
                sql += ", FOREIGN KEY("
                sql += constraint[0]
                sql += ") REFERENCES "
                sql += constraint[1]
        sql += ')'          # ... and balance parentheses before sending.
        logging.info('Creating table {}:\n\t{}'.format(table_name, sql))
        try:
            cursor.execute(sql)
        except pymysql.err.ProgrammingError:
            print('Error creating table {}'.format(table_name))
            logging.info('Error creating table{}:\n\t{}'.format(table_name, sql))
        self.connection.commit()

    def __insert_records(self, cursor, table_name, table_data, sql_col_names, file_name):
        for i in range(len(table_data)):
            values_string = file_name + "', '"
            for item in table_data[i:i+1].values[0]:
                escaped_item = re.sub(r"(['\\])", r'\\\1', str(item))   # Escape textual backslashes and tick marks
                cleaned_item = re.sub(u"\uFFFD", "", escaped_item)      # Fix oddball <?> character
                values_string += cleaned_item.strip() + "', '"          # Strip of leading and trailing whitespace
            values_string = values_string[:-4]                          # Chop off extra "', '"
            sql = "INSERT INTO {} ({}) VALUES ('{}')".format(table_name, "source_file, " + ", ".join(sql_col_names),
                                                             values_string)
            sql = re.sub(r"'(NULL|nan|None)'", "NULL", sql)             # NULL should be sent in SQL w/o quote marks
                                                                        # nan and None should be stored as NULL
            # print('{} of {}: {}'.format(i+1,len(table_data), sql))
            logging.debug('{} of {}: {}'.format(i+1, len(table_data), sql))
            try:
                cursor.execute(sql)
            except (pymysql.err.ProgrammingError, pymysql.err.IntegrityError) as e:
                if not re.search(r'Duplicate entry', repr(e)):
                    logging.info('Error adding entry: \n\t{}'.format(e))
                    logging.info('\t{} of {}: {}'.format(i+1, len(table_data), sql))

        self.connection.commit()

        # -----------------TO DO-----------------------------------
        # Have it return something if the operation raises an error and move the file into a problem file folder.
