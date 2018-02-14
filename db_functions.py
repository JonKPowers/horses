import pymysql.cursors
import re
import logging


class DbHandler:
    def __init__(self, db='horses_test'):
        self.db = db
        self.mysql = None
        self.initialize_db()

    def initialize_db(self):
        """Checks to see if db exists. If not, creates it."""
        self.mysql = self.__connect()
        try:
            with self.mysql.cursor() as cursor:
                sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{}'".format(self.db)
                db_exists = cursor.execute(sql)
                if db_exists:
                    print("Database {} already exists--skipping create step".format(self.db))
                elif db_exists == 0:
                    self.__create_db(cursor)
                    print("Created new database {}".format(self.db))
                else:
                    print("There was a problem checking whether {} exists".format(self.db), end="")
                    print("--unexpected db_exists value.")
        finally:
            self.mysql.close()

    def initialize_table(self, table_name, dtypes, unique_key, foreign_key):
        """Checks to see if a table exists. If not, creates it."""
        self.mysql = self.__connect()
        try:
            with self.mysql.cursor() as cursor:
                self.__use_db(cursor)
                sql = "SELECT count(*) FROM information_schema.TABLES "
                sql += "WHERE (TABLE_SCHEMA = '{}') AND (TABLE_NAME = '{}')".format(self.db, table_name)
                cursor.execute(sql)
                table_exists = [item for item in cursor][0][0]

                if table_exists:
                    logging.info("Table {} already exists--skipping creation step.".format(table_name))
                elif table_exists is None:
                    print("There was an error determining if table {} exists".format(table_name), end="")
                    print("table_exists still at default value--skipping creation step.")
                elif table_exists == 0:
                    self.__create_table(cursor, table_name, dtypes, unique_key, foreign_key)
                else:
                    print("There was a problem checking whether {} exists".format(table_name), end="")
                    print("--unexpected table_exists value.")
        finally:
            self.mysql.close()
        # TO DO
        # Check whether table looks like it has the right number of columns and column names

    def add_to_table(self, table_name, table_data, sql_col_names, file_name):
        self.mysql = self.__connect()
        try:
            with self.mysql.cursor() as cursor:
                self.__use_db(cursor)
                self.__insert_records(cursor, table_name, table_data, sql_col_names, file_name)
        finally:
            self.mysql.close()
        # ---------------TO DO---------------------------
        #   Run some checks to see if the data looks like the right shape, etc.

    # Hidden methods ------------------------

    def __connect(self):
        return pymysql.connect(
            host='localhost',
            user='codelou',
            password='ABCabc123!'
        )

    def __create_db(self, cursor):
        sql = 'CREATE DATABASE {}'.format(self.db)
        cursor.execute(sql)
        self.mysql.commit()

    def __use_db(self, cursor):
        sql = 'USE {}'.format(self.db)
        cursor.execute(sql)
        self.mysql.commit()

    def __create_table(self, cursor, table_name, dtypes, unique_key, foreign_key):
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
            sql += ", FOREIGN KEY("
            sql += list(foreign_key)[0]
            sql += ") REFERENCES "
            sql += list(foreign_key.values())[0]
        sql += ')'          # ... and balance parentheses before sending.
        print(sql)
        cursor.execute(sql)
        self.mysql.commit()
        # -----------------TO DO----------------------
        #   Need to add primary/unique key constraints.
        #   Maybe pull those 'extras' out from a separate function that
        #   returns the extra stuff based on the table_

    def __insert_records(self, cursor, table_name, table_data, sql_col_names, file_name):
        for i in range(len(table_data)):
            values_string = file_name + "', '"
            for item in table_data[i:i+1].values[0]:
                escaped_item = re.sub(r"(['\\])", r'\\\1', str(item))   # Escape textual backslashes and tick marks
                cleaned_item = re.sub(u"\uFFFD", "", escaped_item)      # Fix oddball <?> character
                values_string += cleaned_item + "', '"
            values_string = values_string[:-4]                          # Chop off extra "', '"
            sql = "INSERT INTO {} ({}) VALUES ('{}')".format(table_name, "source_file, " + ", ".join(sql_col_names),
                                                             values_string)
            sql = re.sub(r"'NULL'", "NULL", sql)                        # NULL should be sent in SQL w/o quote marks
            # print('{} of {}: {}'.format(i+1,len(table_data), sql))
            logging.debug('{} of {}: {}'.format(i+1, len(table_data), sql))
            try:
                cursor.execute(sql)
            except (pymysql.err.ProgrammingError, pymysql.err.IntegrityError) as e:
                logging.info('Error adding entry: \n\t{}'.format(e))
                logging.info('\t{} of {}: {}'.format(i+1, len(table_data), sql))

        self.mysql.commit()

        # -----------------TO DO-----------------------------------
        # Have it return something if the operation raises an error and move the file into a problem file folder.
