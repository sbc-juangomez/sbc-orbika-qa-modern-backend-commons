class ModelsHeadersValidate:
    __scenario = None
    __status_code = None
    __response = None
    __transaction_id = None
    __session_id = None
    __expects = None
    __email = None
    __insurer_id = None

    def __init__(self, scenario, status_code, response, transaction_id, session_id, expects, email, insurer_id):
        self.__scenario = scenario
        self.__status_code = status_code
        self.__response = response
        self.__transaction_id = transaction_id
        self.__session_id = session_id
        self.__expects = expects
        self.__email = email
        self.__insurer_id = insurer_id

    def get_response_data_headers(self):
        return {'scenario': self.__scenario,
                'status_code': self.__status_code,
                'response': self.__response,
                'transaction_id': self.__transaction_id,
                'session_id': self.__session_id,
                'expects': self.__expects,
                'email': self.__email,
                'insurer_id': self.__insurer_id
                }

    @staticmethod
    def get_response_data_headers_error(scenario, transaction_id, session_id, expects, email, insurer_id):
        return {'scenario': scenario,
                'status_code': 500,
                'response': {"error": "Error al realizar la solicitud"},
                'transaction_id': transaction_id,
                'session_id': session_id,
                'expects': expects,
                'email': email,
                'insurer_id': insurer_id
                }
