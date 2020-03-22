# tinder-token

Python library for generating access tokens for using Tinder API, using Facebook or Phone authentication.

## Quick Start

Install the package:

    pip install tinder-token

If you want to use Facebook authentication, install with the following:

    pip install tinder-token[facebook]

### API - Facebook

The `facebook.get_tinder_token` function will return a tuple, which contains the tinder token and refresh token.

    from tinder_token.facebook import TinderTokenFacebookV2

    facebook = TinderTokenFacebookV2()

    def sample_email_password(email: str, password: str) -> (str, str):
        return facebook.get_tinder_token(fb_email=email, fb_password=password)

    def sample_facebook_token(fb_token: str) -> (str, str):
        return facebook.get_tinder_token(fb_token=fb_token)

### API - Phone

    from tinder_token.phone import TinderTokenPhoneV2

    phone = TinderTokenPhoneV2()

    def sample_phone(phone_number: str) -> str:
        phone.send_otp_code(phone_number)
        otp_code = input('code: ')

        refresh_token = phone.get_refresh_token(otp_code, phone_number)
        return phone.get_tinder_token(refresh_token)

### CLI Script

A sample script is installed with the package.
Follow the prompts in order to retrieve your access token.

    ./tinder-token
