from config.db.connection_manager import Connection
from common.utils.db_utils import DbUtils


class ConfigSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_data(self):
        connection = Connection()
        self.set_connection(connection)
        self.set_db_utils(DbUtils(connection))

    def set_connection(self, value: Connection):
        self.connection = value

    def set_db_utils(self, dbUtils: DbUtils):
        self.dbUtils = dbUtils
