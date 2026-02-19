import logging

import requests

from orbika.commons.models.headers.models_headers_validate import ModelsHeadersValidate
from orbika.commons.util.read_files.util_read_json import UtilReadJson
from orbika.commons.util.transversal_functions.util_data_generator import UtilDataGenerator

logger = logging.getLogger(__name__)


class EndpointsHeadersValidate:

    @staticmethod
    def request_massive_headers(url, body, headers, params, request_method, access_token='',json_file="test_cases_headers.json"):
        logger.debug(f'URL:: {url}')
        logger.debug(f'BODY:: {body}')
        logger.debug(f'HEADERS:: {headers}')
        logger.debug(f'PARAMS:: {params}')
        logger.debug(f'REQUEST_METHOD:: {request_method}')
        if access_token != '':
            logger.debug(f'ACCESS_TOKEN:: {access_token}')
        try:
            valid_methods = {'GET': requests.get, 'POST': requests.post, 'PUT': requests.put, 'DELETE': requests.delete}
            if request_method not in valid_methods:
                logger.error(f"Método HTTP inválido: {request_method}")
                return []
            headers_cases = UtilReadJson.read_json_files(json_file)
            if not headers_cases:
                logger.warning("El archivo JSON está vacío o no contiene casos válidos.")
                return []
            return EndpointsHeadersValidate._process_cases(url, body, headers, params, access_token, request_method, headers_cases, valid_methods)
        except Exception as e:
            logger.error(f"Error al ejecutar solicitud de forma masiva: {e}")
            return []

    @staticmethod
    def _process_cases(url, body, headers, params, access_token, request_method, headers_cases, valid_methods):
        responses = []
        for case in headers_cases:
            logger.debug(f"Peticion de caso: {case}")
            if not case:
                logger.warning(f"Caso inválido en el JSON: {case}")
                continue
            scenario, expects, new_headers = EndpointsHeadersValidate._prepare_case(headers, case, access_token)
            transaction_id, session_id = EndpointsHeadersValidate._generate_ids(new_headers, scenario)
            try:
                logger.debug(f'request masivo: {body}')
                response = EndpointsHeadersValidate._send_request(
                    url, body, new_headers, params, request_method, valid_methods
                )
                insurer_id = params.get('insurer_id', None)
                logger.debug(f'insurer obtenido de params {insurer_id}')
                if insurer_id is None:
                    input_body = body.get('input', None)
                    if input_body is not None:
                        insurer_id = input_body.get('insurer_id', None)
                        logger.debug(f'insurer obtenido del body con input {insurer_id}')
                    else:
                        insurer_id = body.get('insurer_id', None)
                        logger.debug(f'insurer obtenido del body {insurer_id}')
                if insurer_id is None:
                    insurer_id = headers.get('insurer_id', None)
                    logger.debug(f'insurer obtenido de headers {insurer_id}')
                responses.append(
                    ModelsHeadersValidate(scenario, response.status_code, response.json(), transaction_id, session_id, expects,
                                          new_headers.get('email', False), insurer_id).get_response_data_headers()
                )
            except requests.RequestException as e:
                logger.error(f"Error al realizar la solicitud {request_method} para el caso {case}: {e}")
                ModelsHeadersValidate.get_response_data_headers_error(scenario, transaction_id, session_id, expects, new_headers.get('email', False), None)
        logger.debug(f'retornando las repuestas :::::::::::::::::::::::: {responses}')
        return responses

    @staticmethod
    def _prepare_case(headers, case, access_token):
        new_headers = headers.copy()
        new_headers.update(case['data']['headers'])

        if 'Authorization' in new_headers:
            new_headers['Authorization'] = access_token

        scenario = case['scenario']
        expects = case['expects']
        return scenario, expects, new_headers

    @staticmethod
    def _generate_ids(new_headers, scenario):
        transaction_id = new_headers.get('transaction_id', False)
        session_id = new_headers.get('session_id', False)

        if transaction_id and scenario != 'transaction_id_uuid_validate':
            transaction_id = UtilDataGenerator.generate_uuid()
            new_headers['transaction_id'] = transaction_id

        if session_id and scenario != 'session_id_uuid_valid':
            session_id = UtilDataGenerator.generate_uuid()
            new_headers['session_id'] = session_id

        return transaction_id, session_id

    @staticmethod
    def _send_request(url, body, headers, params, request_method, valid_methods):
        request_function = valid_methods[request_method]
        return request_function(
            url,
            headers=headers,
            json=body if body else None,
            params=params if params else None,
            timeout=10
        )
