from django.conf import settings
from django.contrib.auth.models import update_last_login

from rest_framework import serializers

from forex_backends.common.validations import Validator

from accounts.models import User
from accounts.utils import verify_email_password


class RegisterReviewerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):
        result, message = Validator.is_valid_email(data["email"])
        if not result:
            raise serializers.ValidationError(message)
        return data


class LoginReviewerSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, required=False)
    password = serializers.CharField(write_only=True)

    tokens = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["tokens", "refresh_token", "email", "password", "role"]

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)
        try:
            user = User.objects.get(email=email)
            if user.is_active:
                validated_data = {"email": email, "password": password}
                result, message, user = Validator.is_valid_user(email, password)
                if not result:
                    raise serializers.ValidationError(message)
                update_last_login(None,user)
                return {
                    "email": user.email,
                    "tokens": user.tokens().get("access"),
                    "refresh_token": user.tokens().get("refresh"),
                    "password": user.password,
                    "message": message,
                    "role" : user.role
                }
            else:
                raise serializers.ValidationError("Your account is Deactivated")
        except User.DoesNotExist:
            raise serializers.ValidationError("User Not Exists")


class ForgetReviewerPasswordSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email"]

    def validate(self, data):
        result, message = Validator.is_contact_exists(data["email"])
        if not result:
            raise serializers.ValidationError(message)
        return data
