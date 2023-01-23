import os
import pyotp
import base64
from datetime import datetime
from kavenegar import KavenegarAPI, APIException, HTTPException

# Time after which OTP will expire
EXPIRY_TIME = 300  # seconds


class generateKey:
    '''
        This class returns the string needed to generate the key
    '''

    @staticmethod
    def returnValue(phone) -> str:
        return str(phone) + str(datetime.date(datetime.now())) + os.getenv('OTP_SECRET_KEY')


def create_OTP(phone):
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
    return pyotp.TOTP(key, interval=EXPIRY_TIME)  # TOTP Model for OTP is created


def send_otp_sms(OTP, phone) -> bool:
    try:
        api = KavenegarAPI(os.getenv('SMS_API_KEY'))
        params = {
            'receptor': f"{phone}",
            'template': f"{os.getenv('SMS_TEMPLATE')}",
            'token': f"{OTP.now()}",
            'type': 'sms',
        }
        response = api.verify_lookup(params)

        return True
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

    return False
