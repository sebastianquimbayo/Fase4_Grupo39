import mysql.connector
import sys
from config import config_variables as config

timeout = 10


sys.path.append("..")


class Connection:
    def __init__(self):
        self.connection = self.createConnection()

    def createConnection(self):
        return mysql.connector.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DATABASE_NAME,
            port=config.PORT,
        )

    def getConnection(self):
        if self.connection is None:
            self.connection = self.createConnection()
        # elif self.connection.is_connected():
        #     self.connection = self.createConnection()
        return self.connection
