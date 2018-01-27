import pymysql.cursors


class DbUpdater:
    def __init__(self, db='horses_test', name_files=None):
        self.db = db
        self.mysql = None

    def initialize_db(self):
        # Check to see if db exists. If not, create it.
        pass

    def initialize_table(self, table, table_type, table_data):
        # Check to see if table exists and whether it has the right columns
        # If the table exists, let us know. Otherwise, create the table
        # Figure out correct columns from table_type argument
        table_exists = None
        try:
            with self.mysql.cursor() as cursor:
                sql = "SELECT count(*) FROM information_schema.TABLES " \
                      "WHERE (TABLE_SCHEMA = '{}') AND (TABLE_NAME = '{}')".format(
                                                                            self.db, table
                                                                            )
                cursor.execute(sql)
                table_exists = [item for item in cursor][0][0]

                if table_exists:
                    print("Table {} already exists--skipping creation step.".format(table))
                elif table_exists is None:
                    print("There was an error determining if table {} exists--skipping creation step.".format(table))
                elif table_exists == 0:
                    self.__create_table(cursor, table, table_data)
                else:
                    print("There was a problem checking whether {} exists--table_exists still at default.".format(table))
        finally:
            self.mysql.close()


    def add_to_table(self, table, table_data):
        # Run some checks to see if data looks like the right shape.
        # Add each row of data to the table
        # Add some logging?
        columns = [key for key, value in table_data.dtypes.items()]
        try:
            with self.mysql.cursor() as cursor:
                self.__insert_records(cursor, table, table_data, columns)
        finally:
            self.mysql.close()

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

    def __create_table(self, cursor, table, table_data):
        data_type = None
        sql = "CREATE TABLE '{}' (".format(table)
        for key, value in table_data.dtypes.items():
            if value == 'object':
                data_type = 'VARCHAR(255)'
            elif value == 'int64':
                data_type = 'INT'
            elif value =='float64':
                data_type = 'FLOAT'
            else:
                print('Error determining datatype for key: {}, value: {}'.format(key, value))
            sql += "{} {}, ".format(key, data_type)
        sql = sql[:-2]      # Chop off extra ', ' ...
        sql += ')'          # ... and balance parentheses before sending.
        cursor.execute(sql)
        self.mysql.commit()
        #   Need to add primary/unique key constraints.
        #   Maybe pull those 'extras' out from a separate function that
        #   returns the extra stuff based on the table_

    def __insert_records(self, cursor, table, table_data, columns):
        table_values = table_data.values
        for i in range(len(columns)):
            values_string = ""
            for item in table_values[i]:
                values_string += str(item) + "', '"
            sql = "INSERT INTO {} ('{}') VALUES('{}')".format(
                                                        table,
                                                        ", ".join(columns),
                                                        values_string
                                                        )
            cursor.execut(sql)
        self.mysql.commit()
