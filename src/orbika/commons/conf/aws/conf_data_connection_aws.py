import os


class ConfDataConnectionAws:

    def __init__(self):
        self.dates = {
            'qa': {
                'REGION_NAME': 'us-east-1',
                'cognito':
                    {
                        'SERVICE_NAME': 'cognito-idp',
                        'USER_POOL_ID': 'us-east-1_PkjXYa5HS'
                    },

                'lambda':
                    {
                        'SERVICE_NAME': 'lambda',
                        'COGNITO': {
                            "LAMBDA_NAME": 'orbika-stg-sec-login-cognito-lambda',
                            'VARIABLES':
                                {
                                    "REAL_URL": 'https://cognito-idp.us-east-1.amazonaws.com/',
                                    "MOCK_URL": 'https://castlemockdemo.subocol.com/castlemock/mock/rest/project/NpJ1A9/application/eu72DD/login'
                                }
                        },
                        'CAPTCHA': {
                            "LAMBDA_NAME": 'orbika-stg-sec-login-captcha-lambda',
                            'VARIABLES':
                                {
                                    "REAL_URL": 'https://www.google.com/recaptcha/api/siteverify',
                                    "MOCK_URL": 'https://castlemockdemo.subocol.com/castlemock/mock/rest/project'
                                                '/NpJ1A9/application/eu72DD/siteverify',
                                    "SECRET_KEY_REAL": '6LfHVhosAAAAAFjg_gAjt0hE_Zka-svT9zvHbMZ3',
                                    "SECRET_KEY_MOCK": '6LfHpXwqAAAAAIi_OMtzYqHx4Sf1DxWBD0CxSec'
                                }

                        }
                    },
                'dynamodb':
                    {
                        "SERVICE_NAME": 'dynamodb',
                        "EVENT_SUCCESS": 'orbika-stg-trace-dynamodb',
                        "EVENT_FAIL": 'orbika-stg-error-dynamodb',
                        'SERVICE_ORDER': 'orbika-stg-service-order-dynamodb',
                        'PROGRESS_ORDER': 'orbika-stg-order-progress-dynamodb',
                        'SERVICE_STATUS': 'orbika-stg-status-service-order-dynamodb',
                        'VEHICLE_BY_PLATE': 'orbika-stg-service-order-vehicle-dynamodb'
                    },
                's3':
                    {
                        "SERVICE_NAME": 's3',
                        "SURA": 'orbika-stg-sura-bucket',
                        "BOLIVAR": 'orbika-stg-bolivar-bucket',
                        "SURA_PANAMA": 'orbika-stg-sura-panama-bucket',
                        "SURA_CHILE": 'orbika-stg-sura-chile-bucket'
                    }
            },
            'dev':
                {
                    'REGION_NAME': 'us-east-1',
                    'cognito': {
                        'SERVICE_NAME': 'cognito-idp',
                        'USER_POOL_ID': 'us-east-1_AHfFOamni'
                    },
                    'lambda':
                        {
                            'SERVICE_NAME': 'lambda',
                            'cognito': {
                                "LAMBDA_NAME": 'orbika-dev-sec-login-cognito-lambda',
                                'VARIABLES':
                                    {
                                        "REAL_URL": 'https://cognito-idp.us-east-1.amazonaws.com/',
                                        "MOCK_URL": 'https://castlemockdemo.subocol.com/castlemock/mock/rest/project/NpJ1A9/application/eu72DD/initiate_auth'
                                    }
                            },
                            'CAPTCHA': {
                                "LAMBDA_NAME": 'orbika-dev-sec-login-captcha-lambda',
                                'VARIABLES':
                                    {
                                        "REAL_URL": 'https://www.google.com/recaptcha/api/siteverify',
                                        "MOCK_URL": 'https://castlemockdemo.subocol.com/castlemock/mock/rest/project'
                                                    '/NpJ1A9/application/eu72DD/siteverify',
                                        "SECRET_KEY_REAL": '6LfHVhosAAAAAFjg_gAjt0hE_Zka-svT9zvHbMZ3',
                                        "SECRET_KEY_MOCK": '6LfHpXwqAAAAAIi_OMtzYqHx4Sf1DxWBD0CxSec'
                                    }

                            }

                        },
                    'dynamodb':
                        {
                            "SERVICE_NAME": 'dynamodb',
                            "EVENT_SUCCESS": 'orbika-dev-trace-dynamodb',
                            "EVENT_FAIL": 'orbika-dev-error-dynamodb',
                            'SERVICE_ORDER': 'orbika-dev-service-order-dynamodb',
                            'PROGRESS_ORDER': 'orbika-dev-order-progress-dynamodb',
                            'SERVICE_STATUS': 'orbika-dev-status-service-order-dynamodb',
                            'VEHICLE_BY_PLATE': 'orbika-dev-service-order-vehicle-dynamodb'
                        },
                    's3':
                        {
                            "SERVICE_NAME": 's3',
                            "SURA": 'orbika-dev-sura-bucket',
                            "BOLIVAR": 'orbika-dev-bolivar-bucket',
                            "SURA_PANAMA": 'orbika-dev-sura-panama-bucket',
                            "SURA_CHILE": 'orbika-dev-sura-chile-bucket'
                        }
                },
            'mock':
                {
                    'REGION_NAME': 'us-east-1',
                    'cognito': {
                        'SERVICE_NAME': 'cognito-idp',
                        'USER_POOL_ID': 'us-east-1_AHfFOamni'
                    },
                    'lambda':
                        {
                            'SERVICE_NAME': 'lambda',
                            'COGNITO': {
                                "LAMBDA_NAME": 'orbika-dev-sec-login-cognito-lambda',
                                'VARIABLES':
                                    {
                                        "REAL_URL": 'https://cognito-idp.us-east-1.amazonaws.com/',
                                        "MOCK_URL": 'https://castlemockdemo.subocol.com/castlemock/mock/rest/project/NpJ1A9/application/eu72DD/login'
                                    }
                            }
                        },
                    'dynamodb':
                        {
                            "SERVICE_NAME": 'dynamodb',
                            "EVENT_SUCCESS": 'orbika-dev-trace-dynamodb',
                            "EVENT_FAIL": 'orbika-dev-error-dynamodb',
                            'SERVICE_ORDER': 'orbika-dev-service-order-dynamodb',
                            'PROGRESS_ORDER': 'orbika-dev-order-progress-dynamodb',
                            'SERVICE_STATUS': 'orbika-dev-status-service-order-dynamodb',
                            "VEHICLE_BY_PLATE": 'orbika-dev-service-order-vehicle-dynamodb'
                        },
                    's3':
                        {
                            "SERVICE_NAME": 's3',
                            "SURA": 'orbika-dev-sura-bucket',
                            "BOLIVAR": 'orbika-dev-bolivar-bucket',
                            "SURA_PANAMA": 'orbika-dev-sura-panama-bucket',
                            "SURA_CHILE": 'orbika-dev-sura-chile-bucket'
                        }
                }
        }

    def get_dates_params(self, service):
        env = os.getenv('ENVIRONMENT')
        return self.dates[env][service]

    def get_region_name(self):
        env = os.getenv('ENVIRONMENT')
        return self.dates[env]['REGION_NAME']
