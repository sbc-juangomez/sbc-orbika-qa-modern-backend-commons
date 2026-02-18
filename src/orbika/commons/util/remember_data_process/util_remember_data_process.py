class UtilRememberDataProcess:
    __code = None
    __body = None
    __response = None
    __response_status_code = None
    __transaction_id = None
    __cognito_id_user = None
    __scenario = None
    __email = None
    __session_id = None
    __email_header = None
    __session_id_header = None
    __insurer_id = None
    __country_id = None
    __regional_id = None
    __department_id = None
    __city_id = None
    __last_sent_limit = None
    __status_orders = None
    __service_order_id = None
    __role_id = None
    __permission_id_user = None
    __permission_id = None
    __permission_detail_id = None
    __vehicle_type_id = None
    __plate = None
    __pieces = None
    __step = None
    __process = None
    __trace = None
    __files = None
    __response_details_true = None
    __response_details_false = None
    __service_order_status_id = None
    __type_operation_id = None
    __data_history = None
    __challenge_name = None
    __session_token = None
    __application_client_id = None
    __client_id = None
    __user_id = None
    __application_id = None
    __workshop_id = None

    @classmethod
    def set_history(cls, data_history):
        cls.__data_history = data_history

    @classmethod
    def get_history(cls):
        return cls.__data_history

    @classmethod
    def reset_history(cls):
        cls.__data_history = None

    @classmethod
    def set_code(cls, code):
        cls.__code = code

    @classmethod
    def get_code(cls):
        return cls.__code

    @classmethod
    def set_body(cls, body):
        cls.__body = body

    @classmethod
    def get_body(cls):
        return cls.__body

    @classmethod
    def reset_body(cls):
        cls.__body = None

    @classmethod
    def set_response(cls, response):
        cls.__response = response

    @classmethod
    def get_response(cls):
        return cls.__response

    @classmethod
    def reset_response(cls):
        cls.__response = None

    @classmethod
    def set_response_status_code(cls, response_status_code):
        cls.__response_status_code = response_status_code

    @classmethod
    def get_response_status_code(cls):
        return cls.__response_status_code

    @classmethod
    def reset_response_status_code(cls):
        cls.__response_status_code = None

    @classmethod
    def set_transaction_id(cls, transaction_id):
        cls.__transaction_id = transaction_id

    @classmethod
    def set_user_id(cls, user_id):
        cls.__user_id = user_id

    @classmethod
    def reset_user_id(cls):
        cls.__user_id = None

    @classmethod
    def get_user_id(cls):
        return cls.__user_id

    @classmethod
    def get_transaction_id(cls):
        return cls.__transaction_id

    @classmethod
    def resert_transaction_id(cls):
        cls.__transaction_id = None

    @classmethod
    def set_cognito_id_user(cls, cognito_id_user):
        cls.__cognito_id_user = cognito_id_user

    @classmethod
    def get_cognito_id_user(cls):
        return cls.__cognito_id_user

    @classmethod
    def set_scenario(cls, scenario):
        cls.__scenario = scenario

    @classmethod
    def get_scenario(cls):
        return cls.__scenario

    @classmethod
    def set_email(cls, email):
        cls.__email = email

    @classmethod
    def get_email(cls):
        return cls.__email

    @classmethod
    def reset_email(cls):
        cls.__email = None

    @classmethod
    def set_session_id(cls, session_id):
        cls.__session_id = session_id

    @classmethod
    def get_session_id(cls):
        return cls.__session_id

    @classmethod
    def set_refresh_token(cls, refresh_token):
        cls.__refresh_token = refresh_token

    @classmethod
    def get_refresh_token(cls):
        return cls.__refresh_token

    @classmethod
    def reset_refresh_token(cls):
        cls.__refresh_token = None

    @classmethod
    def set_email_header(cls, email_header):
        cls.__email_header = email_header

    @classmethod
    def get_email_header(cls):
        return cls.__email_header

    @classmethod
    def reset_email_header(cls):
        cls.__email_header = None

    @classmethod
    def set_session_id_header(cls, session_id_header):
        cls.__session_id_header = session_id_header

    @classmethod
    def get_session_id_header(cls):
        return cls.__session_id_header

    @classmethod
    def set_insurer_id(cls, insurer_id):
        cls.__insurer_id = insurer_id

    @classmethod
    def get_insurer_id(cls):
        return cls.__insurer_id

    @classmethod
    def reset_insurer_id(cls):
        cls.__insurer_id = None

    @classmethod
    def set_country_id(cls, country_id):
        cls.__country_id = country_id

    @classmethod
    def get_country_id(cls):
        return cls.__country_id

    @classmethod
    def reset_country_id(cls):
        cls.__country_id = None

    @classmethod
    def set_regional_id(cls, regional_id):
        cls.__regional_id = regional_id

    @classmethod
    def get_regional_id(cls):
        return cls.__regional_id

    @classmethod
    def reset_regional_id(cls):
        cls.__regional_id = None

    @classmethod
    def set_department_id(cls, department_id):
        cls.__department_id = department_id

    @classmethod
    def get_department_id(cls):
        return cls.__department_id

    @classmethod
    def reset_department_id(cls):
        cls.__department_id = None

    @classmethod
    def set_city_id(cls, city_id):
        cls.__city_id = city_id

    @classmethod
    def get_city_id(cls):
        return cls.__city_id

    @classmethod
    def reset_city_id(cls):
        cls.__city_id = None

    @classmethod
    def set_permission_id(cls, permission_id):
        cls.__permission_id = permission_id

    @classmethod
    def get_permission_id(cls):
        return cls.__permission_id

    @classmethod
    def reset_permission_id(cls):
        cls.__permission_id = None

    @classmethod
    def set_permission_details_id(cls, permission_detail_id):
        cls.__permission_detail_id = permission_detail_id

    @classmethod
    def get_permission_details_id(cls):
        return cls.__permission_detail_id

    @classmethod
    def reset_permission_details_id(cls):
        cls.__permission_detail_id = None

    @classmethod
    def set_permission_detail_id(cls, permission_detail_id):
        cls.__permission_detail_id = permission_detail_id

    @classmethod
    def get_permission_detail_id(cls):
        return cls.__permission_detail_id

    @classmethod
    def reset_permission_detail_id(cls):
        cls.__permission_detail_id = None

    @classmethod
    def get_status_orders(cls):
        return cls.__status_orders

    @classmethod
    def set_status_orders(cls, statu_orders):
        cls.__status_orders = statu_orders

    @classmethod
    def reset_status_orders(cls):
        cls.__status_orders = None

    @classmethod
    def get_service_order_id(cls):
        return cls.__service_order_id

    @classmethod
    def set_service_order_id(cls, service_order_id):
        cls.__service_order_id = service_order_id

    @classmethod
    def reset_service_order_id(cls):
        cls.__service_order_id = None

    @classmethod
    def set_last_sent_limit(cls, last_sent_limit):
        cls.__last_sent_limit = last_sent_limit

    @classmethod
    def get_last_sent_limit(cls):
        return cls.__last_sent_limit

    @classmethod
    def reset_last_sent_limit(cls):
        cls.__last_sent_limit = None

    @classmethod
    def set_permission_id_user(cls, permission_id_use):
        cls.__permission_id_user = permission_id_use

    @classmethod
    def get_permission_id_user(cls):
        return cls.__permission_id_user

    @classmethod
    def reset_permission_id_user(cls):
        cls.__permission_id_user = None

    @classmethod
    def get_role_id(cls):
        return cls.__role_id

    @classmethod
    def set_role_id(cls, role_id):
        cls.__role_id = role_id

    @classmethod
    def reset_role_id(cls):
        cls.__role_id = None

    @classmethod
    def get_vehicle_type_id(cls):
        return cls.__vehicle_type_id

    @classmethod
    def set_vehicle_type_id(cls, vehicle_type_id):
        cls.__vehicle_type_id = vehicle_type_id

    @classmethod
    def reset_vehicle_type_id(cls):
        cls.__vehicle_type_id = None

    @classmethod
    def set_plate(cls, plate):
        cls.__plate = plate

    @classmethod
    def get_plate(cls):
        return cls.__plate

    @classmethod
    def reset_plate(cls):
        cls.__plate = None

    @classmethod
    def set_pieces(cls, pieces):
        cls.__pieces = pieces

    @classmethod
    def get_pieces(cls):
        return cls.__pieces

    @classmethod
    def reset_pieces(cls):
        cls.__pieces = None

    @classmethod
    def set_step(cls, step):
        cls.__step = step

    @classmethod
    def get_step(cls):
        return cls.__step

    @classmethod
    def reset_step(cls):
        cls.__step = None

    # add method Process

    @classmethod
    def set_process(cls, process):
        cls.__process = process

    @classmethod
    def get_process(cls):
        return cls.__process

    @classmethod
    def reset_process(cls):
        cls.__process = None

    @classmethod
    def set_trace(cls, trace):
        cls.__trace = trace

    @classmethod
    def get_trace(cls):
        return cls.__trace

    @classmethod
    def reset_trace(cls):
        cls.__trace = None

    @classmethod
    def set_files(cls, files):
        cls.__files = files

    @classmethod
    def get_files(cls):
        return cls.__files

    @classmethod
    def reset_files(cls):
        cls.__files = None

    @classmethod
    def set_response_details_true(cls, response_details_true):
        cls.__response_details_true = response_details_true

    @classmethod
    def get_response_details_true(cls):
        return cls.__response_details_true

    @classmethod
    def reset_response_details_true(cls):
        cls.__response_details_true = None

    @classmethod
    def set_response_details_false(cls, response_details_false):
        cls.__response_details_false = response_details_false

    @classmethod
    def get_response_details_false(cls):
        return cls.__response_details_false

    @classmethod
    def reset_response_details_false(cls):
        cls.__response_details_false = None

    @classmethod
    def get_service_order_status_id(cls):
        return cls.__service_order_status_id

    @classmethod
    def set_service_order_status_id(cls, service_order_status_id):
        cls.__service_order_status_id = service_order_status_id

    @classmethod
    def reset_service_order_status_id(cls):
        cls.__service_order_status_id = None

    @classmethod
    def get_type_operation_id(cls):
        return cls.__type_operation_id

    @classmethod
    def set_type_operation_id(cls, type_operation_id):
        cls.__type_operation_id = type_operation_id

    @classmethod
    def reset_type_operation_id(cls):
        cls.__type_operation_id = None

    @classmethod
    def set_challenge_name(cls, challenge_name):
        cls.__challenge_name = challenge_name

    @classmethod
    def get_challenge_name(cls):
        return cls.__challenge_name

    @classmethod
    def reset_challenge_name(cls):
        cls.__challenge_name = None

    @classmethod
    def set_session_token(cls, session_token):
        cls.__session_token = session_token

    @classmethod
    def get_session_token(cls):
        return cls.__session_token

    @classmethod
    def reset_session_token(cls):
        cls.__session_token = None

    @classmethod
    def set_application_client_id(cls, application_client_id):
        cls.__application_client_id = application_client_id

    @classmethod
    def get_application_client_id(cls):
        return cls.__application_client_id

    @classmethod
    def reset_application_client_id(cls):
        cls.__application_client_id = None

    @classmethod
    def set_client_id(cls, client_id):
        cls.__client_id = client_id

    @classmethod
    def get_client_id(cls):
        return cls.__client_id

    @classmethod
    def reset_client_id(cls):
        cls.__client_id = None

    @classmethod
    def set_application_id(cls, application_id):
        cls.__application_id = application_id

    @classmethod
    def get_application_id(cls):
        return cls.__application_id

    @classmethod
    def reset_application_id(cls):
        cls.__application_id = None

    @classmethod
    def set_workshop_id(cls, workshop_id):
        cls.__workshop_id = workshop_id

    @classmethod
    def get_workshop_id(cls):
        return cls.__workshop_id

    @classmethod
    def reset_workshop_id(cls):
        cls.__workshop_id = None