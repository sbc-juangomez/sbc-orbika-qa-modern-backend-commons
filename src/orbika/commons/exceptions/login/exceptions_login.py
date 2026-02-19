import logging
import re

from orbika.commons.util.database.util_database_suite_db import UtilDatabaseSuiteDB

logger = logging.getLogger(__name__)

UUID_REGEX = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)


class ExceptionsLogin:

    @staticmethod
    def validate_login_success_response(response, expected_challenge_name):
        # result.details
        logger.info(f"Este es la informacion de validate_login_success_response exceptions_login {response}")
        assert response['result']['details'] is not None and isinstance(response['result']['details'], dict), (
            "El campo 'details' es obligatorio, no puede ser nulo y debe ser un objeto (dict)"
        )

        if response['result']['details'].get("challenge_name") is not None:
            assert isinstance(response['result']['details']['challenge_name'], str), (
                f"El campo 'challenge_name' debe ser de tipo string, se obtuvo {type(response['result']['details']['challenge_name']).__name__}"
            )
            assert response['result']['details']['challenge_name'] == expected_challenge_name, (
                f"El campo 'challenge_name' esperado era '{expected_challenge_name}'"
            )

        else:
            assert response['result']['details']['cognito_id'] is not None, "El campo 'cognito_id' no existe en la respuesta"
            assert isinstance(response['result']['details']['cognito_id'], str), (
                f"El campo 'cognito_id' debe ser de tipo string, se obtuvo {type(response['result']['details']['cognito_id']).__name__}"
            )
            assert len(response['result']['details']['cognito_id'].strip()) > 0, "El campo 'cognito_id' no puede estar vacío"
            ExceptionsLogin.validate_result_details_field(response)

        if response['result']['details'].get("session") is not None:
            assert isinstance(response['result']['details']['session'], str), (
                f"El campo 'session' debe ser de tipo string, se obtuvo {type(response['result']['details']['session']).__name__}"
            )
            assert len(response['result']['details']['session'].strip()) > 0, "El campo 'session' no puede estar vacío"

    @staticmethod
    def auth_mfa_success_response(response):

        # existencia y tipo
        details = response.get("result", {}).get("details")
        assert details is not None, "El campo 'details' es obligatorio y no puede ser nulo"
        assert isinstance(details, dict), "El campo 'details' debe ser un objeto (dict)"

        ExceptionsLogin.validate_result_details_field(response)

    @staticmethod
    def validate_result_details_field(response):
        """
        Valida que el campo 'details' existe en 'result' y valida todos los campos
        que componen el objeto 'details' incluyendo su estructura completa.

        Args:
            response (dict): La respuesta del servicio a validar.

        Raises:
            AssertionError: Si algún campo requerido no existe, tiene un tipo incorrecto,
                          o no cumple con las validaciones esperadas.
        """

        details = response['result']['details']

        # Validar campos principales de details
        assert 'cognito_id' in details, "El campo 'cognito_id' no existe en 'details'"
        assert isinstance(details['cognito_id'], str) and details[
            'cognito_id'], "El campo 'cognito_id' debe ser una cadena no vacía"

        assert 'access_token' in details, "El campo 'access_token' no existe en 'details'"
        assert isinstance(details['access_token'], str) and details[
            'access_token'], "El campo 'access_token' debe ser una cadena no vacía"

        assert 'refresh_token' in details, "El campo 'refresh_token' no existe en 'details'"
        assert isinstance(details['refresh_token'], str) and details[
            'refresh_token'], "El campo 'refresh_token' debe ser una cadena no vacía"

        assert 'expires_in' in details, "El campo 'expires_in' no existe en 'details'"
        assert isinstance(details['expires_in'], (int, float)), "El campo 'expires_in' debe ser un número"
        assert details['expires_in'] > 0, "El campo 'expires_in' debe ser mayor que 0"

        # Validar session_expiration_time
        assert 'session_expiration_time' in details, "El campo 'session_expiration_time' no existe en 'details'"
        assert isinstance(details['session_expiration_time'],
                          dict), "El campo 'session_expiration_time' debe ser de tipo dict"

        session_exp = details['session_expiration_time']
        assert 'inactivity_warning_time' in session_exp, "El campo 'inactivity_warning_time' no existe en 'session_expiration_time'"
        assert isinstance(session_exp['inactivity_warning_time'],
                          (int, float)), "El campo 'inactivity_warning_time' debe ser un número"

        assert 'inactivity_alert_time' in session_exp, "El campo 'inactivity_alert_time' no existe en 'session_expiration_time'"
        assert isinstance(session_exp['inactivity_alert_time'],
                          (int, float)), "El campo 'inactivity_alert_time' debe ser un número"

        assert 'access_token_expiration_time' in session_exp, "El campo 'access_token_expiration_time' no existe en 'session_expiration_time'"
        assert isinstance(session_exp['access_token_expiration_time'],
                          (int, float)), "El campo 'access_token_expiration_time' debe ser un número"

        # Validar user_id
        assert 'user_id' in details, "El campo 'user_id' no existe en 'details'"
        assert isinstance(details['user_id'], (int, float)), "El campo 'user_id' debe ser un número"

        # Validar name
        assert 'name' in details, "El campo 'name' no existe en 'details'"
        assert isinstance(details['name'], str), "El campo 'name' debe ser de tipo str"

        # Validar clients
        assert 'clients' in details, "El campo 'clients' no existe en 'details'"
        assert isinstance(details['clients'], list), "El campo 'clients' debe ser de tipo list"
        assert len(details['clients']) > 0, "El campo 'clients' no puede estar vacío"

        # Validar estructura de cada cliente
        for idx, client in enumerate(details['clients']):
            assert isinstance(client, dict), f"El cliente en el índice {idx} debe ser de tipo dict"

            assert 'client_id' in client, f"El campo 'client_id' no existe en el cliente del índice {idx}"
            assert isinstance(client['client_id'],
                              (int, float)), f"El campo 'client_id' del cliente {idx} debe ser un número"

            assert 'client_name' in client, f"El campo 'client_name' no existe en el cliente del índice {idx}"
            assert isinstance(client['client_name'],
                              str), f"El campo 'client_name' del cliente {idx} debe ser de tipo str"

            assert 'country_id' in client, f"El campo 'country_id' no existe en el cliente del índice {idx}"
            assert isinstance(client['country_id'],
                              (int, float)), f"El campo 'country_id' del cliente {idx} debe ser un número"

            assert 'applications' in client, f"El campo 'applications' no existe en el cliente del índice {idx}"
            assert isinstance(client['applications'],
                              list), f"El campo 'applications' del cliente {idx} debe ser de tipo list"
            assert len(client['applications']) > 0, f"El campo 'applications' del cliente {idx} no puede estar vacío"

            # Validar estructura de cada aplicación
            for app_idx, application in enumerate(client['applications']):
                assert isinstance(application,
                                  dict), f"La aplicación en el índice {app_idx} del cliente {idx} debe ser de tipo dict"

                assert 'name' in application, f"El campo 'name' no existe en la aplicación {app_idx} del cliente {idx}"
                assert isinstance(application['name'],
                                  str), f"El campo 'name' de la aplicación {app_idx} del cliente {idx} debe ser de tipo str"

                assert 'app_client_default' in application, f"El campo 'app_client_default' no existe en la aplicación {app_idx} del cliente {idx}"
                assert isinstance(application['app_client_default'],
                                  bool), f"El campo 'app_client_default' de la aplicación {app_idx} del cliente {idx} debe ser de tipo bool"

                assert 'application_id' in application, f"El campo 'application_id' no existe en la aplicación {app_idx} del cliente {idx}"
                assert isinstance(application['application_id'], (int,
                                                                  float)), f"El campo 'application_id' de la aplicación {app_idx} del cliente {idx} debe ser un número"

                # Validar role
                assert 'role' in application, f"El campo 'role' no existe en la aplicación {app_idx} del cliente {idx}"
                assert isinstance(application['role'],
                                  dict), f"El campo 'role' de la aplicación {app_idx} del cliente {idx} debe ser de tipo dict"

                role = application['role']
                assert 'id' in role, f"El campo 'id' no existe en el role de la aplicación {app_idx} del cliente {idx}"
                assert isinstance(role['id'], (
                    int,
                    float)), f"El campo 'id' del role de la aplicación {app_idx} del cliente {idx} debe ser un número"

                assert 'name' in role, f"El campo 'name' no existe en el role de la aplicación {app_idx} del cliente {idx}"
                assert isinstance(role['name'],
                                  str), f"El campo 'name' del role de la aplicación {app_idx} del cliente {idx} debe ser de tipo str"

                # Validar domain dentro de role
                assert 'domain' in role, f"El campo 'domain' no existe en el role de la aplicación {app_idx} del cliente {idx}"
                assert isinstance(role['domain'],
                                  dict), f"El campo 'domain' del role de la aplicación {app_idx} del cliente {idx} debe ser de tipo dict"

                domain = role['domain']
                assert 'id' in domain, f"El campo 'id' no existe en el domain del role de la aplicación {app_idx} del cliente {idx}"
                assert isinstance(domain['id'], (int,
                                                 float)), f"El campo 'id' del domain del role de la aplicación {app_idx} del cliente {idx} debe ser un número"

                assert 'name' in domain, f"El campo 'name' no existe en el domain del role de la aplicación {app_idx} del cliente {idx}"
                assert isinstance(domain['name'],
                                  str), f"El campo 'name' del domain del role de la aplicación {app_idx} del cliente {idx} debe ser de tipo str"

                # Validar permissions dentro de role
                assert 'permissions' in role, f"El campo 'permissions' no existe en el role de la aplicación {app_idx} del cliente {idx}"
                assert isinstance(role['permissions'],
                                  list), f"El campo 'permissions' del role de la aplicación {app_idx} del cliente {idx} debe ser de tipo list"
                assert len(role[
                               'permissions']) > 0, f"El campo 'permissions' del role de la aplicación {app_idx} del cliente {idx} no puede estar vacío"

                # Validar estructura de cada permiso
                for perm_idx, permission in enumerate(role['permissions']):
                    assert isinstance(permission,
                                      dict), f"El permiso en el índice {perm_idx} del role de la aplicación {app_idx} del cliente {idx} debe ser de tipo dict"

                    assert 'id' in permission, f"El campo 'id' no existe en el permiso {perm_idx} del role de la aplicación {app_idx} del cliente {idx}"
                    assert isinstance(permission['id'], (int,
                                                         float)), f"El campo 'id' del permiso {perm_idx} del role de la aplicación {app_idx} del cliente {idx} debe ser un número"

                    assert 'name' in permission, f"El campo 'name' no existe en el permiso {perm_idx} del role de la aplicación {app_idx} del cliente {idx}"
                    assert isinstance(permission['name'],
                                      str), f"El campo 'name' del permiso {perm_idx} del role de la aplicación {app_idx} del cliente {idx} debe ser de tipo str"

                    assert 'path' in permission, f"El campo 'path' no existe en el permiso {perm_idx} del role de la aplicación {app_idx} del cliente {idx}"
                    assert isinstance(permission['path'],
                                      str), f"El campo 'path' del permiso {perm_idx} del role de la aplicación {app_idx} del cliente {idx} debe ser de tipo str"

                # Validar permissions_added (puede estar vacío)
                assert 'permissions_added' in application, f"El campo 'permissions_added' no existe en la aplicación {app_idx} del cliente {idx}"
                assert isinstance(application['permissions_added'],
                                  list), f"El campo 'permissions_added' de la aplicación {app_idx} del cliente {idx} debe ser de tipo list"

                # Validar permissions_excluded (puede estar vacío)
                assert 'permissions_excluded' in application, f"El campo 'permissions_excluded' no existe en la aplicación {app_idx} del cliente {idx}"
                assert isinstance(application['permissions_excluded'],
                                  list), f"El campo 'permissions_excluded' de la aplicación {app_idx} del cliente {idx} debe ser de tipo list"

    @staticmethod
    def validate_permissions_against_db(response: object) -> None:
        details = response["result"]["details"]
        user_id = details["user_id"]

        db = UtilDatabaseSuiteDB()

        try:
            logger.info(f"Este es la informacion de validate_permissions_against_db exceptions_login")

            resp_clients = details.get("clients", [])
            db_clients = db.get_user_clients(user_id)

            logger.info(f"Este es el resp_clients:: {resp_clients}")
            logger.info(f"Este es el db_clients:: {db_clients}")

            # 1) VALIDAR QUE EL RESPONSE TENGA CLIENTS
            if not resp_clients:
                raise AssertionError(f"El usuario {user_id} NO tiene clientes en response, esto es inválido")

            if not db_clients:
                raise AssertionError(f"El usuario {user_id} NO tiene clientes en base de datos (security.user_application_client)")

            db_clients_grouped = {}
            for c in db_clients:
                db_clients_grouped.setdefault(c["client_id"], []).append(c)

            logger.info(f"Este es el db_clients_grouped:: {db_clients_grouped}")

            # VALIDAR CLIENTES
            for client in resp_clients:

                client_id = client["client_id"]
                applications = client.get("applications", [])

                assert client_id in {c["client_id"] for c in db_clients}, (
                    f"El usuario {user_id} NO tiene asignado el client_id {client_id} en DB"
                )

                # ---------------------------------------------
                # VALIDAR APLICACIONES POR CLIENTE
                # ---------------------------------------------
                for app in applications:
                    app_name = app["name"]
                    role = app.get("role", {})
                    app_id = app.get("application_id")
                    permissions = role.get("permissions", [])
                    permissions_added = app.get("permissions_added", [])
                    permissions_excluded = app.get("permissions_excluded", [])

                    # Buscar application_client_id según client + application
                    db_app = next(
                        (a for a in db_clients if a["client_id"] == client_id and a["application_name"] == app_name),
                        None
                    )

                    assert db_app, (
                        f"El usuario {user_id} NO tiene asignada la aplicación '{app_name}' "
                        f"en el client_id {client_id} según DB"
                    )

                    application_client_id = db_app["application_client_id"]

                    # ---------------------------------------------
                    # VALIDAR ROLE Y SUS PERMISOS BASE
                    # ---------------------------------------------
                    role_id = role.get("id")
                    if role_id:
                        logger.info(
                            f"Validando permisos del rol id={role_id} para user_id={user_id}, app_id={app_id}, application_client_id={application_client_id}")
                        db_role_permissions = db.get_role_permissions(role_id, app_id, application_client_id)
                        db_perm_ids = {p["permission_id"] for p in db_role_permissions}
                        resp_perm_ids = {p["id"] for p in permissions}

                        missing = resp_perm_ids - db_perm_ids
                        assert not missing, (
                            f"Permisos del rol id={role_id} faltantes en DB: {missing}"
                        )

                    # ---------------------------------------------
                    # PERMISSIONS ADDED
                    # ---------------------------------------------
                    db_added = db.get_user_permissions(user_id, status=True)
                    db_added_ids = {p["permission_id"] for p in db_added}
                    resp_added_ids = {p["id"] for p in permissions_added}

                    missing_added = resp_added_ids - db_added_ids
                    assert not missing_added, (
                        f"permissions_added no coinciden con DB (faltan en DB): {missing_added}"
                    )

                    # ---------------------------------------------
                    # PERMISSIONS EXCLUDED
                    # ---------------------------------------------
                    db_excluded = db.get_user_permissions(user_id, status=False)
                    db_excluded_ids = {p["permission_id"] for p in db_excluded}
                    resp_excluded_ids = {p["id"] for p in permissions_excluded}

                    missing_excluded = resp_excluded_ids - db_excluded_ids
                    assert not missing_excluded, (
                        f"permissions_excluded no coinciden con DB (faltan en DB): {missing_excluded}"
                    )

        finally:
            db.close()

    @staticmethod
    def validate_associate_fotware_token_success_response(response):
        """
        Valida que el campo 'details' existe en 'result' y valida todos los campos
        que componen el objeto 'details' para el servicio sec-associate-fotware-token.

        Args:
            response (dict): La respuesta del servicio a validar.

        Raises:
            AssertionError: Si algún campo requerido no existe, tiene un tipo incorrecto,
                          o no cumple con las validaciones esperadas.
        """
        logger.info(f"Este es la informacion de validate_associate_fotware_token_success_response exceptions_login {response}")

        # Validar que details existe y es un diccionario
        details = response.get("result", {}).get("details")
        assert details is not None, "El campo 'details' es obligatorio y no puede ser nulo"
        assert isinstance(details, dict), "El campo 'details' debe ser un objeto (dict)"

        # Validar qr_base64
        assert 'qr_base64' in details, "El campo 'qr_base64' no existe en 'details'"
        assert isinstance(details['qr_base64'], str), (
            f"El campo 'qr_base64' debe ser de tipo string, se obtuvo {type(details['qr_base64']).__name__}"
        )
        assert len(details['qr_base64'].strip()) > 0, "El campo 'qr_base64' no puede estar vacío"

        # Validar session
        assert 'session' in details, "El campo 'session' no existe en 'details'"
        assert isinstance(details['session'], str), (
            f"El campo 'session' debe ser de tipo string, se obtuvo {type(details['session']).__name__}"
        )
        assert len(details['session'].strip()) > 0, "El campo 'session' no puede estar vacío"

        logger.info("Validación de details para sec-associate-fotware-token exitosa")