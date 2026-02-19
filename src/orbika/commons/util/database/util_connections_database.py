import logging

import psycopg2
from psycopg2 import OperationalError

from orbika.commons.conf.database.conf_data_connection import ConfDataConnection

logger = logging.getLogger(__name__)


class UtilConnectionsDatabase:

    def __init__(self):
        self.connection = None

    def create_connection(self, database):
        data_connection = ConfDataConnection()
        params = data_connection.get_connection_params(database)
        if params is None:
            logger.error(f"{database} base de datos no encontrada")
            return None
        try:
            self.connection = psycopg2.connect(
                host=params["HOST"],
                port=params["PORT"],
                dbname=params["DATABASE"],
                user=params["USERNAME"],
                password=params["PASSWORD"]
            )
            logger.debug(f"Conexion correcta con: {database}")
            return self.connection
        except OperationalError as e:
            logger.error(f"Error conectando a la base de datos, {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
