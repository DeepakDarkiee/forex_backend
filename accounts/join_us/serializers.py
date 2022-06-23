from forex_backends.common.validations import Validator
from rest_framework import serializers
from accounts.models import User


class RegisterRoleSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = ["email", "password", "role"]

    def validate(self, data):
        result, message = Validator.is_valid_email(data["email"])
        if not result:
            raise serializers.ValidationError(message)
        return data