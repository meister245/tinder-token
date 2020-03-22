# phone auth is based on examples / ideas from the following
# https://github.com/fbessez/Tinder/blob/faa8459aae8165758aa2d6f055f037130a9bbbe1/phone_auth_token.py

import requests


class TinderTokenPhoneCommon(object):
    TINDER_API_BASE_URL = "https://api.gotinder.com"
    FB_TOKEN_URL = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

    REQ_HEADERS = {
        "user-agent": "Tinder/11.4.0 (iPhone; iOS 12.4.1; Scale/2.00)"
    }


class TinderTokenPhoneV2(TinderTokenPhoneCommon):
    PHONE_TOKEN_URL = TinderTokenPhoneCommon.TINDER_API_BASE_URL + "/v2/auth/login/sms"
    CODE_REQUEST_URL = TinderTokenPhoneCommon.TINDER_API_BASE_URL + "/v2/auth/sms/send?auth_type=sms"
    CODE_VALIDATE_URL = TinderTokenPhoneCommon.TINDER_API_BASE_URL + "/v2/auth/sms/validate?auth_type=sms"

    @classmethod
    def get_tinder_token(cls, refresh_token: str):
        payload = {"refresh_token": refresh_token}

        resp = requests.post(
            cls.PHONE_TOKEN_URL,
            headers=cls.REQ_HEADERS,
            json=payload,
            verify=False,
        )

        return resp.json().get("data", {}).get("api_token", False)

    @classmethod
    def get_refresh_token(cls, otp_code: str, phone_number: str):
        payload = {'otp_code': otp_code, 'phone_number': phone_number}

        resp = requests.post(
            cls.CODE_VALIDATE_URL,
            headers=cls.REQ_HEADERS,
            json=payload,
            verify=False,
        )

        return resp.json().get("data", {}).get("refresh_token", False)

    @classmethod
    def send_otp_code(cls, phone_number: str):
        payload = {"phone_number": phone_number}

        resp = requests.post(
            cls.CODE_REQUEST_URL,
            headers=cls.REQ_HEADERS,
            json=payload,
            verify=False,
        )

        return resp.json().get("data", {}).get("sms_sent", False)
