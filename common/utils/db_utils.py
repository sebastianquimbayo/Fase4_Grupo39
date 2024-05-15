from mysql.connector import Error
from config.db.connection_manager import Connection



class DbUtils:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection
        pass

    def ejecutar_consulta(self, query, parameters=()):
        try:
            connection = self.connection.getConnection()
            cursor = connection.cursor()
            if connection.is_connected():
                cursor.execute(query, parameters)
                results = cursor.fetchall()
                # Obtener todos los resultados de la consulta
                connection.commit()
                return results
        except Error as e:
            print("Error al ejecutar la consulta en MySQL:", e)
        finally:
            if "cursor" in locals() and cursor is not None:
                cursor.close()

        return None
