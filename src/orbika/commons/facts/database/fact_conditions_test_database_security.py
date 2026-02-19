import logging
import os

from orbika.commons.util.database.util_database_functions import UtilDatabaseFunctions
from orbika.commons.util.database.util_database_functions_security import UtilDatabaseFunctionsSecurity
from orbika.commons.util.database.util_database_suite_db_serivice_order import UtilDatabaseSuiteDBServiceOrder

logger = logging.getLogger(__name__)


class FactConditionsTestDatabaseSecurity:
    def __init__(self):
        self.database_functions = UtilDatabaseFunctions()
        self.database_suit_db = UtilDatabaseSuiteDBServiceOrder()
        self.database_functions_security = UtilDatabaseFunctionsSecurity()

    def fact_create_user_database_or_update(self, cognito_id, email, login="v2"):
        if os.getenv('ENVIRONMENT') != 'mock':
            data_user = self.database_functions.get_user_database(email)
            role_id = UtilDatabaseFunctionsSecurity().get_role_id_by_name("Analista aseguradora")
            if data_user is not None and len(data_user) > 0:
                self.database_functions.update_cognito_id_user_database(cognito_id, email)
                if login == "v1":
                    self.database_functions.associate_user_with_insurer(email)
                self.database_functions.associate_user_with_role(email, role_id, version=login)
                logger.info('El usuario ya existe en la base de datos y no se creara')
                return None
            self.database_functions.create_user_database(cognito_id, email)
            self.database_functions.associate_user_with_insurer(email)
            self.database_functions.associate_user_with_role(email, role_id, version=login)
            self.database_functions.associate_user_with_permission(email)
