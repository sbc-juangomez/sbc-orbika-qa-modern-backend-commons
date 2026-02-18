class DataSecLoginUserService:
    JSON = [
        {
            "scenario": 'data_sec_login_user_service_12041_invalid_credentials',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "jsebastiangomez2@poligran.edu.co",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "56d7ba53d789598766dd3e768c1fb25a525fc0b8"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12042_password_change_required',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "fernandadiaz869@gmail.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "123360000"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12043_user_not_found',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "cognitousuarionoregistrado@subocol.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "123360000"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12044_user_disabled',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "jadib88312@anypng.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "56d7ba53d789598766dd3e768c1fb25a525fc0b8"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12045_attempts_exceeded',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "wilmanguerra@subocol.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12048_password_temporal_expired',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "fernandadiaz869@gmail.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12051_user_not_in_database',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "jsebastiangomez2@poligran.edu.co",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12052_user_inactive',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "l-g-r-c1@hotmail.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_login_user_service_12053_cognito_id_mismatch',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "adrianmorales@subocol.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        }
    ]