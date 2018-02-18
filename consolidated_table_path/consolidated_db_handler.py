import logging
import pymysql

logging.basicConfig(filename='main_py.log', filemode='w', level=logging.INFO)

class SQLConnection:
    def __init__ (self, user, password):
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = self.user,
            password = self.password
        )

        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

class dbHandler:
    def query_db(self, db, sql_query):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self._use_db(db, cursor)
            cursor.execute(sql_query)
            results = list(cursor)
            results_cols = [item[0] for item in cursor.description]
        return results, results_cols

    def create_database(self, database_name):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()

            # Check if database exists; if not, create it
            sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{}'".format(self.db)
            db_exists = cursor.execute(sql)
            if db_exists:
                return_value = 1
                print("Database {} already exists--skipping create step".format(self.db))
            elif db_exists == 0:
                cursor.execute('CREATE DATABASE {}'.format(self.db))
                db.commit()
                return_value = 1
                print("Created new database {}".format(self.db))
            else:
                return_value = 0
                print("There was a problem checking whether {} exists".format(self.db))

        return return_value

    def create_table(self, table_name, sql_cols, unique_keys, foreign_keys):
        with SQLConnection(self.user, self.password) as db:
            cursor = db.cursor()
            self._use_db(db, cursor)

            # Check if table exists; if not, call _create_table to initialize it.
            sql = "SELECT count(*) FROM information_schema.TABLES "
            sql += "WHERE (TABLE_SCHEMA = '{}') AND (TABLE_NAME = '{}')".format(self.db, table_name)
            cursor.execute(sql)
            table_exists = [item for item in cursor][0][0]

            if table_exists:
                return_value = 1
                logging.info("Table {} already exists--skipping creation step.".format(table_name))
            elif table_exists == 0:
                self._create_table(db, cursor, table_name, sql_cols, unique_keys, foreign_keys)
                return_value = 1
                logging.info('Table {} was created')
            else:
                return_value = 0
                logging.info("There was a problem checking whether {} exists".format(table_name))
                print("There was a problem checking whether {} exists".format(table_name))
        return return_value

    def _use_db(self, db, cursor):
        cursor.execute('USE {}'.format(self.db))
        db.commit()

    def _create_table(self, db, cursor, table_name, sql_cols, unique_keys, foreign_keys):
        logging.info('Creating table {}'.format(table_name))
        sql = "CREATE TABLE {} (".format(table_name)

        # Two mandatory fields hard-coded in
        sql += "id INT NOT NULL AUTO_INCREMENT, "
        sql += "source_file VARCHAR(255), "
        # Build up column list from input table structure
        for column_name, column_dtype in sql_cols.items():
            sql += "{} {}, ".format(column_name, column_dtype)
        sql += "PRIMARY KEY (id)"
        # Add unique and foreign key constraints if provided for in the table structure
        if unique_keys:
            sql += ", UNIQUE ("
            for key in unique_keys:
                sql += key + ', '
            sql = sql[:-2]  # Chop off last ', '
            sql += ")"
        if foreign_keys:
            for constraint in foreign_keys:
                sql += ", FOREIGN KEY("
                sql += constraint[0]
                sql += ") REFERENCES "
                sql += constraint[1]
        sql += ')'          # ... and balance parentheses before sending.

        # Send it to the database
        try:
            logging.info('Creating table {}:\n\t{}'.format(table_name, sql))
            cursor.execute(sql)
        except pymysql.err.ProgrammingError:
            print('Error creating table {}'.format(table_name))
            logging.info('Error creating table{}:\n\t{}'.format(table_name, sql))
        db.commit()

    def __init__(self, db, username='codelou', password='ABCabc123!'):
        self.db = db
        self.user = username
        self.password = password