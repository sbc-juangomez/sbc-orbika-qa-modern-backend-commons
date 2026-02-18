import os
import logging

logger = logging.getLogger(__name__)


class ConfLogin:

    HOSTS = {
        "mock": "https://wiremock.subocol.com",
        "dev": "https://jmsxbmk551.execute-api.us-east-1.amazonaws.com",
        "qa": "https://p01gg8jr59.execute-api.us-east-1.amazonaws.com"
    }

    # Endpoints por ambiente
    SERVICES = {
        "mock": {
            "sec-login-user-service": "/api/sec-login-user-service",
            "sec-validate-login-service": "/api/sec-validate-login-service",
            "sec-user-auth-mfa": "/api/sec-user-auth-mfa",
            "sec-get-permissions": "/api/sec-get-permissions",
            "sec-associate-fotware-token": "/api/sec-associate-fotware-token"
        },
        "dev": {
            "sec-login-user-service": "/dev/sec-validate-login-service",
            "sec-validate-login-service": "/dev/sec-validate-login-service",
            "sec-user-auth-mfa": "/dev/sec-user-auth-mfa",
            "sec-get-permissions": "/dev/sec-validate-login-service",
            "sec-associate-fotware-token": "/dev/sec-associate-fotware-token"
        },
        "qa": {
            "sec-login-user-service": "/stg/sec-validate-login-service",
            "sec-validate-login-service": "/stg/sec-validate-login-service",
            "sec-user-auth-mfa": "/stg/sec-user-auth-mfa",
            "sec-get-permissions": "/stg/sec-validate-login-service",
            "sec-associate-fotware-token": "/stg/sec-associate-fotware-token"
        }
    }


    @staticmethod
    def get_url(service_name):

        env = os.getenv('ENVIRONMENT')
        host = ConfLogin.HOSTS.get(env)
        service_path = ConfLogin.SERVICES.get(env, {}).get(service_name)

        if not host:
            logger.error(f"Ambiente '{env}' no configurado en ConfLogin.HOSTS.")
            raise ValueError(f"Ambiente '{env}' no configurado.")
        if not service_path:
            logger.error(f"Servicio '{service_name}' no encontrado en el ambiente '{env}'.")
            raise ValueError(f"Servicio '{service_name}' no configurado en ambiente '{env}'.")

        full_url = f"{host}{service_path}"

        logger.info(f"[ConfLogin] Ambiente: {env.upper()} | Servicio: {service_name} | URL: {full_url}")
        return full_url

