import logging

import allure
import pytest
from orbika.commons.fixture.login.fixture_login import FixtureLogin

from orbika.commons.endpoints.login.endpoints_post_login import PostLogin
from orbika.commons.exceptions.email.exceptions_validate_email_massive_dynamo import ValidateEmailMassiveDynamo
from orbika.commons.exceptions.headers.exceptions_validate_headers_massive import ExceptionsValidateHeadersMassive
from orbika.commons.exceptions.login.exceptions_login import ExceptionsLogin
from orbika.commons.exceptions.response_validator.exceptions_response_validator import ExceptionsResponseValidator
from orbika.commons.tasks.global_tasks.tasks_security import TasksSecurity
from orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from orbika.commons.util.tracking.util_verify_register_event import UtilVerifyRegisterEvent

ERROR_DYNAMO = 'La validación de datos entre DynamoDB y el body falló.'
EXPECTED_ORIGIN = "sec-user-auth-mfa"
ERROR_DESCRIPTION = "Ha ocurrido un error en el proceso de autenticación. ¡Comunícate con servicio al cliente Subocol!"
INVALID_CHALLENGE_NAME = "INVALID_CHALLENGE_NAME"
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
def delete_remember_data_process():
    UtilRememberDataProcess().reset_challenge_name()
    UtilRememberDataProcess().reset_email_header()
    UtilRememberDataProcess().reset_session_token()


@pytest.mark.test_12060_session_success
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=1)
@allure.feature('test_12060_session_success')
def test_12060_session_success():
    with allure.step("1. Validación de datos en el evento success MFA del login"):
        FixtureLogin().get_access_token()
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12060_session_success')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12060, 200, status_code,
                                                                                         "Proceso ejecutado correctamente", EXPECTED_ORIGIN)
    with allure.step("3. Validación de respuesta del servicio del item details"):
        ExceptionsLogin.auth_mfa_success_response(response)

    with allure.step("4. Validación con base de datos SUITE_DB del item details"):
        ExceptionsLogin.validate_permissions_against_db(response)

    with allure.step("5. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_session_is_required
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=2)
@allure.feature('test_12061_session_is_required')
def test_12061_session_is_required():
    with allure.step("1. Validación de obligatoriedad del campo session en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_session_is_required')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_session_not_exist
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=3)
@allure.feature('test_12061_session_not_exist')
def test_12061_session_not_exist():
    with allure.step("1. Validación de obligatoriedad del campo session en la solicitud del login"):
        user_id = TasksSecurity.get_user_id_from_scenario(
            'data_sec_user_auth_mfa_12061_session_not_exist')
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_session_not_exist')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_session_empty
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=4)
@allure.feature('test_12061_session_empty')
def test_12061_session_empty():
    with allure.step("1. Validación de obligatoriedad del campo session en la solicitud del login"):
        user_id = TasksSecurity.get_user_id_from_scenario(
            'data_sec_user_auth_mfa_12061_session_empty')
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_session_empty')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_session_data_type_int
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=6)
@allure.feature('test_12061_session_data_type_int')
def test_12061_session_data_type_int():
    with allure.step("1. Validación de data_type_int del campo session en la solicitud del login"):
        user_id = TasksSecurity.get_user_id_from_scenario(
            'data_sec_user_auth_mfa_12061_session_data_type_int')
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_session_data_type_int')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_session_data_type_float
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=7)
@allure.feature('test_12061_session_data_type_float')
def test_12061_session_data_type_float():
    with allure.step("1. Validación de data_type_float del campo session en la solicitud del login"):
        user_id = TasksSecurity.get_user_id_from_scenario(
            'data_sec_user_auth_mfa_12061_session_data_type_float')
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_session_data_type_float')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_session_min_value
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=8)
@allure.feature('test_12061_session_min_value')
def test_12061_session_min_value():
    with allure.step("1. Validación de min_value del campo session en la solicitud del login"):
        user_id = TasksSecurity.get_user_id_from_scenario(
            'data_sec_user_auth_mfa_12061_session_min_value')
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_session_min_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session no puede tener menos de 100 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_session_max_value
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=9)
@allure.feature('test_12061_session_max_value')
def test_12061_session_max_value():
    with allure.step("1. Validación de max_value del campo session en la solicitud del login"):
        user_id = TasksSecurity.get_user_id_from_scenario(
            'data_sec_user_auth_mfa_12061_session_max_value')
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_session_max_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo session no puede tener más de 1200 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_code_not_exist
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=12)
@allure.feature('test_12061_code_not_exist')
def test_12061_code_not_exist():
    with allure.step("1. Validación de obligatoriedad del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_code_not_exist')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo code es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_code_is_required
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=13)
@allure.feature('test_12061_code_is_required')
def test_12061_code_is_required():
    with allure.step("1. Validación de obligatoriedad del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_code_is_required')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo code es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_code_is_empty
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=14)
@allure.feature('test_12061_code_is_empty')
def test_12061_code_is_empty():
    with allure.step("1. Validación de obligatoriedad del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_code_is_empty')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo code es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_code_min_value
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=15)
@allure.feature('test_12061_code_min_value')
def test_12061_code_min_value():
    with allure.step("1. Validación de min_value del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_code_min_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo code no puede tener menos de 6 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_code_max_value
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=16)
@allure.feature('test_12061_code_max_value')
def test_12061_code_max_value():
    with allure.step("1. Validación de max_value del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_code_max_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo code no puede tener más de 6 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_code_data_type_int
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=17)
@allure.feature('test_12061_code_data_type_int')
def test_12061_code_data_type_int():
    with allure.step("1. Validación de data_type_int del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_code_data_type_int')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo code debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_code_data_type_float
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=18)
@allure.feature('test_12061_code_data_type_float')
def test_12061_code_data_type_float():
    with allure.step("1. Validación de data_type_float del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_code_data_type_float')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo code debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_name_not_exist
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=29)
@allure.feature('test_12061_challenge_name_not_exist')
def test_12061_challenge_name_not_exist():
    with allure.step("1. Validación de obligatoriedad del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_not_exist')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo challenge_name es obligatorio", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_is_required
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=30)
@allure.feature('test_12061_challenge_is_required')
def test_12061_challenge_is_required():
    with allure.step("1. Validación de obligatoriedad del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_is_required')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo challenge_name es obligatorio", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_is_empty
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=31)
@allure.feature('test_12061_challenge_name_is_empty')
def test_12061_challenge_is_empty():
    with allure.step("1. Validación de obligatoriedad del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_is_empty')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo challenge_name es obligatorio", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_invalid_value
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=32)
@allure.feature('test_12061_challenge_invalid_value')
def test_12061_challenge_invalid_value():
    with allure.step("1. Validación de valores permitidos del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        UtilRememberDataProcess.set_challenge_name(INVALID_CHALLENGE_NAME)
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_invalid_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12073, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          f"Tipo de reto MFA no soportado: {INVALID_CHALLENGE_NAME}", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_data_type_int
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=33)
@allure.feature('test_12061_challenge_data_type_int')
def test_12061_challenge_data_type_int():
    with allure.step("1. Validación de data_type_int del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_data_type_int')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo challenge_name debe ser de tipo str", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_data_type_float
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=34)
@allure.feature('test_12061_challenge_data_type_float')
def test_12061_challenge_data_type_float():
    with allure.step("1. Validación de data_type_float del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_data_type_float')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo challenge_name debe ser de tipo str", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_name_min_value
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=35)
@allure.feature('test_12061_challenge_name_min_value')
def test_12061_challenge_name_min_value():
    with allure.step("1. Validación de min_value del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_min_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo challenge_name no puede tener menos de 5 caracteres", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_challenge_name_max_value
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=36)
@allure.feature('test_12061_challenge_name_max_value')
def test_12061_challenge_name_max_value():
    with allure.step("1. Validación de max_value del campo challenge_name en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_user_auth_mfa_12061_challenge_name_max_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12061, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo challenge_name no puede tener más de 50 caracteres", EXPECTED_ORIGIN)
    with allure.step("3. Validar datos de tracking en DyanmoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_fail("EVENT_FAIL", None)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12061_all_headers_validate
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=30)
@allure.feature('test_12061_all_headers_validate')
def test_12061_all_headers_validate():
    with allure.step("1. Se realiza la validación de headers en el servicio que crs_update_progress_order consume"):
        login = PostLogin()
        responses = login.login_headers_massive('data_sec_user_auth_mfa_12061_all_headers_validate')

    with allure.step("2. Se validan todas las respuestas de headers del servicio"):
        ExceptionsValidateHeadersMassive.validate_headers(ERROR_DESCRIPTION, EXPECTED_ORIGIN, 12061, responses)
        ExceptionsValidateHeadersMassive.validate_headers_massive_dynamo(responses)


@pytest.mark.test_12021_email_validate_massive
@pytest.mark.sec_user_auth_mfa
@pytest.mark.all_login
@pytest.mark.run(order=17)
def test_12021_email_validate_massive():
    with allure.step("1. Se realiza la validación masiva de emails en DynamoDB del sec_validate_login_service"):
        FixtureLogin().get_access_token()
        login = PostLogin()
        responses = login.login_emails_massive('data_sec_user_auth_mfa_12060_session_success')

    with allure.step("2. Se validan todas las respuestas de emails en DynamoDB del servicio"):
        ValidateEmailMassiveDynamo.validate_event_dynamo_massive(responses)

