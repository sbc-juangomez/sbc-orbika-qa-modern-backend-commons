import logging

import allure
import pytest

from orbika.commons.endpoints.login.endpoints_post_login import PostLogin
from orbika.commons.exceptions.response_validator.exceptions_response_validator import ExceptionsResponseValidator
from orbika.commons.util.aws.util_aws_functions import UtilAwsFunctions
from orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from orbika.commons.util.tracking.util_verify_register_event import UtilVerifyRegisterEvent

logger = logging.getLogger(__name__)

ERROR_DYNAMO = 'La validación de datos entre DynamoDB y el body falló.'
EXPECTED_ORIGIN = "sec-user-auth-mfa"
ERROR_DESCRIPTION = "Ha ocurrido un error al tratar de ingresar a Orbika, inténtalo nuevamente"

@pytest.fixture(scope="function", autouse=True)
def before_all(request):
    functions_aws = UtilAwsFunctions()
    functions_aws.conf_mfa_client_cognito()

@pytest.mark.test_12041_sec_login_user_service_invalid_credentials
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=33)
@allure.feature('test_12041_sec_login_user_service_invalid_credentials')
def test_12041_sec_login_user_service_invalid_credentials():
    with allure.step("1. Validación de invalid_credentials_user en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_login_user_service_12041_invalid_credentials')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12041, 401, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "Email o contraseña incorrecta. Por favor, verifica tus datos e inténtalo nuevamente.", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12043_sec_login_user_service_user_not_found
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=35)
@allure.feature('test_12043_sec_login_user_service_user_not_found')
def test_12043_sec_login_user_service_user_not_found():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_login_user_service_12043_user_not_found')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12043, 401, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El usuario no se encuentra registrado. Por favor, verifica tu email o regístrate.", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12044_sec_login_user_service_user_disabled
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=36)
@allure.feature('test_12044_sec_login_user_service_user_disabled')
def test_12044_sec_login_user_service_user_disabled():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_login_user_service_12044_user_disabled')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12044, 403, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "Tu cuenta se encuentra deshabilitada. Por favor, contacta al administrador.", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12045_sec_login_user_service_attempts_exceeded
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=37)
@allure.feature('test_12045_sec_login_user_service_attempts_exceeded')
def test_12045_sec_login_user_service_attempts_exceeded():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_login_user_service_12045_attempts_exceeded')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12045, 429, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "Has excedido el número máximo de intentos de inicio de sesión.", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12048_sec_login_user_service_password_temporal_expired
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=38)
@allure.feature('test_12048_sec_login_user_service_password_temporal_expired')
def test_12048_sec_login_user_service_password_temporal_expired():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_login_user_service_12048_password_temporal_expired')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12048, 403, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "Tu contraseña temporal ha expirado. Por favor, solicita una nueva contraseña.", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12051_sec_login_user_service_user_not_in_database
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=39)
@allure.feature('test_12051_sec_login_user_service_user_not_in_database')
def test_12051_sec_login_user_service_user_not_in_database():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_login_user_service_12051_user_not_in_database')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12051, 422, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "Error de autenticación. ¡Comunícate con servicio al cliente Subocol!", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12052_sec_login_user_service_user_inactive
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=40)
@allure.feature('test_12052_sec_login_user_service_user_inactive')
def test_12052_sec_login_user_service_user_inactive():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_login_user_service_12052_user_inactive')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12052, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "Error de autenticación. ¡Comunícate con servicio al cliente Subocol!", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12053_sec_login_user_service_cognito_id_mismatch
@pytest.mark.sec_login_user_service
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=41)
@allure.feature('test_12053_sec_login_user_service_cognito_id_mismatch')
def test_12053_sec_login_user_service_cognito_id_mismatch():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):

        login = PostLogin()
        response = login.login('data_sec_login_user_service_12053_cognito_id_mismatch')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12053, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "Error de autenticación. ¡Comunícate con servicio al cliente Subocol!", "sec-login-user-service")

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
       assert validation_result, ERROR_DYNAMO