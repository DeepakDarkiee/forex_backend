from django.conf import settings
from django.contrib.auth import authenticate

def create_user(user, request_data, role=None):
    result, message, data = False, "Failed", None
    try:
        if role == "Editor":
            user.role = "Editor"
        elif role == "Reviewer":
            user.role = "Reviewer"
        elif role == "Both-ER":
            user.role = "Both-ER"
        else:
            user.role = "Author"
        user.set_password(request_data.get("password"))
        user = user.save()
        result, message, data = True, "User created successfully", None
    except Exception as e:
        result, message, data = False, str(e), None
    return result, message, data


def user_check_password(email, password):
    try:
        verify_status = authenticate(email=email, password=password)
        if verify_status:
            return True
        else:
            return False
    except Exception:
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
            "sender": "Forex",
            "route": 4,
            "DLT_TE_ID": settings.SMS_DLT_ID,
        }
        postdata = urllib.parse.urlencode(values)
        res = requests.get(settings.SEND_SMS_URL, params=postdata)

        logger.debug(
            f"Successfully sent new password for {phone} >>>>>>> Result >>>>>> {res.text}"
        )

        result, message, data = True, "New password sent on your contact number.", None
    except Exception as e:
        result, message, data = False, str(e), None
    return result, message, data
