import logging

from orbika.commons.util.database.util_connections_database import UtilConnectionsDatabase

logger = logging.getLogger(__name__)

class UtilDatabaseFunctionsSecurity:
    def __init__(self):
        self.db_connection = UtilConnectionsDatabase()
        self.connection = self.db_connection.create_connection('orbika-db')

    def get_role_id_by_name(self, role_name):
        try:
            cursor = self.connection.cursor()
            query = """SELECT r.id 
                       FROM "security".roles r
                       WHERE r.name ILIKE %s AND r.status = TRUE
                       LIMIT 1"""
            cursor.execute(query, (f"%{role_name}%",))
            result = cursor.fetchone()
            cursor.close()

            if result:
                role_id = result[0]
                logger.info(f"Rol ID encontrado {role_id} para el nombre de rol {role_name}")
                return role_id
            else:
                logger.info(f"No se encontró ID para el nombre de rol {role_name}")
                return None
        except Exception as e:
            logger.error(f"Error al consultar el ID de rol para el nombre {role_name} en la base de datos: {e}")
            return None
