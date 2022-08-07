from rest_framework import serializers

from accounts.models import User

from forex_backends.common.validations import Validator


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "contact", "profile_pic")

    def validate(self, attrs):
        username = attrs.get("username", None)
        contact = attrs.get("contact", None)
        first_name = attrs.get("first_name", None)
        last_name = attrs.get("last_name", None)
        profile_pic = attrs.get("profile_pic", None)

        try:
            # user = self.request.user
            user = self.context.get("request").user
            if user.is_active:
                validated_data = {"username": username, "contact": contact}
                # result_contact, message = Validator.is_contact_already_exists(contact)
                result_username, message = Validator.is_username_already_exists(
                    username
                )
                if not result_username:
                    raise serializers.ValidationError(message)
                return {
                    "username": username,
                    "contact": contact,
                    "first_name": first_name,
                    "last_name": last_name,
                    "profile_pic": profile_pic,
                }
            else:
                raise serializers.ValidationError("Your account is Deactivated")
        except User.DoesNotExist:
            raise serializers.ValidationError("User Not Exists")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)