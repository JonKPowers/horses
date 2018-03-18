import logging
import pymysql
import re

logging.basicConfig(filename='db_handler.log', filemode='w', level=logging.DEBUG)

class SQLConnection:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user=self.user,
            password=self.password)

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


class QueryDB:
    def query_db(self, sql_query, return_col_names=False):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self._use_db(db, cursor)
            print('Sending SQL query')
            cursor.execute(sql_query)
            print('Processing response')
            results = list(cursor)
            results_cols = [item[0] for item in cursor.description]
        return (results, results_cols) if return_col_names else results

    def update_db(self, sql_query):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self._use_db(db, cursor)
            print('Sending SQL update query')
            logging.debug(sql_query)
            cursor.execute(sql_query)
            db.commit()
            print('Update query sent; change committed')

    def initialize_db(self):
        """Checks to see if db exists. If not, creates it."""
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            sql = f'SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = "{self.db}"'
            db_exists = cursor.execute(sql)
            if db_exists:
                print(f'Database {self.db} already exists--skipping create step')
            elif db_exists == 0:
                self._create_db(db, cursor)
                print(f'Created new database {self.db}')
            else:
                print(f'There was a problem checking whether {self.db} exists--unexpected db_exists value.')

    def add_to_table(self, table_name, table_data, sql_col_names):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self._use_db(db, cursor)
            self._insert_records(db, cursor, table_name, table_data, sql_col_names)

    def initialize_table(self, table_name, dtypes, unique_key, foreign_key):
        """Checks to see if a table exists. If not, creates it."""
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self._use_db(db, cursor)
            sql = 'SELECT count(*) FROM information_schema.TABLES '
            sql += f"WHERE (TABLE_SCHEMA = '{self.db}') AND (TABLE_NAME = '{table_name}')"
            cursor.execute(sql)
            table_exists = [item for item in cursor][0][0]
            if table_exists:
                logging.info(f'Table {table_name} already exists--skipping creation step.')
            elif table_exists == 0:
                self._create_table(db, cursor, table_name, dtypes, unique_key, foreign_key)
            else:
                print(f'There was a problem checking whether {table_name} exists--unexpected table_exists value.')

    def _create_db(self, db, cursor):
        cursor.execute(f'CREATE DATABASE {self.db}')
        db.commit()

    def _use_db(self, db, cursor):
        cursor.execute(f'USE {self.db}')
        db.commit()

    def _create_table(self, db, cursor, table_name, dtypes, unique_key, foreign_key):
        logging.info(f'Creating table {table_name}')
        sql = f'CREATE TABLE {table_name} ('
        sql += 'id INT NOT NULL AUTO_INCREMENT, '
        for column_name, column_dtype in dtypes.items():
            sql += f'{column_name} {column_dtype}, '
        sql += 'PRIMARY KEY (id)'
        if unique_key:
            sql += ', UNIQUE ('
            for key in unique_key:
                sql += key + ', '
            sql = sql[:-2]  # Chop off last ', '
            sql += ")"
        if foreign_key:
            for constraint in foreign_key:
                sql += f', FOREIGN KEY({constraint[0]}) REFERENCES {constraint[1]} '
        sql += ')'          # ... and balance parentheses before sending.
        logging.info(f'Creating table {table_name}:\n\t{sql}')
        try:
            cursor.execute(sql)
        except pymysql.err.ProgrammingError as e:
            print(f'Error creating table {table_name}:\n\t{sql}\n\t{e}')
            logging.info(f'Error creating table{table_name}:\n\t{sql}')
        db.commit()

    def _insert_records(self, db, cursor, table_name, table_data, sql_col_names):
        for i in range(len(table_data)):
            values_string = ''
            for item in table_data[i]:
                escaped_item = re.sub(r"(['\\])", r'\\\1', str(item))   # Escape textual backslashes and tick marks
                cleaned_item = re.sub(u"\uFFFD", "", escaped_item)      # Fix oddball <?> character
                values_string += cleaned_item.strip() + "', '"          # Strip off any leading or trailing whitespace
            values_string = values_string[:-4]                          # Chop off extra "', '"
            sql = f"INSERT INTO {table_name} ({', '.join(sql_col_names)}) VALUES ('{values_string}')"
            sql = re.sub(r"'(NULL|nan|None)'", "NULL", sql)             # NULL should be sent in SQL w/o quote marks
                                                                        # nan and None should be stored as NULL
            # print('{} of {}: {}'.format(i+1,len(table_data), sql))
            logging.debug(f'{i+1} of {len(table_data)}: {sql}')
            try:
                cursor.execute(sql)
            except (pymysql.err.ProgrammingError, pymysql.err.IntegrityError) as e:
                if not re.search(r'Duplicate entry', repr(e)):
                    logging.info(f'Error adding entry: \n\t{e}')
                    logging.info(f'\t{i+1} of {len(table_data)}: {sql}')
        db.commit()

    def __init__(self, db, username='codelou', password='ABCabc123!', initialize_db=False):
        self.db = db
        self.user = username
        self.password = password
        if initialize_db: self.initialize_db()

