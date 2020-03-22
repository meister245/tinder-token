# facebookphone auth is based on examples / ideas from the following
# https://github.com/jaebradley/tinder-client/blob/master/src/index.js
# https://github.com/philipperemy/Deep-Learning-Tinder/blob/master/tinder_token.py

import re
import json

import requests
import robobrowser


class TinderTokenFacebookCommon(object):
    TINDER_API_BASE_URL = "https://api.gotinder.com"
    FB_TOKEN_URL = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

    REQ_HEADERS = {
        "user-agent": "Tinder/11.4.0 (iPhone; iOS 12.4.1; Scale/2.00)"
    }

    @classmethod
    def get_facebook_auth_token(cls, email: str, password: str) -> str:
        s = robobrowser.RoboBrowser(user_agent=cls.REQ_HEADERS["user-agent"], parser="html5lib")
        s.open(cls.FB_TOKEN_URL)
        f = s.get_form()
        f["email"], f["pass"] = email, password
        s.submit_form(f)
        f = s.get_form()

        try:
            s.submit_form(f, submit=f.submit_fields["__CONFIRM__"])  # will always raise exception due to URL format

        except requests.exceptions.InvalidSchema as e:
            data = {k: v for k, v in re.findall(r"([\w]+)=([\w\d\-%.]*)", str(e))}

        return data.get("access_token", False)


class TinderTokenFacebookV2(TinderTokenFacebookCommon):
    TINDER_AUTH = TinderTokenFacebookCommon.TINDER_API_BASE_URL + '/v2/auth'
    TINDER_LOGIN = TinderTokenFacebookCommon.TINDER_API_BASE_URL + '/v2/auth/login/facebook'

    @classmethod
    def get_tinder_token(cls, fb_token: str = False, fb_email: str = False, fb_password: str = False):
        fb_token = cls.get_facebook_auth_token(fb_email, fb_password) if not fb_token else fb_token

        payload = {"token": fb_token}
        resp = requests.post(cls.TINDER_LOGIN, json=payload)

        return (
            resp.json().get("data", {}).get("api_token", False),
            resp.json().get("data", {}).get("refresh_token", False)
        )

    @classmethod
    def refresh_token(cls, session: requests.Session, refresh_token: str) -> (str, str):
        payload = {"grant_type": "refresh_token", "refresh_token": refresh_token}
        resp = session.post(cls.TINDER_AUTH, json=payload)

        return (
            resp.json().get("data", {}).get("api_token", False),
            resp.json().get("data", {}).get("refresh_token", False)
        )
