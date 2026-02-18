import logging

import allure
import pytest

from src.orbika.commons.endpoints.login.endpoints_post_login import PostLogin
from src.orbika.commons.exceptions.headers.exceptions_validate_headers_massive import ExceptionsValidateHeadersMassive
from src.orbika.commons.exceptions.login.exceptions_login import ExceptionsLogin
from src.orbika.commons.exceptions.response_validator.exceptions_response_validator import ExceptionsResponseValidator
from src.orbika.commons.fixture.login.fixture_login import FixtureLogin
from src.orbika.commons.util.aws.util_aws_functions import UtilAwsFunctions
from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from src.orbika.commons.util.tracking.util_verify_register_event import UtilVerifyRegisterEvent

ERROR_DYNAMO = 'La validación de datos entre DynamoDB y el body falló.'
EXPECTED_ORIGIN = "sec-associate-fotware-token"
ERROR_DESCRIPTION = "Ha ocurrido un error en el proceso de autenticación. ¡Comunícate con servicio al cliente Subocol!"


logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def before_test(request):
    functions_aws = UtilAwsFunctions()
    functions_aws.conf_mfa_client_cognito(True)

@pytest.fixture(scope="function")
def get_session_token_from_validate_login():
    """
    Fixture que obtiene el session_token del servicio sec-validate-login-service
    usando el escenario test_12020_session_success_mfa
    """
    session_token = FixtureLogin().get_session_token_mfa()
    logger.debug(f'Este es el session_token obtenido del fixture (MFA):::: {session_token}')
    return session_token

@pytest.mark.test_12120_session_token_success
@pytest.mark.sec_associate_fotware_token
@pytest.mark.all_login
@pytest.mark.run(order=1)
@allure.feature('test_12120_session_token_success')
def test_12120_session_token_success(before_test, get_session_token_from_validate_login):
    with allure.step("1. Validación de datos en el evento success del sec-associate-fotware-token"):
        login = PostLogin()
        response = login.login('data_sec_associate_fotware_token_12120_session_token_success')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12120, 200, status_code,
                                                          "Proceso ejecutado correctamente.", EXPECTED_ORIGIN)
    with allure.step("3. Validación de respuesta del servicio del item details"):
        ExceptionsLogin.validate_associate_fotware_token_success_response(response)
    with allure.step("4. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None, validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12121_session_token_not_exist
@pytest.mark.sec_associate_fotware_token
@pytest.mark.all_login
@pytest.mark.run(order=2)
@allure.feature('test_12121_session_token_not_exist')
def test_12121_session_token_not_exist():
    with allure.step("1. Validación de obligatoriedad del campo session_token en la solicitud del sec-associate-fotware-token"):
        login = PostLogin()
        response = login.login('data_sec_associate_fotware_token_12121_session_token_not_exist')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12121, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session_token es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None, validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12121_session_token_is_required
@pytest.mark.sec_associate_fotware_token
@pytest.mark.all_login
@pytest.mark.run(order=3)
@allure.feature('test_12121_session_token_is_required')
def test_12121_session_token_is_required():
    with allure.step("1. Validación de obligatoriedad del campo session_token en la solicitud del sec-associate-fotware-token"):
        login = PostLogin()
        response = login.login('data_sec_associate_fotware_token_12121_session_token_is_required')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12121, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session_token es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None, validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12121_session_token_is_empty
@pytest.mark.sec_associate_fotware_token
@pytest.mark.all_login
@pytest.mark.run(order=4)
@allure.feature('test_12121_session_token_is_empty')
def test_12121_session_token_is_empty():
    with allure.step("1. Validación de obligatoriedad del campo session_token en la solicitud del sec-associate-fotware-token"):
        login = PostLogin()
        response = login.login('data_sec_associate_fotware_token_12121_session_token_is_empty')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12121, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session_token es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None, validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12121_session_token_data_type_int
@pytest.mark.sec_associate_fotware_token
@pytest.mark.all_login
@pytest.mark.run(order=5)
@allure.feature('test_12121_session_token_data_type_int')
def test_12121_session_token_data_type_int():
    with allure.step("1. Validación de data_type_int del campo session_token en la solicitud del sec-associate-fotware-token"):
        login = PostLogin()
        response = login.login('data_sec_associate_fotware_token_12121_session_token_data_type_int')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12121, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session_token debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None, validate_new_fields=True)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12121_session_token_data_type_float
@pytest.mark.sec_associate_fotware_token
@pytest.mark.all_login
@pytest.mark.run(order=6)
@allure.feature('test_12121_session_token_data_type_float')
def test_12121_session_token_data_type_float():
    with allure.step("1. Validación de data_type_float del campo session_token en la solicitud del sec-associate-fotware-token"):
        login = PostLogin()
        response = login.login('data_sec_associate_fotware_token_12121_session_token_data_type_float')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12121, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session_token debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None, validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12121_headers_validate_massive
@pytest.mark.sec_associate_fotware_token
@pytest.mark.all_login
@pytest.mark.run(order=7)
@allure.feature('test_12121_headers_validate_massive')
def test_12121_headers_validate_massive():
    with allure.step("1. Se realiza la validación masiva de headers en el servicio que sec-associate-fotware-token consume"):
        login = PostLogin()
        responses = login.login_headers_massive('data_sec_associate_fotware_token_12121_headers_validate_massive')

    with allure.step("2. Se validan todas las respuestas de headers del servicio"):
        ExceptionsValidateHeadersMassive.validate_headers(ERROR_DESCRIPTION, EXPECTED_ORIGIN, 12121, responses)
        ExceptionsValidateHeadersMassive.validate_headers_massive_dynamo(responses)

