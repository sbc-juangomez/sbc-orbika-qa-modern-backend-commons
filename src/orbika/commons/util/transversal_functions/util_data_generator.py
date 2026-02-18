import uuid

import pyotp


class UtilDataGenerator:

    @staticmethod
    def generate_code_mfa(mfa_secret):
        totp = pyotp.TOTP(mfa_secret)
        tot_code = totp.now()
        return tot_code

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())