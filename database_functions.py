import column_dtypes
import pymysql.cursors
import re


class DbHandler:
    def __init__(self, db='horses_test', name_files=None):
        self.db = db
        self.mysql = None
        self.column_dtypes = {
            '1': column_dtypes.col_1_dtypes,
            '2': column_dtypes.col_2_dtypes,
            '3': column_dtypes.col_3_dtypes,
            '4': column_dtypes.col_4_dtypes,
            '5': column_dtypes.col_5_dtypes,
            '6': column_dtypes.col_6_dtypes,
            'DRF': column_dtypes.past_performances_dtypes,
        }

    def initialize_db(self):
        """Checks to see if db exists. If not, creates it."""
        self.mysql = self.__connect()
        db_exists = None
        try:
            with self.mysql.cursor() as cursor:
                sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{}'".format(self.db)
                db_exists  = cursor.execute(sql)
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

    def initialize_table(self, table_name, extension):
        """Checks to see if a table exists. If not, creates it."""
        self.mysql = self.__connect()
        table_exists = None
        try:
            with self.mysql.cursor() as cursor:
                self.__use_db(cursor)
                sql = "SELECT count(*) FROM information_schema.TABLES "
                sql += "WHERE (TABLE_SCHEMA = '{}') AND (TABLE_NAME = '{}')".format(self.db, table_name)
                cursor.execute(sql)
                table_exists = [item for item in cursor][0][0]

                if table_exists:
                    print("Table {} already exists--skipping creation step.".format(table_name))
                elif table_exists == None:
                    print("There was an error determining if table {} exists".format(table_name), end="")
                    print("table_exists still at default value--skipping creation step.")
                elif table_exists == 0:
                    self.__create_table(cursor, table_name, extension)
                else:
                    print("There was a problem checking whether {} exists".format(table_name), end="")
                    print("--unexpected table_exists value.")
        finally:
            self.mysql.close()
        # TO DO
        # Check whether tabel looks like it has the right number of columns and column names


    def add_to_table(self, table_name, table_data, column_names):
        self.mysql = self.__connect()
        try:
            with self.mysql.cursor() as cursor:
                self.__use_db(cursor)
                self.__insert_records(cursor, table_name, table_data, column_names)
        finally:
            self.mysql.close()
        # ---------------TO DO---------------------------
        #   Run some checks to see if the data looks like the right shape, etc.
        #   Add some logging

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

    def __create_table(self, cursor, table_name, extension):
        data_type = None
        sql = "CREATE TABLE {} (".format(table_name)
        column_dtypes = self.column_dtypes[extension]
        for column_name, column_dtype in column_dtypes.items():
            sql += "{} {}, ".format(column_name, column_dtype)
        sql = sql[:-2]      # Chop off extra ', ' ...
        sql += ')'          # ... and balance parentheses before sending.
        print(sql)
        cursor.execute(sql)
        self.mysql.commit()
        # -----------------TO DO----------------------
        #   Need to add primary/unique key constraints.
        #   Maybe pull those 'extras' out from a separate function that
        #   returns the extra stuff based on the table_

    def __insert_records(self, cursor, table_name, table_data, column_names):
        table_values = table_data.values
        for i in range(len(table_data)):
            values_string = ""
            for item in table_values[i]:
                values_string += re.sub(r"'", "\\'", str(item)) + "', '"
            values_string = values_string[:-4]  # Chop off extra "', '"
            sql = "INSERT INTO {} ({}) VALUES ('{}')".format(table_name, ", ".join(column_names), values_string)
            sql = re.sub(r"'NULL'", "NULL", sql)  # NULL should be sent in SQL w/o quote marks
            print(i+1, "of", len(table_data), ":", sql)
            cursor.execute(sql)
        self.mysql.commit()
