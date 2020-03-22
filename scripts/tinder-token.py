#!/usr/bin/env python3

import re
import sys
import getpass

import requests


def main():
    requests.urllib3.disable_warnings()
    auth_type = input(f'choose authentication [facebook/phone]: ')

    if auth_type == 'facebook':
        from tinder_token.facebook import TinderTokenFacebookV2

        facebook = TinderTokenFacebookV2()
        fb_email = input('facebook email: ')
        fb_password = getpass.getpass('facebook password: ')

        token, refresh_token = facebook.get_tinder_token(fb_email=fb_email, fb_password=fb_password)

    elif auth_type == 'phone':
        from tinder_token.phone import TinderTokenPhoneV2

        phone = TinderTokenPhoneV2()
        phone_number = input('enter phone number [country_code + phone_number]: ')
        phone_number = re.sub('[^0-9]', '', phone_number)

        phone.send_otp_code(phone_number)
        otp_code = input('enter received code: ')
        otp_code = re.sub('[^0-9]', '', otp_code)

        refresh_token = phone.get_refresh_token(otp_code, phone_number)
        token = phone.get_tinder_token(refresh_token)

    else:
        exit(f'invalid value "{auth_type}"')

    print(f'your access token - {token}')


if __name__ == "__main__":
    main()
