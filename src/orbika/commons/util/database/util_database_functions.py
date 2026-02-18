import logging

from src.orbika.commons.util.database.util_connections_database import UtilConnectionsDatabase

logger = logging.getLogger(__name__)


class UtilDatabaseFunctions:

    def __init__(self):
        self.db_connection = UtilConnectionsDatabase()

    def get_user_database(self, email):
        connection = self.db_connection.create_connection(database='suite-db')

        try:
            cursor = connection.cursor()
            query = """select * from "security".users where email = %s"""
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            logger.info(f'Resultados de la base de datos::: {result}')
            cursor.close()
            return result
        except Exception as e:
            logger.error(f'Error al consultar el usuario en la base de datos:: {e}')
        return None

    def update_cognito_id_user_database(self, id, email):
        connection = self.db_connection.create_connection(database='orbika-db')

        try:
            cursor = connection.cursor()
            query = """UPDATE "security".users
                       set cognito_id = %s
                       where email = %s
                        """
            cursor.execute(query, (id, email,))
            connection.commit()
            cursor.close()
            logger.info(f'Usuario actualizado en la base de datos con cognito_id::: {id}')
        except Exception as e:
            logger.error(f'Error al actualizar el usuario en base de datos:: {e}')

    def associate_user_with_insurer(self, email):
        connection = self.db_connection.create_connection(database='orbika-db')

        try:
            cursor = connection.cursor()

            # Verificar si ya existe la asociación
            check_query = """
                SELECT 1 FROM "security".user_insurer ui
                JOIN "security".users u ON ui.user_id = u.id
                WHERE u.email = %s
            """
            cursor.execute(check_query, (email,))
            exists = cursor.fetchone()

            if exists:
                logger.debug('El usuario ya está asociado a la aseguradora')
            else:
                # Insertar solo si no existe
                insert_query = """
                    INSERT INTO "security".user_insurer (user_id, insurer_id)
                    VALUES ((SELECT id FROM "security".users WHERE email = %s), 1)
                """
                cursor.execute(insert_query, (email,))
                connection.commit()
                logger.debug('Usuario asociado correctamente a aseguradora')

            cursor.close()
        except Exception as e:
            logger.error(f"Error al asociar usuario con aseguradora: {e}")

    def associate_user_with_role(self, email, role_id, version=None):
        connection = self.db_connection.create_connection(database='orbika-db')

        try:
            cursor = connection.cursor()

            # Verificar si ya existe la asociación
            check_query = """
                SELECT 1 FROM "security".user_roles ur
                JOIN "security".users u ON ur.user_id = u.id
                WHERE u.email = %s AND ur.role_id = %s
            """
            cursor.execute(check_query, (email, role_id))
            exists = cursor.fetchone()

            if exists:
                logger.debug('El usuario ya está asociado a este rol')
            else:
                if version == 'v2':
                    cursor.execute("""SELECT MAX(id) FROM "security".user_roles""")
                    result_id = cursor.fetchone()[0]

                    # Si la tabla está vacía, empezamos en 1, si no, sumamos 1
                    nuevo_id = 1 if result_id is None else result_id + 1
                    insert_query = """
                        INSERT INTO "security".user_roles (id,user_id, role_id)
                        VALUES (%s,(SELECT id FROM "security".users WHERE email = %s), %s)
                    """
                    cursor.execute(insert_query, (nuevo_id, email, role_id))

                else:
                    # Insertar solo si no existe
                    insert_query = """
                        INSERT INTO "security".user_roles (user_id, role_id, insurer_id)
                        VALUES ((SELECT id FROM "security".users WHERE email = %s), %s, 1)
                    """
                    cursor.execute(insert_query, (email, role_id))
                connection.commit()
                logger.debug('Usuario asociado correctamente a rol')

            cursor.close()
            logger.debug('usuario asociado correctamente a rol')
        except Exception as e:
            logger.error(f"Error al asociar usuario con roles:: {e}")

    def create_user_database(self, id, email):
        connection = self.db_connection.create_connection(database='orbika-db')
        logger.debug(f"id insertar {id}")
        logger.debug(f"email insertar {email}")
        try:
            cursor = connection.cursor()
            query = """insert into "security".users 
                           (cognito_id,email,"name",lastname,phone,country_code,status_user_id,last_connection)
                            values 
                            (%s, %s ,'Usuar1', 'Temp', '3216546565', '+57', 1, '2024-11-05 22:49:15.076-05')"""
            cursor.execute(query, (id, email,))
            connection.commit()
            cursor.close()
            logger.debug('Usuario creado en la base de datos')
        except Exception as e:
            logger.error(f"El usuario no se puede crear en la base de datos::: {e}")

    def associate_user_with_permission(self, email):
        connection = self.db_connection.create_connection(database='orbika-db')
        try:
            cursor = connection.cursor()
            query = """
                    INSERT INTO "security".user_permissions (user_id,permission_id,status,insurer_id)
                    values       
                ((select id from "security".users where email = %s), 4,true,1)"""
            cursor.execute(query, (email,))
            connection.commit()
            cursor.close()
            logger.debug('usuario asociado correctamente a permisos')
        except Exception as e:
            logger.error(f"Error al asociar usuario con permisos:: {e}")
