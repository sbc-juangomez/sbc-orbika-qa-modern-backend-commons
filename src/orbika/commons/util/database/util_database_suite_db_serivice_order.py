import logging

from orbika.commons.util.database.util_connections_database import UtilConnectionsDatabase

logger = logging.getLogger(__name__)


class UtilDatabaseSuiteDBServiceOrder:
    def __init__(self):
        self.db_connection = UtilConnectionsDatabase()
        self.connection = self.db_connection.create_connection('suite-db')
