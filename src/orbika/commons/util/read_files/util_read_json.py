import json
import logging
import os

logger = logging.getLogger(__name__)


class UtilReadJson:

    @staticmethod
    def read_json_files(archivo):
        env = os.getenv('ENVIRONMENT')
        base_path = os.path.join("resources", "data", env)
        json_path = os.path.join(base_path, archivo)

        if not os.path.exists(json_path):
            src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
            json_path = os.path.join(src_dir, "resources", "data", env, archivo)

        logger.info(f"Intentando leer el archivo en la ruta: {json_path}")

        if not os.path.exists(json_path):
            logger.error(f"No se encontró el archivo de test cases en la ruta: {json_path}")
            return None  # Retorna None si no encuentra el archivo

        try:
            with open(json_path, "r", encoding="utf-8") as file:
                json_data = json.load(file)
                logger.info(f"Archivo cargado correctamente: {json_path}")
                logger.debug(f"Contenido del archivo: {json_data}")
                return json_data

        except Exception as e:
            logger.error(f"Error al leer el archivo JSON: {e}")
            return None
