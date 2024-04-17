from mysql.connector import Error

import pymysql
import sys
from config import config_variables as config

timeout = 10


sys.path.append("..")


class Connection:
    def __init__(self):
        self.connection = self.createConnection()

    def createConnection(self):
        return pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db=config.DATABASE_NAME,
            host=config.HOST,
            password=config.PASSWORD,
            read_timeout=timeout,
            port=int(config.PORT),
            user=config.USER,
            write_timeout=timeout,
        )

    def getConnection(self):
        if self.connection is None:
            self.connection = self.createConnection()
        # elif self.connection.is_connected():
        #     self.connection = self.createConnection()
        return self.connection
