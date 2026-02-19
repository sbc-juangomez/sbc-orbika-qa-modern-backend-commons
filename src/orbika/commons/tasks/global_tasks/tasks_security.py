import logging
import os

from orbika.commons.factories.factory_scenario import FactoryScenario
from orbika.commons.util.database.util_database_functions import UtilDatabaseFunctions

logger = logging.getLogger(__name__)


class TasksSecurity:

    @staticmethod
    def get_user_id(email):
        database = UtilDatabaseFunctions()
        result = database.get_user_database(email)
        logger.debug(f"El user_id retornado desde la tarea es ::{result[0]}")
        return result[0]

    @staticmethod
    def get_user_id_from_scenario(scenario):
        try:
            if os.environ['ENVIRONMENT'] == 'mock':
                return 1
            database = UtilDatabaseFunctions()
            data = FactoryScenario.get_scenario_data(scenario)
            headers = data.get("headers", {})
            email = headers['email']
            result = database.get_user_database(email)
            logger.debug(f"El user_id retornado desde la tarea es ::{result[0]}")
            return str(result[0])
        except Exception as e:
            logger.debug(f'No se encontro el usuario. {e}')
            return None

    @staticmethod
    def get_email_from_scenario(scenario):
        try:
            data = FactoryScenario.get_scenario_data(scenario)
            input_data = data.get("input", {})
            email = input_data.get('email')

            logger.debug(f"El email retornado desde la tarea es ::{email}")
            return email
        except Exception as e:
            logger.debug(f'No se encontró el usuario. {e}')
            return None

    @staticmethod
    def get_user_id_from_scenario_no_bd(scenario):
        try:
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"DATA del escenario :::: {data}")
            headers = data.get("headers", {})
            logger.info(f"HEADERS del escenario :::: {headers}")
            user_id = headers['user_id']
            logger.info(f"USER_ID del escenario :::: {user_id}")
            logger.debug(f"El user_id retornado desde la tarea es ::{user_id}")
            return user_id
        except Exception as e:
            logger.debug(f'No se encontró el usuario. {e}')
            return None

    @staticmethod
    def get_service_order_id_from_scenario_no_bd(scenario):
        try:
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"DATA del escenario :::: {data}")
            params = data.get("params", {})
            logger.info(f"PARAMS del escenario :::: {params}")
            service_order_id = params['service_order_id']
            logger.debug(f"El service_order_id retornado desde la tarea es ::{service_order_id}")
            return service_order_id
        except Exception as e:
            logger.debug(f'No se encontró el usuario. {e}')
            return None

    @staticmethod
    def get_insurer_id_from_scenario_no_bd(scenario):
        try:
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"DATA del escenario :::: {data}")
            params = data.get("params", {})
            logger.info(f"PARAMS del escenario :::: {params}")
            insurer_id = params['insurer_id']
            logger.debug(f"El insurer_id retornado desde la tarea es ::{insurer_id}")
            return insurer_id
        except Exception as e:
            logger.debug(f'No se encontró el insurer_id. {e}')
            return None

    @staticmethod
    def get_flow_id_from_scenario_no_bd(scenario):
        try:
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"DATA del escenario :::: {data}")
            params = data.get("params", {})
            logger.info(f"PARAMS del escenario :::: {params}")
            flow_id = params['flow_id']
            logger.debug(f"El flow_id retornado desde la tarea es ::{flow_id}")
            return flow_id
        except Exception as e:
            logger.debug(f'No se encontró el flow_id. {e}')
            return None

    @staticmethod
    def get_status_id_from_scenario_no_bd(scenario):
        try:
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"DATA del escenario :::: {data}")
            params = data.get("params", {})
            logger.info(f"PARAMS del escenario :::: {params}")
            service_order_status_id = params['service_order_status_id']
            logger.debug(f"El service_order_status_id retornado desde la tarea es ::{service_order_status_id}")
            return service_order_status_id
        except Exception as e:
            logger.debug(f'No se encontró el service_order_status_id. {e}')
            return None
