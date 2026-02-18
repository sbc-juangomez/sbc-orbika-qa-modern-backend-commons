import logging
import os

from src.orbika.commons.factories.factory_scenario import FactoryScenario
from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from src.orbika.commons.util.transversal_functions.util_data_generator import UtilDataGenerator

logger = logging.getLogger(__name__)
ENVIRONMENT = os.getenv('ENVIRONMENT')
MFA_SECRET_KEY = {"dev": "GYRKASU3KLD7G54OAINGHNTMWCIVM6MEWP3KFKQJCGJW2VLVLLIA",
                  "qa": "DPKJSUBP7XWFMXUTRB25NP73KLDJNJWOPLFXKNAG37QSB5C5SARQ"}


def prepare_headers(scenario):
    try:
        data = FactoryScenario.get_scenario_data(scenario)
        logger.debug(f"Datos originales del escenario desde prepare_data_header : {data}")

        # Obtener headers
        headers = data.get("headers", {})
        logger.debug(f"Headers obtenidos del escenario: {headers}")
        UtilRememberDataProcess.set_email_header(headers.get("email", ""))
        # Modificaciones a los headers
        if ENVIRONMENT != 'mock':
            if "session_id" in headers:
                headers['session_id'] = UtilDataGenerator.generate_uuid()
            if "transaction_id" in headers:
                headers['transaction_id'] = UtilDataGenerator.generate_uuid()

        logger.info(f"Estos son los headers a enviar :: {headers}")
        return headers

    except Exception as e:
        logger.error(f"Error al preparar los datos para validacion headers: {e}")
        return {}


class PrepareDataValidateLoginService:
    @staticmethod
    def prepare_data_validate_login_service(scenario):
        try:
            UtilRememberDataProcess.set_scenario(scenario)
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"Este es el json que recibe prepare_data_login desde get_scenario_data: {data}")

            headers = prepare_headers(scenario)
            body = data.get("body", {})

            if headers.get("transaction_id") is not None and headers.get("transaction_id") != '' and len(str(headers.get("transaction_id"))) == 36:
                transaction_id = headers.get("transaction_id")
            else:
                transaction_id = None
            logger.debug(f"transaction_id obtenido: {transaction_id}")
            UtilRememberDataProcess.set_email_header(headers.get("email"))

            if "session_id" in data and isinstance(data["headers"], dict):

                ## Condición para saltar el transaction_id y continuar con el obtenido.
                if ENVIRONMENT != 'mock':
                    # Condición para generar un nuevo transaction_id
                    if transaction_id is not None and transaction_id != '' and len(str(transaction_id)) == 36:
                        data["headers"]["transaction_id"] = UtilDataGenerator.generate_uuid()
                        logger.info(f"Se generó un nuevo transaction_id: {data['headers']['transaction_id']}")
                    else:
                        # Mantener el transaction_id como está
                        logger.info(f"El transaction_id recibido se mantiene sin cambios: {transaction_id}")
                else:
                    logger.info(f"Se mantiene el transaction_id en ambiente mock: {transaction_id}")

            return headers, body
        except Exception as e:
            logger.error(f"Error data login: {e}")
            return {}, {}

    @staticmethod
    def prepare_data_user_auth_mfa(scenario):
        try:
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"Este es el json que recibe prepare_data_user_auth_mfa desde get_scenario_data: {data}")
            headers = data.get("headers", {})
            body = data.get("body", {})
            email = headers.get("email")
            invalid_challenge = UtilRememberDataProcess().get_challenge_name()
            if invalid_challenge is not None:
                logger.debug(f"El challenge_name obtenido es: {invalid_challenge}")
                body["challenge_name"] = invalid_challenge
            if "success" in scenario:
                session = UtilRememberDataProcess().get_session_token()
                email = UtilRememberDataProcess().get_email()
                body["code"] = UtilDataGenerator.generate_code_mfa(MFA_SECRET_KEY[ENVIRONMENT])
                body["session"] = session
                headers["email"] = email
                logger.debug("Código MFA generado y agregado al body.")
            if headers.get("transaction_id") is not None and headers.get("transaction_id") != '' and len(str(headers.get("transaction_id"))) == 36:
                transaction_id = headers.get("transaction_id")
            if email is not None:
                UtilRememberDataProcess.set_email_header(email)
            else:
                transaction_id = None
            logger.debug(f"transaction_id obtenido: {transaction_id}")

            if ENVIRONMENT != 'mock':
                # Condición para generar un nuevo transaction_id
                if transaction_id is not None and transaction_id != '' and len(str(transaction_id)) == 36:
                    data["headers"]["transaction_id"] = UtilDataGenerator.generate_uuid()
                    logger.info(f"Se generó un nuevo transaction_id: {data['headers']['transaction_id']}")
                else:
                    # Mantener el transaction_id como está
                    logger.info(f"El transaction_id recibido se mantiene sin cambios: {transaction_id}")
            else:
                logger.info(f"Se mantiene el transaction_id en ambiente mock: {transaction_id}")
            logger.info(f"Estos son los headers a enviar :: {headers}")
            logger.info(f"Este es el body a enviar :: {body}")
            return headers, body
        except Exception as e:
            logger.error(f"Error data user auth mfa: {e}")
            return {}, {}

    @staticmethod
    def prepare_data_associate_fotware_token(scenario):
        try:
            UtilRememberDataProcess.set_scenario(scenario)
            data = FactoryScenario.get_scenario_data(scenario)
            logger.info(f"Este es el json que recibe prepare_data_associate_fotware_token desde get_scenario_data: {data}")
            headers = data.get("headers", {})
            body = data.get("body", {})
            email = headers.get("email")

            # Si es un caso exitoso, obtener el session_token del servicio sec-validate-login-service
            if "success" in scenario:
                session_token = UtilRememberDataProcess().get_session_token()
                if session_token:
                    body["session_token"] = session_token
                    logger.debug("Session token obtenido del servicio sec-validate-login-service y agregado al body.")
                else:
                    # Si no hay session_token guardado, usar el del body o la cadena por defecto
                    if "session_token" not in body or not body["session_token"]:
                        body["session_token"] = "eyJjdHkiOiJKV1QiL..."
                        logger.debug("Session token no disponible, usando valor por defecto.")

            if headers.get("transaction_id") is not None and headers.get("transaction_id") != '' and len(str(headers.get("transaction_id"))) == 36:
                transaction_id = headers.get("transaction_id")
            else:
                transaction_id = None

            if email is not None:
                UtilRememberDataProcess.set_email_header(email)

            logger.debug(f"transaction_id obtenido: {transaction_id}")

            if ENVIRONMENT != 'mock':
                # Condición para generar un nuevo transaction_id
                if transaction_id is not None and transaction_id != '' and len(str(transaction_id)) == 36:
                    headers["transaction_id"] = UtilDataGenerator.generate_uuid()
                    logger.info(f"Se generó un nuevo transaction_id: {headers['transaction_id']}")
                else:
                    # Mantener el transaction_id como está
                    logger.info(f"El transaction_id recibido se mantiene sin cambios: {transaction_id}")
            else:
                logger.info(f"Se mantiene el transaction_id en ambiente mock: {transaction_id}")

            # Preparar headers
            if ENVIRONMENT != 'mock':
                if "session_id" in headers:
                    headers['session_id'] = UtilDataGenerator.generate_uuid()
                if "transaction_id" not in headers or not headers.get("transaction_id"):
                    headers['transaction_id'] = UtilDataGenerator.generate_uuid()

            logger.info(f"Estos son los headers a enviar :: {headers}")
            logger.info(f"Este es el body a enviar :: {body}")
            return headers, body
        except Exception as e:
            logger.error(f"Error data associate fotware token: {e}")
            return {}, {}
