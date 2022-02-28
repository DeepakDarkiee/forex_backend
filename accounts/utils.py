from django.conf import settings
from django.contrib.auth import authenticate

# from django.contrib.auth import authenticate
# from twilio.base.exceptions import TwilioRestException
# from twilio.rest import Client

# from accounts.models import User

# client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
# verify = client.verify.services(settings.TWILIO_VERIFY_SERVICE_SID)


def create_user(user, request_data):
    result, message, data = False, "Failed", None
    try:
        user.set_password(request_data.get("password"))
        user = user.save()
        result, message, data = True, "User created successfully", None
    except Exception as e:
        result, message, data = False, str(e), None
    return result, message, data


# def user_check_password(emial, code):
#     try:
#         verify_status = client.verify.services(
#             settings.TWILIO_VERIFY_SERVICE_SID
#         ).verification_checks.create(to="+91" + email, code=code)
#         return verify_status.status == "approved"
#     except TwilioRestException:
#         return False

# def verify_contact_password(request_data):
#     result, message, data = False, "Failed", None
#     email = request_data.get("email", None)
#     password = request_data.get("password", None)
#     verify = user_check_password(email, password)
#     if verify:
#         result, message, data = True, "Successfully Verified", None
#     else:
#         result, message, data = False, "Invalid PASSWORD", None
#     return result, message, data


def user_check_password(email, password):
    try:
        verify_status = authenticate(email=email, password=password)
        if verify_status:
            return True
        else:
            return False
    except:
        return False


def verify_email_password(request_data):
    result, message, data = False, "Failed", None
    email = request_data.get("email", None)
    password = request_data.get("password", None)
    verify = user_check_password(email, password)
    print(verify)
    if verify:
        result, message, data = True, "Successfully Verified", None
    else:
        result, message, data = False, "Invalid User or PASSWORD", None
    return result, message, data


def forget_user_password(user, random_password):
    result, message, data = False, "Failed", None
    try:

        user.set_password(str(random_password))
        user.save()
        result, message, data = True, "forget password successfully", None
    except Exception as e:
        result, message, data = False, str(e), None
    return result, message, data


def forget_password_message_send(phone, random_password):
    result, message, data = False, "Failed", None
    try:
        message = f"Dear User, Your OTP new password {random_password} for SHEKUNJ Regards.%0AShekunj"
        values = {
            "authkey": settings.SMS_AUTH_TOKE,
            "mobiles": f"91{phone}",
            "message": message,
            "sender": "Shkunj",
            "route": 4,
            "DLT_TE_ID": settings.SMS_DLT_ID,
        }
        postdata = urllib.parse.urlencode(values)
        res = requests.get(settings.SEND_SMS_URL, params=postdata)

        logger.debug(
            f"Successfully sent new password for {phone} >>>>>>> Result >>>>>> {res.text}"
        )

        # client.messages.create(to="+91" + phone, from_ = settings.TWILIO_NUMBER,  body=f"Hello there, {random_password}!")
        result, message, data = True, "New password sent on your contact number.", None
    except Exception as e:
        result, message, data = False, str(e), None
    return result, message, data
