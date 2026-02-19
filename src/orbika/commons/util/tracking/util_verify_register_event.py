import logging
import os
import time
import uuid

from orbika.commons.util.aws.util_aws_functions import UtilAwsFunctions
from orbika.commons.util.constants.constants_integration_data_ia import EnumIntegrationDataIA
from orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from orbika.commons.util.transversal_functions.util_get_data_list import UtilGetDataList

logger = logging.getLogger(__name__)


class UtilVerifyRegisterEvent:

    def __init__(self):
        self.aws_functions = UtilAwsFunctions()
        self._load_data_from_memory()

    def _load_data_from_memory(self):
        self.email_body = UtilRememberDataProcess.get_email()
        self.session_id_body = UtilRememberDataProcess.get_session_id()
        self.email_header = UtilRememberDataProcess.get_email_header()
        self.session_id_header = UtilRememberDataProcess.get_session_id_header()
        self.response = UtilRememberDataProcess.get_response()
        self.body = UtilRememberDataProcess.get_body()
        self.response_details = UtilRememberDataProcess.get_response_details_true()
        self.status_code = UtilRememberDataProcess.get_response_status_code()

        logger.debug(f"response_details: {self.response_details}")
        logger.debug(f"response: {self.response}")
        logger.debug(f"status_code: {self.status_code}")
        logger.info(f"session_id_header: {self.session_id_header}")
        logger.info(f"email_header: {self.email_header}")

    def _get_sources_by_functionality(self):
        if os.getenv('FUNCTIONALITY') == "login":
            return self.session_id_body, self.email_body
        return self.session_id_header, self.email_header

    def _add_difference(self, differences, field, expected, found):
        differences.append({
            "field": field,
            "expected": expected,
            "found": found
        })

    def _validate_common_fields(self, event_dynamo, differences):
        session_id_source, email_source = self._get_sources_by_functionality()

        if event_dynamo.get("session_id", {}).get("S") != session_id_source:
            self._add_difference(differences, "session_id", session_id_source, event_dynamo.get("session_id"))

        if event_dynamo.get("email", {}).get("S") != email_source:
            self._add_difference(differences, "email", email_source, event_dynamo.get("email"))

        try:
            duration = float(event_dynamo.get("duration", {}).get("S", 0))
            if duration <= 0:
                self._add_difference(differences, "duration", "> 0", event_dynamo.get("duration"))
        except ValueError:
            self._add_difference(differences, "duration", "a valid float", event_dynamo.get("duration"))

        insurer_value = UtilRememberDataProcess.get_insurer_id()
        expected_insurer = str(insurer_value) if insurer_value is not None else "cross"
        if event_dynamo.get("insurer", {}).get("S") != expected_insurer:
            self._add_difference(differences, "insurer", expected_insurer, event_dynamo.get("insurer", {}).get("S"))

        if not event_dynamo.get("time"):
            self._add_difference(differences, "time", "not null", event_dynamo.get("time"))

    def _validate_new_fields(self, event_dynamo, differences):
        logger.debug(f"event_dynamo que entra a _validate_new_fields: {event_dynamo}")
        request = event_dynamo.get("request", {}).get("S")
        logger.debug(f"request extraido de dynamo: {request}")
        response = event_dynamo.get("response", {}).get("S")
        logger.debug(f"response extraido de dynamo: {response}")
        status_code = event_dynamo.get("status_code", {}).get("S")
        logger.debug(f"status_code extraido de dynamo: {status_code}")
        user_id = event_dynamo.get("user_id", {}).get("N")
        logger.debug(f"user_id extraido de dynamo: {user_id}")
        event = event_dynamo.get("artifact", {}).get("S")
        logger.debug(f"event extraido de dynamo: {event}")

        if not request:
            self._add_difference(differences, "request", "not empty", request)

        if not response:
            self._add_difference(differences, "response", "not empty", response)

        if not event:
            self._add_difference(differences, "event", "not empty", event)

        if status_code != str(self.status_code):
            self._add_difference(differences, "status_code", str(self.status_code), status_code)

        if not user_id:
            self._add_difference(differences, "user_id", "non-empty integer", user_id)
        else:
            try:
                int(user_id)
            except ValueError:
                self._add_difference(differences, "user_id", "integer", user_id)

    def _validate_event_dynamo(self, event_results, differences):
        if not event_results:
            logger.error("No se encontraron resultados en event_results.")
            return False
        expect_list = UtilGetDataList.get_list(UtilRememberDataProcess().get_insurer_id()
                                               ,UtilRememberDataProcess.get_vehicle_type_id(),UtilRememberDataProcess.get_type_operation_id(),
                                               EnumIntegrationDataIA().list_integrations)
        if set(event_results) != set(expect_list):
            self._add_difference(differences, "event", expect_list, event_results)
        if differences:
            logger.error(f"Diferencias encontradas en el registo de servicios de ia : {differences}")
            return False

        logger.info("Validación exitosa de servicios de ia ")
        return True


    def validate_event_success(self, table, transaction_id, validate_new_fields=False, validate_several_fields=False):
        if os.environ['ENVIRONMENT'] == 'mock':
            return True

        logger.info(f"Validando tabla: {table}")
        transaction_id = transaction_id or UtilRememberDataProcess.get_transaction_id()
        if validate_several_fields:
            time.sleep(2)
        event_dynamo = self.aws_functions.get_data_tracking_dynamodb(table, transaction_id)

        if not event_dynamo:
            logger.error("No se obtuvieron datos de EVENT_SUCCESS.")
            return False

        differences = []
        if validate_several_fields:
            functionality = os.getenv('FUNCTIONALITY', '')
            functionality = functionality.replace('_', '-').lower()
            found_item = []
            logger.debug(f"event_dynamo seleccionado: {event_dynamo}")
            event_results = [item['event']['S'] for item in event_dynamo]
            logger.debug(f"event_result: {event_results}")
            for item in event_dynamo:
                event_dict = item.get('event', {})
                event_string = event_dict.get('S', '')

                if functionality in event_string:
                    found_item.append(item)  # Guardamos el diccionario completo
                    break
            if found_item:
                logger.debug(f"Elemento encontrado: {found_item}")
                event_dynamo = found_item
            else:
                logger.error("No se encontró  elemento con 'vac-data-integration-ia' en el campo 'event'.")
                return False
            self._validate_event_dynamo(event_results, differences)
        event_dynamo = event_dynamo[0]
        logger.debug(f"event_dynamo seleccionado posicion 0: {event_dynamo}")

        self._validate_common_fields(event_dynamo, differences)

        if validate_new_fields:
            self._validate_new_fields(event_dynamo, differences)

        if differences:
            logger.error(f"Diferencias encontradas: {differences}")
            return False

        logger.info("Validación exitosa: Los datos coinciden entre DynamoDB y el body.")
        return True





    def validate_event_fail(self, table, transaction_id, validate_new_fields=False,description_response_edit=None):
        if os.environ['ENVIRONMENT'] == 'mock':
            return True

        logger.info(f"Validando tabla de error: {table}")
        transaction_id = transaction_id or UtilRememberDataProcess.get_transaction_id()
        logger.debug(f"transaction_id obtenido en validate_event_fail : {transaction_id}")
        event_dynamo = self.aws_functions.get_data_tracking_dynamodb(table, transaction_id)

        if not event_dynamo:
            logger.error(f"No se obtuvieron datos de EVENT_FAIL para el transaction_id: {transaction_id}")
            return False

        event_dynamo = event_dynamo[0]
        logger.debug(f"event_dynamo seleccionado posicion 0: {event_dynamo}")
        differences = []
        session_id_source, email_source = self._get_sources_by_functionality()

        session_id_dynamo = event_dynamo.get("session_id", {}).get("S")
        email_dynamo = event_dynamo.get("email", {}).get("S")

        if session_id_source in [False, 'sessions_id', '']:
            if session_id_dynamo != "unknown":
                self._add_difference(differences, "session_id", "unknown", session_id_dynamo)
        elif not isinstance(session_id_source, str) or not self.is_valid_uuid(session_id_source):
            if session_id_dynamo != "invalid":
                self._add_difference(differences, "session_id", "invalid", session_id_dynamo)
        elif session_id_dynamo != session_id_source:
            self._add_difference(differences, "session_id", session_id_source, session_id_dynamo)

        if email_source in [False, 'emails', None, ""]:
            if email_dynamo != "unknown":
                self._add_difference(differences, "email", "unknown", email_dynamo)
        elif not isinstance(email_source, str) or len(email_source) < 5 or len(
                email_source) > 255 or email_source == 'invalid':
            if email_dynamo != "invalid":
                self._add_difference(differences, "email", "invalid", email_dynamo)
        elif email_dynamo != email_source:
            self._add_difference(differences, "email", email_source, email_dynamo)
        detail_response = self.response.get("error", {}).get("details")
        error_description = event_dynamo.get("error_description", {}).get("S")
        error_message = event_dynamo.get("error_message", {}).get("S")

        if description_response_edit is not None and "No se encontró información de las piezas" in error_description:
            detail_response= description_response_edit

        description_response = self.response.get("error", {}).get("description")
        logger.info("Este es el valor de detail_response: %s", detail_response)
        logger.info("Este es el valor de detail_response de dynamo: %s", error_description)


        if detail_response and error_description != detail_response:
            self._add_difference(differences, "error_description", detail_response, error_description)

        if description_response and error_message != description_response:
            self._add_difference(differences, "error_message", description_response, error_message)

        insurer_value = UtilRememberDataProcess.get_insurer_id()
        insurer_dynamo = event_dynamo.get("insurer", {}).get("S")
        logger.debug(f"insurer_value obtenido: {insurer_value}")
        logger.debug(f"insurer_dynamo obtenido: {insurer_dynamo}")

        if insurer_value is None:
            expected_insurer = "cross"
        elif insurer_value == "" or table in ["insurers_id", "insurer_ids"]:
            expected_insurer = "unknown"
        elif isinstance(insurer_value, float) or insurer_value in ['\"1\"', "1", 0] or (
                isinstance(insurer_value, int) and insurer_value > 32767):
            expected_insurer = "invalid"
        else:
            expected_insurer = str(insurer_value)

        if insurer_dynamo != expected_insurer:
            self._add_difference(differences, "insurer", expected_insurer, insurer_dynamo)

        if not event_dynamo.get("time"):
            self._add_difference(differences, "time", "not null", event_dynamo.get("time"))

        # ✅ Validación de nuevos campos (faltaba esta parte)
        if validate_new_fields:
            self._validate_new_fields(event_dynamo, differences)

        if differences:
            logger.error(f"Diferencias encontradas en evento fallido: {differences}")
            return False

        logger.info("Validación exitosa de evento fallido.")
        return True



    @staticmethod
    def is_valid_uuid(value):
        try:
            uuid.UUID(value)
            return True
        except (ValueError, TypeError):
            return False
