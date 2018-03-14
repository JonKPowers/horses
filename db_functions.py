import pymysql.cursors
import re
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


class DbHandler:
    def __init__(self, db='horses_test', username='codelou', password='ABCabc123!'):
        self.db = db
        self.user = username
        self.password = password
        self.initialize_db()

    def query_db(self, db, sql_query):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self.__use_db(db, cursor)
            cursor.execute(sql_query)
            results = list(cursor)
            results_cols = [item[0] for item in cursor.description]
        return results, results_cols

    def initialize_db(self):
        """Checks to see if db exists. If not, creates it."""
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{}'".format(self.db)
            db_exists = cursor.execute(sql)
            if db_exists:
                print("Database {} already exists--skipping create step".format(self.db))
            elif db_exists == 0:
                self.__create_db(db, cursor)
                print("Created new database {}".format(self.db))
            else:
                print("There was a problem checking whether {} exists".format(self.db), end="")
                print("--unexpected db_exists value.")

    def initialize_table(self, table_name, dtypes, unique_key, foreign_key):
        """Checks to see if a table exists. If not, creates it."""
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self.__use_db(db, cursor)
            sql = "SELECT count(*) FROM information_schema.TABLES "
            sql += "WHERE (TABLE_SCHEMA = '{}') AND (TABLE_NAME = '{}')".format(self.db, table_name)
            cursor.execute(sql)
            table_exists = [item for item in cursor][0][0]
            if table_exists:
                logging.info("Table {} already exists--skipping creation step.".format(table_name))
            elif table_exists == 0:
                self.__create_table(db, cursor, table_name, dtypes, unique_key, foreign_key)
            else:
                print("There was a problem checking whether {} exists".format(table_name), end="")
                print("--unexpected table_exists value.")
        # TO DO
        # Check whether table looks like it has the right number of columns and column names

    def add_to_table(self, table_name, table_data, sql_col_names, file_name):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self.__use_db(db, cursor)
            self.__insert_records(db, cursor, table_name, table_data, sql_col_names, file_name)

    def __create_db(self, db, cursor):
        sql = 'CREATE DATABASE {}'.format(self.db)
        cursor.execute(sql)
        db.commit()

    def __use_db(self, db, cursor):
        sql = 'USE {}'.format(self.db)
        cursor.execute(sql)
        db.commit()

    def __create_table(self, db, cursor, table_name, dtypes, unique_key, foreign_key):
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
        db.commit()

    def __insert_records(self, db, cursor, table_name, table_data, sql_col_names, file_name):
        for i in range(len(table_data)):
            values_string = file_name + "', '"
            for item in table_data[i:i+1].values[0]:
                escaped_item = re.sub(r"(['\\])", r'\\\1', str(item))   # Escape textual backslashes and tick marks
                cleaned_item = re.sub(u"\uFFFD", "", escaped_item)      # Fix oddball <?> character
                values_string += cleaned_item + "', '"
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

        db.commit()

        # -----------------TO DO-----------------------------------
        # Have it return something if the operation raises an error and move the file into a problem file folder.
