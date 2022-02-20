from accounts.models import User
from django.conf import settings
from forex_backends.common.validations import Validator
from rest_framework import serializers


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
