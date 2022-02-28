from accounts.models import User
from django.conf import settings
from forex_backends.common.validations import Validator
from rest_framework import serializers
from accounts.utils import verify_email_password

class RegisterAuthorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):
        result, message = Validator.is_valid_email(data["email"])
        if not result:
            raise serializers.ValidationError(message)

        # if data["email"] != "":
        #     result, message = Validator.is_valid_exists_email(data["email"])
        #     if not result:
        #         raise serializers.ValidationError(message)

        return data
    
class LoginAuthorSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True)

    tokens = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["tokens", "refresh_token", "email", "password"]

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)
        user = User.objects.get(email=email)
        if user.is_active:
            validated_data = {"email": email,"password": password}
            # password_result, password_message, data = verify_email_password(validated_data)
            # if not password_result:
            #     raise serializers.ValidationError(password_message)
            #     return {
            #         "message": password_message,
            #     }
            # else:
            result, message, user = Validator.is_valid_user(email,password)
            if not result:
                raise serializers.ValidationError(message)

            return {
                "email": user.email,
                "tokens": user.tokens().get("access"),
                "refresh_token": user.tokens().get("refresh"),
                "password": user.password,
                "message": message,
            }
        else:
            raise serializers.ValidationError("Your account is Deactivated")    


class ForgetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ["email"]
    def validate(self, data):
        result, message = Validator.is_contact_exists(data["email"])
        if not result:
            raise serializers.ValidationError(message)
        return data