class DataSecGetPermissions:
    JSON = [
        {
            "scenario": 'data_sec_get_permissions_12082_sec_get_permissions_user_not_in_database',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001a",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001a",
                    "email": "emailnotindatabase@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                        "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_get_permissions_12084_sec_get_permissions_user_not_clients',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001a",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001a",
                    "email": "andresmejia@gmail.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                            "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_get_permissions_12086_sec_get_permissions_user_client_not_apps',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001a",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001a",
                    "email": "emailnotindatabase@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                        "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_get_permissions_12082_sec_get_permissions_user_not_in_database',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001a",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001a",
                    "email": "emailnotindatabase@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                        "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_get_permissions_12087_sec_get_permissions_user_client_app_not_rol',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001a",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001a",
                    "email": "emailnotindatabase@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                        "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_get_permissions_12090_sec_get_permissions_user_rol_without_permissions',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001a",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001a",
                    "email": "sebastiantorres@gmail.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                        "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        }
    ]