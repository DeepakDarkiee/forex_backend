from accounts.models import User
from rest_framework import serializers

from accounts.utils import register_social_user
from forex_backends.common.validations import Validator

from .provider_validation import Google


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()
    

    def validate_auth_token(self, auth_token):
        google_helper = Google()
        user_data = google_helper.validate(auth_token)
        if isinstance(user_data, str):
            raise serializers.ValidationError(user_data)
        try:
            user_data["sub"]
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired, please login again."
            )

        result = User.objects.filter(username=user_data["email"], auth_provider="email")
        if result:
            raise serializers.ValidationError("This email already exists!")

        user_id = user_data["sub"]
        email = user_data["email"]
        name = user_data["given_name"]
        # name = user_data["name"]
        last_name = user_data["family_name"]
        provider = "google"

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name,last_name=last_name
        )
