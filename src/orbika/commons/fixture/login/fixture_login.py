import logging
import os

from orbika.commons.endpoints.login.endpoints_post_login import PostLogin
from orbika.commons.util.aws.util_aws_functions import UtilAwsFunctions
from orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess

logger = logging.getLogger(__name__)


class FixtureLogin:

    @staticmethod
    def get_access_token(conf_mfa=False):
        UtilAwsFunctions().conf_mfa_client_cognito(conf_mfa)
        if os.environ['ENVIRONMENT'] == 'mock':
            return 'mock_data'
        logger.info(f"Variable de entorno FUNCTIONALITY ::{os.getenv('FUNCTIONALITY')}")
        functionality = os.getenv('FUNCTIONALITY')
        os.environ['FUNCTIONALITY'] = 'login'
        logger.info("Variable de entorno FUNCTIONALITY cambiada temporalmente a 'login'")

        login = PostLogin()

        if conf_mfa is False:
            result = login.login('data_sec_validate_login_service_12020_session_success')
            logger.info(f"Este es el result de login fixture :: {result}")
            access_token = result['result']['details']['access_token']
            logger.info(f"Este es el session :: {access_token}")
            if functionality is not None:
                os.environ['FUNCTIONALITY'] = functionality
                logger.info(f"Variable de entorno FUNCTIONALITY restaurada a {functionality}")
            return access_token
        else:
            result = login.login('data_sec_validate_login_service_12020_session_success_software')
            logger.info(f"Este es el result de login fixture :: {result}")
            session_token= result['result']['details']['session']
            logger.info(f"Este es el session_id :: {session_token}")
            UtilRememberDataProcess().set_session_token(session_token)
            if functionality is not None:
                os.environ['FUNCTIONALITY'] = functionality
                logger.info(f"Variable de entorno FUNCTIONALITY restaurada a {functionality}")
            return session_token

    @staticmethod
    def get_session_token_mfa():
        """
        Obtiene el session_token ejecutando el escenario MFA (test_12020_session_success_mfa).
        """
        UtilAwsFunctions().conf_mfa_client_cognito(True)
        if os.environ['ENVIRONMENT'] == 'mock':
            return 'mock_data'
        logger.info(f"Variable de entorno FUNCTIONALITY ::{os.getenv('FUNCTIONALITY')}")
        functionality = os.getenv('FUNCTIONALITY')
        os.environ['FUNCTIONALITY'] = 'login'
        logger.info("Variable de entorno FUNCTIONALITY cambiada temporalmente a 'login'")

        login = PostLogin()
        result = login.login('data_sec_validate_login_service_12020_session_success_mfa')
        logger.info(f"Este es el result de login fixture MFA :: {result}")
        session_token = result['result']['details']['session']
        logger.info(f"Este es el session_token MFA :: {session_token}")
        UtilRememberDataProcess().set_session_token(session_token)
        if functionality is not None:
            os.environ['FUNCTIONALITY'] = functionality
            logger.info(f"Variable de entorno FUNCTIONALITY restaurada a {functionality}")
        return session_token