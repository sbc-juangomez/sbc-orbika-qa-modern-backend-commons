import logging

logger = logging.getLogger(__name__)


class ExceptionsResponseValidator:

    @staticmethod
    def validate_common_execution_fields_response_successful(response, expected_code, expected_status_code, status_code, expected_description,
                                                             expected_origin):
        assert status_code == expected_status_code, (f"Se esperaba un código de estado {expected_status_code}, pero se "
                                                     f"obtuvo {status_code}")
        assert response.get('execution') is not None, "El campo 'execution' es obligatorio y no puede ser nulo"
        assert isinstance(response['execution']['artifact'], str) and response['execution'][
            'artifact'], "El campo 'artifact' debe ser una cadena no vacía"
        assert isinstance(response['execution']['duration'], (float, int)) and response['execution'][
            'duration'] > 0, "El campo 'duration' debe ser un número mayor que 0"
        assert "session_id" in response["execution"], "El campo 'session_id' no existe en la respuesta"

        assert response['result']['code'] == expected_code, f"El 'error code' no es {expected_code} se obtuvo {response['result']['code']}"
        assert response['result'][
                   'description'] == expected_description, f"El 'error description' no es {expected_description} se obtuvo {response['result']['description']}"
        assert response['result']['origin'] == expected_origin, f"El campo 'origin' no es {expected_origin} se obtuvo {response['result']['origin']} "

    @staticmethod
    def validate_error_fields(response, expected_code, expected_status_code, status_code, expected_description,
                              expected_details,
                              expected_origin):
        assert status_code == expected_status_code, f"Se esperaba un código de estado {expected_status_code}, pero se obtuvo {status_code}"
        assert response.get('execution') is not None, "El campo 'execution' es obligatorio y no puede ser nulo"
        assert isinstance(response['execution']['artifact'], str) and response['execution'][
            'artifact'], "El campo 'artifact' debe ser una cadena no vacía"
        assert isinstance(response['execution']['duration'], (float, int)) and response['execution'][
            'duration'] > 0, "El campo 'duration' debe ser un número mayor que 0"
        assert "session_id" in response["execution"], "El campo 'session_id' no existe en la respuesta"
        assert response['error']['code'] == expected_code, f"El 'error code' no es {expected_code} se obtuvo {response['error']['code']}"
        assert response['error'][
                   'description'] == expected_description, f"La descripción de error no es la esperada se obtuvo {response['error']['description']}"
        if expected_details is None:
            assert isinstance(response['error']['details'], str) and response['error'][
                'details'], "'details' debe ser una cadena no vacía ni nula"
        else:
            assert response['error'][
                       'details'] == expected_details, f"El detalle del error no es el esperado, se obtuvo {response['error']['details']} en lugar de {expected_details}"

        assert response['error']['origin'] == expected_origin, f"El campo 'origin' no es {expected_origin}"

    @staticmethod
    def validate_error_fields_soft(response, expected_code, expected_status_code, status_code, expected_description, expected_details,
                                   expected_origin):
        error_code_response = response.get('error').get('code', None)
        errors = [
            ExceptionsResponseValidator.assert_validate_equals(status_code, expected_status_code,
                                                               f"Se esperaba un código de estado 400, pero se obtuvo {status_code}"),
            ExceptionsResponseValidator.assert_validate_not_none(response.get('execution'), "El campo 'execution' es obligatorio y no puede ser nulo"),
            ExceptionsResponseValidator.assert_validate_instance(response['execution']['artifact'], str, "El campo 'artifact' debe ser una cadena"),
            ExceptionsResponseValidator.assert_validate_not_empty(response['execution'], "El campo 'artifact' debe ser una cadena no vacía"),
            ExceptionsResponseValidator.assert_validate_instance(response['execution']['duration'], float, "El campo 'duration' debe ser numerico"),
            ExceptionsResponseValidator.assert_validate_max_value(response['execution']['duration'], 0,
                                                                  "El campo 'duration' debe ser un número mayor que 0"),
            ExceptionsResponseValidator.assert_validate_value_in_obj("session_id", response["execution"],
                                                                     "El campo 'session_id' no existe en la respuesta"),
            ExceptionsResponseValidator.assert_validate_equals(response['error']['code'], expected_code,
                                                               f"El 'error code' no es {expected_code}, se obtuvo {error_code_response}"),
            ExceptionsResponseValidator.assert_validate_equals(response['error']['description'], expected_description,
                                                               "La descripción de error no es la esperada"),
            ExceptionsResponseValidator.assert_validate_equals(response['error']['details'], expected_details, "El detalle del error no es el esperado"),
            ExceptionsResponseValidator.assert_validate_equals(response['error']['origin'], expected_origin,
                                                               f"El campo 'origin' no es {expected_origin}")]

        errors = [item for item in errors if item is not None]
        return errors

    @staticmethod
    def assert_validate_equals(result, expect, message):
        try:
            assert result == expect, message
        except AssertionError as e:
            return {"error": str(e)}

    @staticmethod
    def assert_validate_not_none(result, message):
        try:
            assert result is not None, message
        except AssertionError as e:
            return {"error": str(e)}

    @staticmethod
    def assert_validate_max_value(result, expect, message):
        try:
            assert result > expect, message
        except AssertionError as e:
            return {"error": str(e)}

    @staticmethod
    def assert_validate_instance(result, expect_type, message):
        try:
            assert isinstance(result, expect_type), message
        except AssertionError as e:
            return {"error": str(e)}

    @staticmethod
    def assert_validate_not_empty(result, message):
        try:
            assert result, message
        except AssertionError as e:
            return {"error": str(e)}

    @staticmethod
    def assert_validate_value_in_obj(result, expect, message):
        try:
            assert result in expect, message
        except AssertionError as e:
            return {"error": str(e)}

    # Valida que el listado sea alfabetico en las lambdas
    @staticmethod
    def validate_sort_service_lists(list_service, field, name_sevice):
        names = [workshop[field] for workshop in list_service]
        is_order = names == sorted(names, key=str.lower)
        assert is_order, f'Error al validar la lista para el servicio: {name_sevice}'

    @staticmethod
    def validate_json_key_values(json1: dict, json2: dict) -> bool:
        """
        Valida que cada clave en el primer JSON tenga el mismo valor
        en el segundo JSON.

        Args:
            json1 (dict): El primer diccionario (JSON).
            json2 (dict): El segundo diccionario (JSON).

        Returns:
            bool: True si todas las claves de json1 tienen el mismo valor en json2,
                  False en caso contrario. Imprime las diferencias encontradas.
        """
        is_valid = True

        # Iterar sobre las claves del primer JSON
        for key, value1 in json1.items():
            if key not in json2:
                logger.info(f"ERROR: La clave '{key}' existe en el primer JSON pero no en el segundo.")
                is_valid = False
                continue  # Pasa a la siguiente clave

            value2 = json2[key]

            # Comparar los valores
            if value1 != value2:
                logger.info(f"ERROR: La clave '{key}' tiene valores diferentes:")
                logger.info(f"  - Valor en JSON1: {value1}")
                logger.info(f"  - Valor en JSON2: {value2}")
                is_valid = False

        for key in json2:
            if key not in json1:
                logger.info(f"ADVERTENCIA: La clave '{key}' existe en el segundo JSON pero no en el primero.")
                is_valid = False

        return is_valid
