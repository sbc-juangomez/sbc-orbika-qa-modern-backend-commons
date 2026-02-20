import logging
import os

import allure

from src.orbika.commons.exceptions.response_validator.exceptions_response_validator import ExceptionsResponseValidator
from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from src.orbika.commons.util.tracking.util_verify_register_event import UtilVerifyRegisterEvent

logger = logging.getLogger(__name__)


class ExceptionsValidateHeadersMassive:

    @staticmethod
    def validate_headers(expect_description, expect_origin, code_service_expect, responses, no_auth=False):
        errors = []
        assert len(responses) > 0, "No se encontraron respuestas para validar"
        logger.debug(f"estas son las respuestas a validar masivas ::: {responses}")
        for response in responses:
            logger.debug(f'Validate dataaaa::::: {response}')
            scenario = response['scenario']
            logger.debug(f'validando scenario:::{scenario}')
            response_service = response['response']
            status_code_expect = response['expects']['expect_status_code']
            status_code_service = response['status_code']
            details_expect = response['expects']['expect_details']
            if response['scenario'] != 'authorization_no_exist':
                if no_auth is True:
                    break
                result = ExceptionsResponseValidator.validate_error_fields_soft(response_service, code_service_expect, status_code_expect, status_code_service,
                                                                                expect_description, details_expect, expect_origin)
                logger.debug(f'errores del scenario::: {scenario} : {result}')
                if result:
                    errors += list(map(lambda x, s=scenario: {**x, "scenario": s}, result))
            else:
                if status_code_service != 401:
                    errors.append({'scenario': scenario, 'error': f"Se esperaba un código de estado 401, pero se obtuvo {status_code_service}"})
                if response_service['message'] != "Unauthorized":
                    errors.append({'scenario': scenario, 'error': "Se esperaba el mensaje : Unauthorized"})

        if errors:
            error_message = ExceptionsValidateHeadersMassive.group_errors(errors)
            allure.attach(error_message, name="Errores Consolidados", attachment_type=allure.attachment_type.TEXT)
            assert False, f"Se encontraron errores en la validación del servicio:\n{error_message}"

    @staticmethod
    def validate_headers_massive_dynamo(responses):
        if os.environ['ENVIRONMENT'] == 'mock':
            return True
        errors_dynamo = []
        scenarios_not_dynamo = ['transaction_id_no_exist', 'transaction_id_is_empty', 'transaction_id_is_required', 'transaction_id_uuid_validate',
                                'authorization_no_exist']
        for response in responses:
            UtilRememberDataProcess.set_insurer_id(response['insurer_id'])
            scenario = response['scenario']
            if scenario in scenarios_not_dynamo:
                continue
            transaction_id = response.get('transaction_id', False)
            session_id = response.get('session_id', False)
            email = response.get('email', {})
            UtilRememberDataProcess.set_session_id_header(session_id)
            UtilRememberDataProcess.set_session_id(session_id)
            UtilRememberDataProcess.set_email_header(email)
            data_response = response.get('response')
            UtilRememberDataProcess.set_response(data_response)
            register_dynamo = UtilVerifyRegisterEvent()
            diferencces = register_dynamo.validate_event_fail('EVENT_FAIL', transaction_id)
            if not diferencces:
                errors_dynamo.append({
                    'email': email,
                    'transaction_id': transaction_id,
                    'scenario': scenario
                })
        if errors_dynamo:
            error_message_dynamo = "\n".join(
                [f"Scenario: {error['scenario']} Correo: {error['email']} - transaction_id: {error['transaction_id']}" for error in errors_dynamo])
            allure.attach(error_message_dynamo, name="Errores Consolidados", attachment_type=allure.attachment_type.TEXT)
            logger.debug('despues del attach')
            assert False, f"Se encontraron errores en la validación Dynamo:\n{error_message_dynamo}"

    @staticmethod
    def group_errors(errors):
        grouped_errors = {}
        for error in errors:
            scenario = error["scenario"]
            grouped_errors.setdefault(scenario, []).append(error["error"])
        error_message = "\n".join([f"Escenario: {scenario} - Errores: {', '.join(error_list)}" for scenario, error_list in grouped_errors.items()])
        return error_message
