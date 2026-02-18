class DataSecAssociateFotwareToken:
    JSON = [
        {
            "scenario": 'data_sec_associate_fotware_token_12120_session_token_success',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60501",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "danielarios@gmail.com"
                },
                "body": {
                    "session_token": "eyJjdHkiOiJKV1QiL..."
                }
            }
        },
        {
            "scenario": 'data_sec_associate_fotware_token_12121_session_token_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6002b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a002b",
                    "email": "danielarios@gmail.com"
                },
                "body": {
                }
            }
        },
        {
            "scenario": 'data_sec_associate_fotware_token_12121_session_token_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6003b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a003b",
                    "email": "danielarios@gmail.com"
                },
                "body": {
                    "session_tokens": "eyJjdHkiOiJKV1QiL..."
                }
            }
        },
        {
            "scenario": 'data_sec_associate_fotware_token_12121_session_token_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6004b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a004b",
                    "email": "danielarios@gmail.com"
                },
                "body": {
                    "session_token": ""
                }
            }
        },
        {
            "scenario": 'data_sec_associate_fotware_token_12121_session_token_data_type_int',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6005b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a005b",
                    "email": "danielarios@gmail.com"
                },
                "body": {
                    "session_token": 123456789
                }
            }
        },
        {
            "scenario": 'data_sec_associate_fotware_token_12121_session_token_data_type_float',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6006b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a006b",
                    "email": "danielarios@gmail.com"
                },
                "body": {
                    "session_token": 123.456
                }
            }
        },
        {
            "scenario": 'data_sec_associate_fotware_token_12121_headers_validate_massive',
            "data": {
                "headers": {},
                "body": {
                    "session_token": "eyJjdHkiOiJKV1QiL..."
                }
            }
        }
    ]

