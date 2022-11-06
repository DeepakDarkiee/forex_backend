from django.conf import settings
from django.contrib.auth import authenticate
from accounts.models import Role, User

def create_user(user, request_data, role=None):
    result, message, data = False, "Failed", None
    try:
        role = Role.objects.get(name=role)
        user.role = role
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


def register_social_user(provider, user_id, email, name,last_name):
    filtered_user_by_email = User.objects.filter(
        username=email, email=email, auth_provider="google"
    )

    if filtered_user_by_email.exists():
        registered_user = authenticate(username=email, password=user_id)

        return {
            "username": registered_user.username,
            "email": registered_user.email,
            "tokens": registered_user.tokens(),
        }

    else:
        user = {
            "username": email,
            "name": name,
            "email": email,
            "password": user_id,
            "is_verified": True,
            "auth_provider": provider,
            "last_name": last_name,
        }
        new_user = User.objects.create_user(**user)
        return {
            "email": new_user.email,
            "username": new_user.username,
            "tokens": new_user.tokens(),
        }
