import logging
import os

from src.orbika.commons.conf.aws.conf_data_connection_aws import ConfDataConnectionAws
from src.orbika.commons.util.aws.util_aws_functions import UtilAwsFunctions

logger = logging.getLogger(__name__)

ERROR_SCENARIO = 'No fue posible realizar las consultas de preparación del entorno de prueba.'


class FactConditionsTestsAws:
    def __init__(self):
        self.aws_functions = UtilAwsFunctions()
        self.get_dates_lambda = ConfDataConnectionAws().get_dates_params('lambda')

    def fact_create_user_cognito(self, password, email):
        if os.getenv('ENVIRONMENT') != 'mock':
            try:
                # Verificar si el usuario ya existe
                if self.aws_functions.check_cognito_user_exists(email):
                    # Eliminar al usuario si existe
                    logger.info(f"El usuario {email} ya existe. Procediendo a eliminarlo.")
                    self.aws_functions.delete_user_cognito(email)

                # Crear el usuario
                response = self.aws_functions.create_cognito_user(password, email)
                assert response is not None, ERROR_SCENARIO
                logger.info(f"Usuario creado correctamente: {email}")
            except Exception as e:
                logger.error(f"Error al preparar los datos {e}")
                assert False, ERROR_SCENARIO
