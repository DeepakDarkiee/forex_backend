from django.conf import settings
from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    # @staticmethod
    def validate(self, auth_token):
        try:
            CLIENT_ID = settings.GOOGLE_CLIENT_ID
            idinfo = id_token.verify_oauth2_token(
                auth_token, requests.Request(), CLIENT_ID
            )

            if "accounts.google.com" in idinfo["iss"]:
                if idinfo["email_verified"]:
                    return idinfo
                return "Please verify your email account."
            else:
                return "Please login with your gmail account."
        except:
            return "The token is either invalid or expired."
