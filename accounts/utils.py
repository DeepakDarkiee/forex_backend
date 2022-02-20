from django.conf import settings


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
