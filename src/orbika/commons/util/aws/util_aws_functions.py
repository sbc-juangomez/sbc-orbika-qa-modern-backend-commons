import logging
import time

from botocore.exceptions import NoCredentialsError, ClientError

from src.orbika.commons.conf.aws.conf_data_connection_aws import ConfDataConnectionAws
from src.orbika.commons.util.aws.util_connections_aws import UtilConnectionsAws
from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess

logger = logging.getLogger(__name__)


class UtilAwsFunctions:
    def __init__(self):
        self.get_connection_aws = UtilConnectionsAws()
        self.get_dates_cognito = ConfDataConnectionAws().get_dates_params('cognito')
        self.get_dates_dynamodb = ConfDataConnectionAws().get_dates_params('dynamodb')

    def conf_mfa_client_cognito(self, enabled=True):
        client = self.get_connection_aws.get_client_aws('cognito')

        # 1. Prepara los argumentos (kwargs) base
        kwargs_boto = {
            'UserPoolId': self.get_dates_cognito['USER_POOL_ID'],
            'MfaConfiguration': 'ON' if enabled else 'OFF'
        }

        # 2. SOLO añade el bloque de configuración si vas a HABILITAR
        if enabled:
            kwargs_boto['SoftwareTokenMfaConfiguration'] = {
                'Enabled': True
            }

        try:
            # 4. Pasa los argumentos desempaquetados usando **
            response = client.set_user_pool_mfa_config(**kwargs_boto)

            logger.info(f'MFA configurado correctamente para el cliente: {response}')
            return response


        except Exception as e:
            logger.error(f'Error al configurar MFA para el cliente en Cognito: {e}')
            return None

    def get_data_tracking_dynamodb(self, table, transaction_id):

        valid_tables = ["EVENT_SUCCESS", "EVENT_FAIL"]
        if table in valid_tables:
            data_dynamo = self._query_event_dynamodb(table, transaction_id)
            return data_dynamo
        else:
            logger.error(f"Tabla desconocida: {table}")
            return None

    def _query_event_dynamodb(self, event_type, transaction_id):

        logger.info(f"Ejecutando consulta para {event_type}.")

        if not transaction_id:
            logger.error("No se puede ejecutar el query en DynamoDB debido a que no se encontró el transaction_id.")
            return None

        logger.info(f"Valor del transaction_id obtenido: {transaction_id}")

        client = self.get_connection_aws.get_client_aws('dynamodb')
        table_tracking = self.get_dates_dynamodb.get(event_type)

        if not table_tracking:
            logger.error(f"Tabla desconocida para {event_type}.")
            return None

        params = {
            "index_name": "transaction-id-index",
        }

        response = self._query_dynamodb(
            client,
            table_tracking,
            params,
            key="transaction_id",
            value=str(transaction_id)
        )

        if not response:
            logger.info("No se encontraron resultados en el primer intento, esperando 3 segundos para reintentar...")
            time.sleep(5)
            response = self._query_dynamodb(
                client,
                table_tracking,
                params,
                key="transaction_id",
                value=str(transaction_id)
            )

        if response:
            logger.info("Consulta ejecutada exitosamente.")
        else:
            logger.warning(f"No se encontraron resultados tras el reintento en {event_type}.")

        return response

    def _query_dynamodb(self, client, table_tracking, params, key, value):

        try:
            logger.info(
                f"Iniciando consulta en DynamoDB para la tabla: {table_tracking}, Índice: {params['index_name']}"
            )

            response = client.query(
                TableName=table_tracking,
                IndexName=params["index_name"],
                KeyConditionExpression=f"{key} = :value",
                ExpressionAttributeValues={
                    ":value": {"S": value}
                }
            )

            logger.debug(f"Respuesta de DynamoDB: {response}")

            if 'Items' in response and response['Items']:
                logger.debug(f"Registros encontrados: {response['Items']}")
                return response['Items']
            else:
                logger.warning(f"No se encontraron datos en la tabla {table_tracking}. Respuesta: {response}")
                return None

        except NoCredentialsError:
            logger.error("Las credenciales de AWS no fueron encontradas.")
            return None

        except ClientError as e:
            error_message = e.response['Error']['Message']
            logger.error(f"Error de cliente al consultar DynamoDB: {error_message}")
            return None

        except Exception as e:
            logger.error(f"Error inesperado al consultar DynamoDB: {str(e)}")
            return None

    def check_cognito_user_exists(self, email):
        client = self.get_connection_aws.get_client_aws('cognito')
        try:
            # Intentar obtener información del usuario
            response = client.admin_get_user(
                UserPoolId=self.get_dates_cognito['USER_POOL_ID'],
                Username=email
            )
            logger.info(f"Usuario encontrado: {response}")
            return True  # El usuario existe
        except client.exceptions.UserNotFoundException:
            logger.info(f"El usuario con email {email} no existe en Cognito.")
            return False  # El usuario no existe
        except Exception as e:
            logger.error(f"Error al verificar si el usuario existe en Cognito: {e}")
            raise  # Lanzar la excepción para manejo externo

    def delete_user_cognito(self, username):
        client = self.get_connection_aws.get_client_aws('cognito')
        try:
            client.admin_delete_user(
                UserPoolId=self.get_dates_cognito['USER_POOL_ID'],
                Username=username
            )
            logger.info(f"Usuario '{username}' eliminado correctamente.")
        except Exception as e:
            logger.error(f"Error al eliminar el usuario en Cognito: {e}")


    def create_cognito_user(self, temporary_password, email):
        client = self.get_connection_aws.get_client_aws('cognito')
        try:

            response = client.admin_create_user(
                UserPoolId=self.get_dates_cognito['USER_POOL_ID'],
                TemporaryPassword=temporary_password,
                Username=email,
                UserAttributes=[
                    {'Name': 'email', 'Value': email},
                    {'Name': 'email_verified', 'Value': 'true'}
                ],
                MessageAction='SUPPRESS'
            )
            user_id = response['User']['Username']
            UtilRememberDataProcess.set_cognito_id_user(user_id)
            logger.info(f"Usuario creado correctamente: {response}")
            return response
        except client.exceptions.UsernameExistsException:
            logger.info(f"El usuario con email {email} ya existe en Cognito.")
            user_data = client.admin_get_user(
                UserPoolId=self.get_dates_cognito['USER_POOL_ID'],
                Username=email
            )
            # Construir una respuesta con la misma estructura que admin_create_user
            response = {
                "User": {
                    "Username": user_data['Username'],
                    "UserCreateDate": user_data.get('UserCreateDate', None),
                    "UserLastModifiedDate": user_data.get('UserLastModifiedDate', None),
                    "Enabled": user_data.get('Enabled', True),
                    "UserStatus": user_data.get('UserStatus', 'CONFIRMED'),
                    "Attributes": user_data['UserAttributes']
                }
            }
            user_id = response['User']['Username']
            UtilRememberDataProcess.set_cognito_id_user(user_id)
            logger.info(f"Usuario existente: {response}")
            return response
        except Exception as e:
            # Manejo general de errores
            logger.error(f"Error al crear el usuario en Cognito: {e}")
            return None
