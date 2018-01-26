import pymysql.cursors


class DbHandler:
    def __init__(self, db='horses_test', table=None, columns=None, **kwargs):
        self.db = db
        self.table = table
        self.columns = columns
        self.mysql = None
        pass

    # Hidden methods ------------------------

    def __connect(self):
        return pymysql.connect(
            host='localhost',
            user='codelou',
            password='ABCabc123!'
        )

    def __create_db(self, db_connection):
        sql = 'CREATE DATABASE {}'.format(self.db)
        db_connection.execute(sql)
        self.mysql.commit()

    def __use_db(self, db_connection):
        sql = 'USE {}'.format(self.db)
        db_connection.execute(sql)
        self.mysql.commit()

    def __create_table(self, db_connection):
        sql = "CREATE TABLE '{}' (".format(self.table)
        # CODE TO FIGURE OUT AND ENUMERATE COLUMNS AND TYPES
        # for i in range(len(self.columns)-1):
        #     column = self.columns[i]
        #     sql += "'{}' char(32), ".format(column)
        # sql += "'{}' char(32))".format(self.columns[-1])
        db_connection(sql)
        self.mysql.commit()

    def insert_record(self, db_connection):
        # CODE TO CYCLE THROUGH RECORDS TO INSERT
        # for mushroom in self.mushrooms:
        #     values = mushroom.harvest(self.columns)
        #     sql = "INSERT INTO {} ('{}') VALUE('{}')".format(
        #         self.table,
        #         "', '".join(self.columns),
        #         "', '".join(values)
        #     )
        #    db_connection.execute(sql)
        self.mysql.commit()
