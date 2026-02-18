import logging

from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess
from src.orbika.commons.util.tracking.util_verify_register_event import UtilVerifyRegisterEvent

logger = logging.getLogger(__name__)


class ValidateEmailMassiveDynamo:

    @staticmethod
    def validate_event_dynamo_massive(responses,description=None):
        errores = []
        logger.info(f"esta es la lista de responses que llega a validate_event_fail: {responses}")

        for response in responses:

            transaction_id = response.get('transaction_id')
            session_id = response.get('session_id')
            UtilRememberDataProcess.set_session_id_header(session_id)
            logger.info(f"este es el session_id que voy a recordar desde validate event fail massive ::{session_id}")
            logger.info(f"este es el transaction_id obtenido para consultar en dynamodb::{transaction_id}")
            logger.info \
                (f"esto es lo que recordo de session_id_header dentro e validate_event fail ::{UtilRememberDataProcess.get_session_id_header()}")

            # Obtener expected_email de response
            expected_email = response.get('expected_email')
            email = response.get('email')
            # Validar el valor de expected_email
            if not expected_email:
                email = "invalid"  # Asignar "invalid" si expected_email es False

            UtilRememberDataProcess.set_email_header(email)
            logger.info(f"este es el email obtenido de responses:: {email}")
            data_response = response.get('response')
            UtilRememberDataProcess.set_response(data_response)
            register_dynamo = UtilVerifyRegisterEvent()
            logger.info("esta es la descripción que llega :: %s", description)
            if 200 <= response['status_code'] <= 299:
                diferencces = register_dynamo.validate_event_success('EVENT_SUCCESS', transaction_id)
            else:
                if description is not None:
                    diferencces = register_dynamo.validate_event_fail('EVENT_FAIL', transaction_id,description_response_edit=description)
                else:
                    diferencces = register_dynamo.validate_event_fail('EVENT_FAIL', transaction_id)

            if not diferencces:
                # Si se encontraron diferencias, agrega el correo y transaction_id a la lista de errores
                errores.append({
                    'email': email,
                    'transaction_id': transaction_id
                })
        UtilRememberDataProcess.resert_transaction_id()
        logger.info(f"esto es errores en validate event dynamo massive:::{errores}")
        assert len(errores) == 0, f"error, se encontraron diferencias en las validaciones de dynamodb::{errores}"

