class DataSecUserAuthMfa:
    JSON = [
        {
            "scenario": 'data_sec_user_auth_mfa_12060_session_success',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001b",
                    "email": "danielarios@gmail.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6002b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a002b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "sessions": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6003b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a003b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6003b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a303b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": ""
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_data_type_int',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6004b",
                    "transaction_id": "0199a035-a89a-720f-88c1-957777d6005b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": 232323
                    }
                }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_data_type_float',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6005b",
                    "transaction_id": "0199a035-a89a-720f-88c1-957777d6005b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": 23.2323
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_code_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6012b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a012b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_code_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6011b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a011b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "codes": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_code_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6111b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a111b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_code_min_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6013b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a013b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "32506",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_code_max_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6014b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a014b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "3250600",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_code_data_type_int',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6015b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a015b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": 325060,
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_code_data_type_float',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6016b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a016b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": 3250.6,
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6017b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a017b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6018b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a018b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_names": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6117b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a017b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
            {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_data_type_int',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6020b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a017b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": 1234331,
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
                }
            },
                {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_data_type_float',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6020b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a017b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": 1.32,
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
            },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_invalid_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6020b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a017b",
                    "email": "juangomez@subocol.com",
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "INVALID_CHALLENGE",
                     "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
            },
            {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_min_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6020b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a017b",
                      "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
            },
                {
            "scenario": 'data_sec_user_auth_mfa_12061_challenge_name_max_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6020b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a017b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA_SOFTWARE_TOKEN_MFA_SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
            },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_is_required',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6020b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a020b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "sessions": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
            },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_not_exist',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6021b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a021b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                }
            }
         },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_is_empty',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6120b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a120b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": ""
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_min_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6022b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a022b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlQ29nbml0b1VzZXJQb29sc19rTXMyMDI1LTAx"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_max_value',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6023b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a023b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlQ29nbml0b1VzZXJQb29sc19rTXMyMDI1X0xvbmdUb2tlbl9BYWJjREVGR0hJSktMTU5PUFFSU1RVVldYWVphYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejAxMjM0NTY3ODlhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ekFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaYWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXowMTIzNDU2Nzg5YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eg=="
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_data_type_int',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6024b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a024b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": 7359201847365921
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_session_data_type_float',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6025b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a025b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": 3.5920184736592047
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12061_email_validate_massive',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6001b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a001b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": "data_sec_user_auth_mfa_12061_all_headers_validate",
            "data": {
                "headers": {},
                "body": {
                    "password": "74ba283db845f1685b0c90101a19c0170167aeb8"

                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12060_session_success_without_clients',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6032b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a032b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12060_session_success_client_without_apps',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6033b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a033b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        },
        {
            "scenario": 'data_sec_user_auth_mfa_12060_session_success_clients_without_apps',
            "data": {
                "headers": {
                    "session_id": "0199a035-a89a-720f-88c1-957777d6034b",
                    "transaction_id": "0199a035-d09f-774c-9dec-2e9c974a034b",
                    "email": "juangomez@subocol.com"
                },
                "body": {
                    "code": "325060",
                    "challenge_name": "SOFTWARE_TOKEN_MFA",
                    "session": "AYABeDB9Y307VqRrBwOh6CVU6fwAHQABAAdTZXJ2aWNlABBDb2duaXRvVXNlclBvb2xzAAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3NDU2MjM0Njc1NTU6a2V5L2IxNTVhZmNhLWJmMjktNGVlZC1hZmQ4LWE5ZTA5MzY1M2RiZQC4AQIBAHhR9E4zNbI1ofi3Y01_Ljgh2wK-ZaC__bKufjbgmejy4gFSD_6rjaUWQSqZQIMBgjC1AAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMVQpmRPN1GkGY4ERYAgEQgDvpJ2fJ_ErhRAT6uThIMYPUW907uVUpJpaKphVaixGKZ9cmE3Hy4WN8cm-H6STxflyNoTasc18ABuQNmwIAAAAADAAAEAAAAAAAAAAAAAAAAAAzO6YYiomX3LoBKBpXSKaI_____wAAAAEAAAAAAAAAAAAAAAEAAAEfETVk6ftIrxTHrV0m7LrmJc_uF8PqUXayJZBXXAHhDWIgzRQAMadnSMBJJ5LvzwM_eUsxwieqWlvEdx6XR8Z_cDNSjcz2LDgRI6ZtuNKw0sQvszaLdE2yzyoRK32-LiQXOp4HoawDTJu6c1XMRKISQgTx-kyOZGy4gRRdKXrR1HrehgB1yXtqjRnl2Fb_48iZvTo_oUCXphJAcKiqcQLA0RTEXT2SafZpYOGZ4RXpl8S3QxPHxnQnIHT7sqvxG5gFHV0TXRgqWldkwPoM5URAdNsULVTTDPVbmHEtG0_coOi-Cu0kUDo0-q6POQaS94Rw_S0IRKdmNcjusS9DxqyAsLZiCu_QL46LuFD9uYJNAvePfRwpr3OJs7IOo-mBiaqrlCLRziMTHBEO4j6-FkOi"
                }
            }
        }
    ]