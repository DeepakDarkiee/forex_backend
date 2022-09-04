from accounts.models import User
from django.contrib.auth import authenticate


class Validator:
    @staticmethod
    def is_valid_user(email, password):
        try:
            user = authenticate(email=email, password=password)
            print(user)
            return True, "Ok", user

            if not user:
                return False, "Invalid credentials, please try again.", None

            if not user.is_verified:
                return False, "phone is not verified", None

            if not user.is_active:
                return False, "Account disabled, contact admin", None

        except Exception as e:
            message = f"{e}"
            return False, message, None

    @staticmethod
    def is_contact_already_exists(contact):
        result, message = False, "Contact number already exists!"
        try:
            if not User.objects.filter(contact=contact).exists():
                result, message = True, "OK"
        except Exception as e:
            message = f"{e}"
        return result, message

    @staticmethod
    def is_valid_email(email):
        result, message = False, "This email Already Exits"
        try:
            if not User.objects.filter(email=email).exists():
                result, message = True, "OK"
        except Exception as e:
            message = f"{e}"
        return result, message

    @staticmethod
    def is_contact_exists(email):
        result, message = False, "Email is not exits"
        try:
            if User.objects.filter(email=email).exists():
                result, message = True, "Ok"

        except Exception as e:
            message = f"{e}"
        return result, message
    
    @staticmethod
    def is_username_already_exists(username):
        result, message = False, "username already exists!"
        try:
            if not User.objects.filter(username=username).exists():
                result, message = True, "OK"
        except Exception as e:
            message = f"{e}"
        return result, message
