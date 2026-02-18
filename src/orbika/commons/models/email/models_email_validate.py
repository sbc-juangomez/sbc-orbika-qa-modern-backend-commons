class ModelsEmailValidate:
    __email = None
    __status_code = None
    __response = None
    __transaction_id = None
    __session_id = None
    __expected_email = None

    def __init__(self, email, status_code, response, transaction_id, session_id, expected_email):
        self.__email = email
        self.__status_code = status_code
        self.__response = response
        self.__transaction_id = transaction_id
        self.__session_id = session_id
        self.__expected_email = expected_email

    def get_response_data_email(self):
        return {'email': self.__email,
                'status_code': self.__status_code,
                'response': self.__response,
                'transaction_id': self.__transaction_id,
                'session_id': self.__session_id,
                'expected_email': self.__expected_email,
                }

    @staticmethod
    def get_response_data_email_error(email, transaction_id, session_id, expected):
        return {'email': email,
                'status_code': 500,
                'response': {"error": "Error al realizar la solicitud"},
                'transaction_id': transaction_id,
                'session_id': session_id,
                'expected_email': expected
                }
