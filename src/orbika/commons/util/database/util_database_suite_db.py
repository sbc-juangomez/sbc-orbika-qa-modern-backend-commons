import logging

import psycopg2
import psycopg2.extras

from src.orbika.commons.util.database.util_connections_database import UtilConnectionsDatabase
from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess

logger = logging.getLogger(__name__)


class UtilDatabaseSuiteDB:
    def __init__(self):
        self.db_connection = UtilConnectionsDatabase()
        self.connection = self.db_connection.create_connection('suite-db')

        # CLIENTES + APLICACIONES POR USUARIO

    def get_user_clients(self, user_id):
        """
        Devuelve todos los application_client de un usuario con nombre de client y application.
        """
        query = """
               SELECT 
                   uac.application_client_id,
                   uac.application_client_default,
                   ac.client_id,
                   c.name AS client_name,
                   app.id AS application_id,
                   app.name AS application_name
               FROM security.user_application_client uac
               JOIN configuration.application_client ac ON ac.id = uac.application_client_id
               JOIN configuration.application app ON app.id = ac.application_id
               JOIN configuration.client c ON c.id = ac.client_id
               WHERE uac.user_id = %s;
           """
        try:
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(query, (user_id,))
                rows = cur.fetchall()
                logger.info(f'Resultados de la base de datos clientes y aplicaciones usuario::: {rows}')
                return [dict(r) for r in rows]
        except Exception as e:
            logger.error(f"Error get_user_clients: {e}")
            return []

    def get_user_id_by_email(self, email):
        try:
            cursor = self.connection.cursor()
            query = """SELECT id FROM "security".users WHERE email = %s;"""
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                logger.info(f'User ID encontrado: {result[0]}')
                return result[0]
            logger.info(f'No se encontró User ID para el email proporcionado.')
            return None
        except Exception as e:
            logger.error(f'Error al consultar el user ID en la base de datos:: {e}')
        return None

    def get_role_by_user_database(self):
        try:
            email = UtilRememberDataProcess().get_email_header()
            cursor = self.connection.cursor()
            query = """SELECT r."name" FROM "security".user_roles ur
                    inner join "security".users su 
                    on su.id = ur.user_id 
                    inner join "security".roles r 
                    on r.id = ur.role_id 
                    where su.email = %s;"""
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            logger.info(f'Resultados de la base de datos::: {result}')
            cursor.close()
            if result:
                logger.info(f'Rol encontrado: {result[0]}')
                return result[0]
            logger.info(f'Resultados de la base de datos::: {result}')
            return None
        except Exception as e:
            logger.error(f'Error al consultar el usuario en la base de datos:: {e}')
        return None
