import os


class ConfDataConnection:

    def __init__(self):
        self.databases = {
            "orbika-db": {
                "qa": {
                    "HOST": 'orbika-stg-postgresql-rds.cluster-ceu4bmvstsik.us-east-1.rds.amazonaws.com',
                    "PORT": '5432',
                    "DATABASE": 'orbika-db',
                    "USERNAME": 'fernandadiaz',
                    "PASSWORD": '9B08J$b83>85'
                },
                "dev": {
                    "HOST": 'orbika-dev-postgresql-rds.cluster-cwzszzfd0zrf.us-east-1.rds.amazonaws.com',
                    "PORT": '5432',
                    "DATABASE": 'orbika-db',
                    "USERNAME": 'fernandadiaz',
                    "PASSWORD": '4Md86FwK3@Tw'
                }

            },
            "suite-db": {
                "qa": {
                    "HOST": 'orbika-stg-suite-postgresql-rds.cluster-ceu4bmvstsik.us-east-1.rds.amazonaws.com',
                    "PORT": '5432',
                    "DATABASE": 'suite-db',
                    "USERNAME": 'luisrodriguez',
                    "PASSWORD": '9?x54C9JciF<'
                },
                "dev": {
                    "HOST": 'orbika-dev-suite-postgresql-rds.cluster-cwzszzfd0zrf.us-east-1.rds.amazonaws.com',
                    "PORT": '5432',
                    "DATABASE": 'suite-db',
                    "USERNAME": 'conexionqa',
                    "PASSWORD": '1d34(603MKPb'
                }

            }
        }

    def get_connection_params(self, db_identifier):
        env = os.getenv('ENVIRONMENT')
        if env == 'mock':
            env = 'dev'
        return self.databases[db_identifier][env]
