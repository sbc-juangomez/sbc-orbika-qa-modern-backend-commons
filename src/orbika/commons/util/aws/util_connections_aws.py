import logging

import boto3

from botocore.exceptions import BotoCoreError, NoCredentialsError, PartialCredentialsError
from src.orbika.commons.conf.aws.conf_data_connection_aws import ConfDataConnectionAws

logger = logging.getLogger(__name__)


class UtilConnectionsAws:
    def __init__(self):
        self.parameters_aws = ConfDataConnectionAws()

    def get_client_aws(self, service):
        try:
            client = boto3.client(
                service_name=self.parameters_aws.get_dates_params(service)['SERVICE_NAME'],
                region_name=self.parameters_aws.get_region_name()
            )
            logger.debug(f'Response From get_client_aws::: {client}')
            return client
        except (BotoCoreError, NoCredentialsError, PartialCredentialsError) as e:
            logger.error(f"Error al conectar con AWS {service}: {e}")
            return None