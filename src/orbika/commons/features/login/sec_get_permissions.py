import logging

import allure
import pytest

from src.orbika.commons.endpoints.login.endpoints_post_login import PostLogin
from src.orbika.commons.exceptions.response_validator.exceptions_response_validator import ExceptionsResponseValidator
from src.orbika.commons.util.aws.util_aws_functions import UtilAwsFunctions
from src.orbika.commons.util.database.util_database_suite_db import UtilDatabaseSuiteDB
from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from src.orbika.commons.util.tracking.util_verify_register_event import UtilVerifyRegisterEvent

ERROR_DYNAMO = 'La validación de datos entre DynamoDB y el body falló.'
EXPECTED_ORIGIN = "sec-get-permissions"
ERROR_DESCRIPTION = "Ha ocurrido un error en el proceso de autenticación. ¡Comunícate con servicio al cliente Subocol!"
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
def delete_remember_data_process():
    UtilRememberDataProcess().reset_email_header()
    functions_aws = UtilAwsFunctions()
    functions_aws.conf_mfa_client_cognito(enabled=False)


@pytest.mark.test_12084_sec_get_permissions_user_not_clients
@pytest.mark.sec_get_permissions
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=41)
@allure.feature('test_12084_sec_get_permissions_user_not_clients')
def test_12084_sec_get_permissions_user_not_clients():
    with allure.step(
            "1. Validación de invalid_credentials_user en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_get_permissions_12084_sec_get_permissions_user_not_clients')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12084, 422, status_code, ERROR_DESCRIPTION, "El usuario no tiene clientes asociados",
                                                          EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12087_sec_get_permissions_user_client_app_not_rol
@pytest.mark.sec_get_permissions
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=43)
@allure.feature('test_12087_sec_get_permissions_user_client_app_not_rol')
def test_12087_sec_get_permissions_user_client_app_not_rol():
    with allure.step(
            "1. Validación de invalid_credentials_user en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_get_permissions_12087_sec_get_permissions_user_client_app_not_rol')
        status_code = UtilRememberDataProcess().get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
        user_id = UtilDatabaseSuiteDB().get_user_id_by_email(UtilRememberDataProcess.get_email_header())
        client = UtilDatabaseSuiteDB().get_user_clients(user_id)
        logger.info(f"Clientes asociados al usuario:{client[0]['client_name']}")
    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12086, 422, status_code,
                                                          ERROR_DESCRIPTION,
                                                          f"No se encontró roles o aplicaciones asociadas al usuario para el cliente {client[0]['client_name']}",
                                                          EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12090_sec_get_permissions_user_rol_without_permissions
@pytest.mark.sec_get_permissions
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=44)
@allure.feature('test_12090_sec_get_permissions_user_rol_without_permissions')
def test_12090_sec_get_permissions_user_rol_without_permissions():
    with allure.step(
            "1. Validación de invalid_credentials_user en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_get_permissions_12090_sec_get_permissions_user_rol_without_permissions')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
        rol = UtilDatabaseSuiteDB().get_role_by_user_database()
    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12090, 422, status_code,
                                                          ERROR_DESCRIPTION,
                                                          f"El rol {rol} no tiene permisos asignados",
                                                          EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@allure.feature('test_12091_sec_get_permissions_user_rol_not_found')
def test_12091_sec_get_permissions_user_rol_not_found():
    with allure.step(
            "1. Validación de invalid_credentials_user en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        response = login.login('data_sec_get_permissions_12091_sec_get_permissions_user_rol_not_found')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12091, 422, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "No se encontró información del rol con id 1",
                                                          EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO
