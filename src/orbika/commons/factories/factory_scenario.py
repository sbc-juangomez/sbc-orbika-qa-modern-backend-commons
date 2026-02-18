import copy
import importlib
import logging
import os
import re

from src.orbika.commons.util.remember_data_process.util_remember_data_process import UtilRememberDataProcess

logger = logging.getLogger(__name__)


class FactoryScenario:
    @staticmethod
    def get_data(jsons, scenario):
        for item in jsons:
            if item['scenario'] == scenario:
                return copy.deepcopy(item['data'])
        return None

    @staticmethod
    def get_scenario_data(scenario_and_module):
        logger.debug(f"esto es scenario_and_module {scenario_and_module}")
        environment = os.getenv('ENVIRONMENT')
        functionality = os.getenv('FUNCTIONALITY')
        logger.info(f"esta es la funcionalidad que llega al iniciar get_scenario_data::: {functionality}")
        try:
            match = re.match(r"^(.*?_\D+)(\d+_.+)$", scenario_and_module)
            if match:
                module_part, scenario = match.groups()
                module_part = module_part.rstrip('_')
            else:
                logger.error(f"No se pudo dividir correctamente 'scenario_and_module': {scenario_and_module}")
                return None

            logger.debug(f"esto es module_part {module_part}")
            logger.debug(f"esto es scenario {scenario}")
            UtilRememberDataProcess.set_scenario(scenario)
            code_match = re.match(r"^(\d+)_", scenario)
            code = code_match.group(1) if code_match else None
            UtilRememberDataProcess.set_code(code)
            logger.debug(f"esto es code {code}")
            base_module = f'src.resources.data.{environment}.{functionality}'
            logger.debug(f"esto es base_module {base_module}")
            module_name = f"{base_module}.{module_part}"
            module = importlib.import_module(module_name)
            logger.debug(f"esto es module {module}")

            class_name = ''.join([part.capitalize() for part in module_part.split('_')])
            scenario_class = getattr(module, class_name)
            logger.debug(f"esto es class_name {class_name}")

            json_data = getattr(scenario_class, 'JSON', None)
            # logger.debug(f"esto es json_data {json_data}")
            if json_data:
                return FactoryScenario.get_data(json_data, scenario_and_module)

            logger.error(f"Escenario '{scenario_and_module}' no encontrado en '{module_name}'")
            return None
        except Exception as e:
            logger.error(f"Error al cargar el escenario '{scenario_and_module}': {e}")
            return None
