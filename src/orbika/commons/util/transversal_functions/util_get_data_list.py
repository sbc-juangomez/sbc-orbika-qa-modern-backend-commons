import logging


logger = logging.getLogger(__name__)
class UtilGetDataList:

    """
    Utility class to get data list from a given data source.
    """

    @staticmethod
    def get_list(insurer: int, type_vehicle: int, type_operation: int,data_list: dict) -> list:
        result_country = data_list.get(insurer, {})
        logger.info("result_country: %s", result_country)
        result_vehicle = result_country.get(type_vehicle, {})
        logger.info("result_vehicle: %s", result_vehicle)
        lista_final = result_vehicle.get(type_operation, [])
        logger.info("lista_final: %s", lista_final)
        return lista_final