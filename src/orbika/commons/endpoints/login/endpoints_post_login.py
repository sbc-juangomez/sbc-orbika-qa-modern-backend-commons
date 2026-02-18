import logging

import requests

from src.orbika.commons.conf.login.conf_login import ConfLogin
from src.orbika.commons.endpoints.headers_validate.endpoints_headers_validate import EndpointsHeadersValidate
from src.orbika.commons.factories.factory_scenario import FactoryScenario
from src.orbika.commons.models.email.models_email_validate import ModelsEmailValidate
from src.orbika.commons.tasks.login.tasks_prepare_data_login import PrepareDataValidateLoginService
from src.orbika.commons.util.read_files.util_read_json import UtilReadJson
from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from src.orbika.commons.util.transversal_functions.util_data_generator import UtilDataGenerator

logger = logging.getLogger(__name__)


class PostLogin:
    def __init__(self):
        self.url = None
        self.service_name = None

    def login(self, scenario):

        self.service_name = self.extract_service_from_scenario(scenario)
        self.url = ConfLogin.get_url(self.service_name)
        logger.info(f"Servicio detectado: {self.service_name} | URL: {self.url}")
        logger.info(f"obtenido en endpoint scenario: {scenario}")

        try:
            prepare = PrepareDataValidateLoginService()
            if self.service_name == "sec-user-auth-mfa":
                logger.info("Preparando datos para sec-user-auth-mfa")
                headers, body = prepare.prepare_data_user_auth_mfa(scenario)
            elif self.service_name == "sec-associate-fotware-token":
                logger.info("Preparando datos para sec-associate-fotware-token")
                headers, body = prepare.prepare_data_associate_fotware_token(scenario)
            else:
                headers, body = prepare.prepare_data_validate_login_service(scenario)
            logger.info(f"obtenido en endpoint Body: {body}")
            logger.info(f"obtenido en endpoint Headers: {headers}")

            if "session_id" in headers and isinstance(headers, dict):
                logger.debug(f"se ha obtenido data con headers y body, session_id::: {headers['session_id']}")
                email_header = headers.get("email")
                session_id_header = headers.get("session_id")
                if session_id_header:
                    UtilRememberDataProcess().set_session_id_header(session_id_header)

                if 'session_id' in headers and headers['session_id'] is not None:
                    transaction_id = headers.get('transaction_id')
                    if transaction_id:
                        UtilRememberDataProcess().set_transaction_id(transaction_id)
            else:
                logger.debug(f"se ha obtenido data con headers y body, pero no se ha obtenido session_id")
                email_header = headers.get("email")
                session_id_header = {}

            UtilRememberDataProcess().set_body(body)
            logger.info(f"Este es el body en login:::: {body}")

            if email_header:
                UtilRememberDataProcess().set_email(email_header)
                logger.debug(f"Este es el email_header en login:::: {email_header}")
            else:
                UtilRememberDataProcess().set_email(False)
                logger.warning("El campo 'email' no está presente en el header.")

            if session_id_header:
                UtilRememberDataProcess().set_session_id(session_id_header)
                logger.debug(f"Este es el session_id_header en login:::: {session_id_header}")
            else:
                UtilRememberDataProcess().set_session_id(False)
                logger.warning("El campo 'session_id' no está presente en el header.")

            # Enviar el body tal como se generó por prepare_data_login
            response = requests.post(self.url, headers=headers, json=body)
            logger.info(f'Response Login: {response}')

            # Procesar y guardar la respuesta
            UtilRememberDataProcess().set_response_status_code(response.status_code)
            status = UtilRememberDataProcess().set_response_status_code
            logger.debug(f'Este es el status_code capturado en login:::: {status}')
            data_response = response.json()
            UtilRememberDataProcess().set_response(data_response)
            logger.info(f'Esto es el JSON de respuesta login::: {data_response}')
            if "success" in scenario:
                if self.service_name == "sec-validate-login-service":
                    if 'challenge_name' in data_response['result']['details']:
                        challenge_name = data_response['result']['details']['challenge_name']
                        logger.debug(f'Este es el challenge_name capturado en login:::: {challenge_name}')
                        UtilRememberDataProcess().set_challenge_name(challenge_name)
                    else:
                        challenge_name = ""
                    UtilRememberDataProcess().set_challenge_name(challenge_name)
                if self.service_name == "sec-user-auth-mfa":
                    if 'session' in data_response['result']['details']:
                        session_token = data_response['result']['details']['session']
                        logger.debug(f'Este es el session_token capturado en login:::: {session_token}')
                        UtilRememberDataProcess().set_session_token(session_token)
                    else:
                        session_token = ""
                    UtilRememberDataProcess().set_session_token(session_token)

            return data_response

        except Exception as e:
            logger.error(f'Error al procesar el login::: {e}')
            return None

    def login_emails_massive(self, scenario, json_name="test_cases_email.json"):
        self.service_name = self.extract_service_from_scenario(scenario)
        self.url = ConfLogin.get_url(self.service_name)
        logger.info(f"Servicio detectado: {self.service_name} | URL: {self.url}")

        try:
            prepare = PrepareDataValidateLoginService()
            if self.service_name == "sec-user-auth-mfa":
                logger.info("Preparando datos para sec-user-auth-mfa")
                headers, body = prepare.prepare_data_user_auth_mfa(scenario)
            elif self.service_name == "sec-associate-fotware-token":
                logger.info("Preparando datos para sec-associate-fotware-token")
                headers, body = prepare.prepare_data_associate_fotware_token(scenario)
            else:
                headers, body = prepare.prepare_data_validate_login_service(scenario)
            logger.info(f"obtenido en endpoint Body: {body}")
            logger.info(f"obtenido en endpoint Headers: {headers}")
            emails_cases = UtilReadJson.read_json_files(json_name)
            responses = []

            for email_case in emails_cases:
                email = email_case.get("email")
                expected = email_case.get("expected")
                if email is None or expected is None:
                    logger.warning(f"Caso inválido en el JSON: {email_case}")
                    continue

                transaction_id = headers['transaction_id'] = UtilDataGenerator.generate_uuid()
                session_id = headers['session_id'] = UtilDataGenerator.generate_uuid()
                headers['email'] = email
                try:

                    logger.debug(f'body MASIVE:: {body}')
                    logger.debug(f'headers MASIVE:: {headers}')
                    response = requests.post(self.url, headers=headers, json=body, timeout=10)
                    logger.debug(f'response MASIVE:: {response.json}')
                    data_response = response.json()
                    data_response_ints = ModelsEmailValidate(email, response.status_code, data_response, transaction_id,
                                                             session_id, expected)
                    responses.append(data_response_ints.get_response_data_email())
                except Exception as e:
                    logger.error(f"Error al realizar la solicitud POST para {email}: {e}")
                    responses.append(
                        ModelsEmailValidate.get_response_data_email_error(email, transaction_id, session_id, expected))
            return responses
        except Exception as e:
            logger.error(f'Error al consultar el progreso de la orden::: {e}')

    def login_headers_massive(self, scenario):
        self.service_name = self.extract_service_from_scenario(scenario)
        self.url = ConfLogin.get_url(self.service_name)
        request_massive_headers = EndpointsHeadersValidate()
        UtilRememberDataProcess.set_scenario(scenario)
        data = FactoryScenario.get_scenario_data(scenario)
        logger.debug(f"data scenario massivo:: {data}")
        headers = data.get("headers", {})
        body = data.get("body", {})
        params = data.get("params", {})
        responses = request_massive_headers.request_massive_headers(self.url, body, headers, params, 'POST', json_file="test_cases_headers_login.json")
        logger.info(responses)
        return responses

    @staticmethod
    def extract_service_from_scenario(scenario):

        mapping = {
            "validate_login": "sec-validate-login-service",
            "login_user": "sec-login-user-service",
            "user_auth_mfa": "sec-user-auth-mfa",
            "get_permissions": "sec-get-permissions",
            "associate_fotware_token": "sec-associate-fotware-token"
        }

        for key, service in mapping.items():
            if key in scenario:
                return service

        raise ValueError(f"No se pudo determinar el servicio a partir del escenario: {scenario}")
