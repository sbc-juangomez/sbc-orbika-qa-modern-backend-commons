import logging

import allure
import pytest

from orbika.commons.endpoints.login.endpoints_post_login import PostLogin
from orbika.commons.exceptions.email.exceptions_validate_email_massive_dynamo import ValidateEmailMassiveDynamo
from orbika.commons.exceptions.headers.exceptions_validate_headers_massive import ExceptionsValidateHeadersMassive
from orbika.commons.exceptions.login.exceptions_login import ExceptionsLogin
from orbika.commons.exceptions.response_validator.exceptions_response_validator import ExceptionsResponseValidator
from orbika.commons.facts.aws.fact_conditions_test_aws import FactConditionsTestsAws
from orbika.commons.facts.database.fact_conditions_test_database_security import FactConditionsTestDatabaseSecurity
from orbika.commons.util.aws.util_aws_functions import UtilAwsFunctions
from orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from orbika.commons.util.tracking.util_verify_register_event import UtilVerifyRegisterEvent

ERROR_DYNAMO = 'La validación de datos entre DynamoDB y el body falló.'
EXPECTED_ORIGIN = "sec-validate-login-service"
ERROR_DESCRIPTION = "Ha ocurrido un error al tratar de ingresar a Orbika, inténtalo nuevamente"


logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def before_test(request):
    active_param = getattr(request, "param", True)
    functions_aws = UtilAwsFunctions()
    functions_aws.conf_mfa_client_cognito(active_param)

@pytest.mark.test_12020_session_success_mfa
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=1)
@allure.feature('test_12020_session_success_mfa')
def test_12020_session_success_mfa(before_test):
    with allure.step("1. Validación de datos en el evento success MFA del login"):
        functions_aws = UtilAwsFunctions()
        functions_aws.conf_mfa_client_cognito()
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12020_session_success_mfa')
        status_code = UtilRememberDataProcess.get_response_status_code()
        challenge_name = UtilRememberDataProcess.get_challenge_name()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
        logger.debug(f'Este es el challenge_name capturado en feature:::: {challenge_name}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsLogin.validate_login_success_response(response, "MFA_SETUP")
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200, status_code,
                                                          "Proceso ejecutado correctamente", EXPECTED_ORIGIN)
    with allure.step("2. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None,validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12020_session_success_software
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=2)
@allure.feature('test_12020_session_success_software')
def test_12020_session_success_software(before_test):
    with allure.step("1. Validación de datos en el evento success SOFTWARE del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12020_session_success_software')
        status_code = UtilRememberDataProcess.get_response_status_code()
        challenge_name = UtilRememberDataProcess.get_challenge_name()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
        logger.debug(f'Este es el challenge_name capturado en feature:::: {challenge_name}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200, status_code,
                                                          "Proceso ejecutado correctamente", EXPECTED_ORIGIN)
        ExceptionsLogin.validate_login_success_response(response, "SOFTWARE_TOKEN_MFA")
    with allure.step("2. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None,validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12020_sec_validate_login_service_password_change_required
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=34)
@allure.feature('test_12020_sec_validate_login_service_password_change_required')
def test_12042_sec_validate_login_service_password_change_required():
    with allure.step("1. Validación de password_change_required en la solicitud de sec_login_user_service del login"):
        login = PostLogin()
        fact_aws = FactConditionsTestsAws()
        fact_aws.fact_create_user_cognito('56d7ba53d789598766dd3e768c1fb25a525fc0b9', 'pruebascrearusuario@test.com')
        fact_database = FactConditionsTestDatabaseSecurity()
        fact_database.fact_create_user_database_or_update(UtilRememberDataProcess.get_cognito_id_user(),
                                                          'pruebascrearusuario@test.com',login="v2")
        response = login.login('data_sec_validate_login_service_12020_password_change_required_success')
        status_code = UtilRememberDataProcess().get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200, status_code,
                                                                                         "Proceso ejecutado correctamente",
                                                                                         EXPECTED_ORIGIN)
        ExceptionsLogin.validate_login_success_response(response, "NEW_PASSWORD_REQUIRED")


    with allure.step("2. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None, validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12020_session_success
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=3)
@allure.feature('test_12020_session_success')
@pytest.mark.parametrize("before_test", [False], indirect=True)
def test_12020_session_success(before_test):
    with allure.step("1. Validación de datos en el evento success sin servicio del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12020_session_success')
        status_code = UtilRememberDataProcess.get_response_status_code()
        challenge_name = UtilRememberDataProcess.get_challenge_name()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')
        logger.debug(f'Este es el challenge_name capturado en feature:::: {challenge_name}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsLogin.validate_login_success_response(response, '')
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200, status_code,
                                                          "Proceso ejecutado correctamente", EXPECTED_ORIGIN)
        ExceptionsLogin.validate_permissions_against_db(response)
    with allure.step("2. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None,validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO



@pytest.mark.test_12021_password_not_exist
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=4)
@allure.feature('test_12021_password_not_exist')
def test_12021_password_not_exist():
    with allure.step("1. Validación de obligatoriedad del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_password_not_exist')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo password es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12021_password_is_required
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=5)
@allure.feature('test_12021_password_is_required')
def test_12021_password_is_required():
    with allure.step("1. Validación de obligatoriedad del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_password_is_required')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo password es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12021_password_is_empty
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=6)
@allure.feature('test_12021_password_is_empty')
def test_12021_password_is_empty():
    with allure.step("1. Validación de obligatoriedad del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_password_is_empty')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo password es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_password_min_value
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=7)
@allure.feature('test_12021_password_min_value')
def test_12021_password_min_value():
    with allure.step("1. Validación de min_value del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_password_min_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo password no puede tener menos de 8 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_password_max_value
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=8)
@allure.feature('test_12021_password_max_value')
def test_12021_password_max_value():
    with allure.step("1. Validación de max_value del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_password_max_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo password no puede tener más de 40 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12021_password_data_type_int
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=9)
@allure.feature('test_12021_password_data_type_int')
def test_12021_password_data_type_int():
    with allure.step("1. Validación de data_type_int del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_password_data_type_int')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo password debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)
       assert validation_result, ERROR_DYNAMO

@pytest.mark.test_12021_password_data_type_float
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=10)
@allure.feature('test_12021_password_data_type_float')
def test_12021_password_data_type_float():
    with allure.step("1. Validación de data_type_float del campo password en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_password_data_type_float')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo password debe ser de tipo str", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_token_recaptcha_not_exist
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=11)
@allure.feature('test_12021_token_recaptcha_not_exist')
def test_12021_token_recaptcha_not_exist():
    with allure.step("1. Validación de obligatoriedad del campo token_recaptcha en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_token_recaptcha_not_exist')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo token_recaptcha es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_token_recaptcha_is_required
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=12)
@allure.feature('test_12021_token_recaptcha_is_required')
def test_12021_token_recaptcha_is_required():
    with allure.step("1. Validación de obligatoriedad del campo token_recaptcha en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_token_recaptcha_is_required')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo token_recaptcha es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_token_recaptcha_is_empty
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=13)
@allure.feature('test_12021_token_recaptcha_is_empty')
def test_12021_token_recaptcha_is_empty():
    with allure.step("1. Validación de obligatoriedad del campo token_recaptcha en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_token_recaptcha_is_empty')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo token_recaptcha es obligatorio", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_token_recaptcha_min_value
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=14)
@allure.feature('test_12021_token_recaptcha_min_value')
def test_12021_token_recaptcha_min_value():
    with allure.step("1. Validación de min_value del campo token_recaptcha en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_token_recaptcha_min_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo token_recaptcha no puede tener menos de 10 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_token_recaptcha_max_value
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=15)
@allure.feature('test_12021_token_recaptcha_max_value')
def test_12021_token_recaptcha_max_value():
    with allure.step("1. Validación de max_value del campo token_recaptcha en la solicitud del login"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12021_token_recaptcha_max_value')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_error_fields(response, 12021, 400, status_code,
                                                          ERROR_DESCRIPTION,
                                                          "El campo token_recaptcha no puede tener más de 5000 caracteres", EXPECTED_ORIGIN)

    with allure.step("3. Validar datos de tracking en DyanmoDB"):
       verifier = UtilVerifyRegisterEvent()
       validation_result = verifier.validate_event_fail("EVENT_FAIL", None,validate_new_fields=True)

       assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12021_headers_validate_massive
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=16)
@allure.feature('test_12021_headers_validate_massive')
def test_12021_headers_validate_massive():
    with allure.step("1. Se realiza la validación masiva de headers en el servicio que sec_validate_login_service consume"):
        login = PostLogin()
        responses = login.login_headers_massive('data_sec_validate_login_service_12021_headers_validate_massive')

    with allure.step("2. Se validan todas las respuestas de headers del servicio"):
        ExceptionsValidateHeadersMassive.validate_headers(ERROR_DESCRIPTION, EXPECTED_ORIGIN, 12021, responses)
        ExceptionsValidateHeadersMassive.validate_headers_massive_dynamo(responses)

@pytest.mark.test_12021_email_validate_massive
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=17)
def test_12021_email_validate_massive():
    with allure.step("1. Se realiza la validación masiva de emails en DynamoDB del sec_validate_login_service"):
        login = PostLogin()
        responses = login.login_emails_massive('data_sec_validate_login_service_12021_email_validate_massive')

    with allure.step("2. Se validan todas las respuestas de emails en DynamoDB del servicio"):
        ValidateEmailMassiveDynamo.validate_event_dynamo_massive(responses)


@pytest.mark.test_12060_session_success_client_case_a
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=34)
@allure.feature('test_12060_session_success_client_case_a')
def test_12060_session_success_client_case_a():
    with allure.step(
            "1. Validación de datos en el evento success MFA del login del user_id con un cliente un rol sin permisos added o excluded"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12060_session_success_client_case_a')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200,
                                                                                         status_code,
                                                                                         "Proceso ejecutado correctamente",
                                                                                         EXPECTED_ORIGIN)
    with allure.step("3. Validación de respuesta del servicio del item details"):
        ExceptionsLogin.validate_login_success_response(response, '')

    with allure.step("4. Validación con base de datos SUITE_DB del item details"):
        ExceptionsLogin.validate_permissions_against_db(response)

    with allure.step("5. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None,validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO



@pytest.mark.test_12060_session_success_client_case_b
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=35)
@allure.feature('test_12060_session_success_client_case_b')
def test_12060_session_success_client_case_b():
    with allure.step(
            "1. Validación de datos en el evento success MFA del login del user_id con un cliente un rol con permisos added y sin permisos excluded"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12060_session_success_client_case_b')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200,
                                                                                         status_code,
                                                                                         "Proceso ejecutado correctamente",
                                                                                         EXPECTED_ORIGIN)
    with allure.step("3. Validación de respuesta del servicio del item details"):
        ExceptionsLogin.validate_login_success_response(response, '')

    with allure.step("4. Validación con base de datos SUITE_DB del item details"):
        ExceptionsLogin.validate_permissions_against_db(response)

    with allure.step("5. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None,validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12060_session_success_client_case_d
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=37)
@allure.feature('test_12060_session_success_client_case_d')
def test_12060_session_success_client_case_d():
    with allure.step(
            "1. Validación de datos en el evento success MFA del login del user_id con un cliente un rol con permisos added y excluded"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12060_session_success_client_case_d')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200,
                                                                                         status_code,
                                                                                         "Proceso ejecutado correctamente",
                                                                                         EXPECTED_ORIGIN)
    with allure.step("3. Validación de respuesta del servicio del item details"):
        ExceptionsLogin.validate_login_success_response(response, '')

    with allure.step("4. Validación con base de datos SUITE_DB del item details"):
        ExceptionsLogin.validate_permissions_against_db(response)

    with allure.step("5. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None,validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO


@pytest.mark.test_12060_session_success_client_case_f
@pytest.mark.sec_validate_login_service
@pytest.mark.all_login
@pytest.mark.run(order=39)
@allure.feature('test_12060_session_success_client_case_f')
def test_12060_session_success_client_case_f():
    with allure.step(
            "1. Validación de datos en el evento success MFA del login del user_id con dos clientes con sus permisos respectivos"):
        login = PostLogin()
        response = login.login('data_sec_validate_login_service_12060_session_success_client_case_f')
        status_code = UtilRememberDataProcess.get_response_status_code()
        logger.debug(f'Este es el status_code capturado en feature:::: {status_code}')

    with allure.step("2. Validación de respuesta del servicio"):
        ExceptionsResponseValidator.validate_common_execution_fields_response_successful(response, 12020, 200,
                                                                                         status_code,
                                                                                         "Proceso ejecutado correctamente",
                                                                                         EXPECTED_ORIGIN)
    with allure.step("3. Validación de respuesta del servicio del item details"):
        ExceptionsLogin.validate_login_success_response(response, '')

    with allure.step("4. Validación con base de datos SUITE_DB del item details"):
        ExceptionsLogin.validate_permissions_against_db(response)

    with allure.step("5. Validar datos de tracking en DynamoDB"):
        verifier = UtilVerifyRegisterEvent()
        validation_result = verifier.validate_event_success("EVENT_SUCCESS", None,validate_new_fields=True)
        assert validation_result, ERROR_DYNAMO


