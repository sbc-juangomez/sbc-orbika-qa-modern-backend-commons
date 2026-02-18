class DataSecValidateLoginService:
    JSON = [
        {
            "scenario": 'data_sec_validate_login_service_12020_session_success_mfa',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60501",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "julianahernandez@gmail.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12020_session_success_software',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60101",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "danielarios@gmail.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12020_password_change_required_success',
            "data": {
                "headers": {
                    "session_id": "ca45aa1c-118e-42f6-b9c5-bc9382-123456",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "pruebascrearusuario@test.com",
                    "token_recaptcha": "03AGdBq24D1MLP7hdEJvHb2PxyzZxTu7hx4m-A7xNU7lABR-yC83NAxZONPkp"
                },
                "body": {
                    "password": "56d7ba53d789598766dd3e768c1fb25a525fc0b9"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12020_session_success',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60201",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": "data_sec_validate_login_service_12021_session_id_not_exist",
            "data": {
                "headers": {
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae302",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_session_id_required',
            "data": {
                "headers": {
                    "session_ids": "0199a035-a89a-720f-88c1-957777d60502",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae302",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_session_id_is_empty',
            "data": {
                "headers": {
                    "session_id": "",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae102",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_session_id_invalid_format',
            "data": {
                "headers": {
                    "session_id": "INVALID-FORMAT",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae303",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_validate_massive',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60502",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae303",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_min_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60504",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae304",
                    "email": "@.co",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_max_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60505",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae305",
                    "email": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@example.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_data_type_int',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60506",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae306",
                    "email": 12345,
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_data_type_float',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60506",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae306",
                    "email": 1234.56,
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60507",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae307",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60507",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae307",
                    "emails": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_email_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d67507",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae307",
                    "email": "",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_password_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60508",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae308",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {

                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_password_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60508",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae308",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "passwords": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_password_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60508",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae308",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": ""
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_password_min_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60509",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae309",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_password_max_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60510",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae310",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb80"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_password_data_type_int',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60511",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae311",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": 12345678
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_password_data_type_float',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60511",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae311",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": 1234567.89
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_transaction_id_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60512",
                    "transaction_ids": "0199a035-d09f-774c-9dec-2e9c974ae312",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_transaction_id_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60512",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_transaction_id_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d67512",
                    "transaction_id": "",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_transaction_id_invalid_format',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60513",
                    "transaction_id": "INVALID-FORMAT",
                    "email": "juangomez@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_token_recaptcha_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6053b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae315",
                    "email": "fernandadiaz869@gmail.com",
                    "token_recaptchas": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_token_recaptcha_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6053b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae315",
                    "email": "fernandadiaz869@gmail.com"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_token_recaptcha_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6053b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae315",
                    "email": "fernandadiaz869@gmail.com",
                    "token_recaptcha": ""
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_token_recaptcha_min_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6053b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae315",
                    "email": "fernandadiaz869@gmail.com",
                    "token_recaptcha": "0cAFcWeA4"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12021_token_recaptcha_max_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6053b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae315",
                    "email": "fernandadiaz869@gmail.com",
                    "token_recaptcha": "ey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL098765432_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL0987654321MnbVcxZ_aSqWeRtYuiOpLkJhGfDsA1234567890-_BnMey7JhG89sK12LzXcVbN3mQwErTyUiOp456AsDfGhJkL098765432"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }

            }
        },
        {
            "scenario": "data_sec_validate_login_service_12021_all_headers_validate",
            "data": {
                "headers": {},
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"

                }
            }
        },
        {
            "scenario": "data_sec_validate_login_service_12021_headers_validate_massive",
            "data": {
                "headers": {
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12060_session_success_client_case_a',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60501",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "tobiasalejandrodiaz@gmail.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12060_session_success_client_case_b',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60501",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "saradiaz@gmail.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12060_session_success_client_case_d',

            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60501",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "usuariovariasaseguradoraspordefault@gmail.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        },
        {
            "scenario": 'data_sec_validate_login_service_12060_session_success_client_case_f',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d60501",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974ae301",
                    "email": "noaseguradoradefecto@subocol.com",
                    "token_recaptcha": "0cAFcWeA4jzvg0n8N_aOjZo3__osblSc"
                },
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"
                }
            }
        }
    ]
