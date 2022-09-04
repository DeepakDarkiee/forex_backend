from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_serializer_method

from forex_backends.common import app_logger, rest_utils

from accounts.models import User
from accounts.reviewer.serializers import (
    ForgetReviewerPasswordSerializer,
    LoginReviewerSerializer,
    RegisterReviewerSerializer,
)
from accounts.utils import (
    create_user,
    forget_password_message_send,
    forget_user_password,
    verify_email_password,
)


class RegisterReviewerView(generics.GenericAPIView):
    serializer_class = RegisterReviewerSerializer

    def post(self, request):
        # breakpoint()
        try:
            data = request.data
            serializer = self.serializer_class(data=data)

            if serializer.is_valid():
                user = serializer.save(email=data.get("email"))
                result, message, response_data = create_user(user, data, role="Reviewer")
                if result:
                    data = serializer.data
                    data["token"] = user.tokens().get("access")
                    data["refresh_token"] = user.tokens().get("refresh")
                    return rest_utils.build_response(
                        status.HTTP_200_OK, message, data=data, errors=None
                    )
                else:
                    return rest_utils.build_response(
                        status.HTTP_400_BAD_REQUEST, message, data=None, errors=message
                    )
            else:
                return rest_utils.build_response(
                    status.HTTP_400_BAD_REQUEST,
                    rest_utils.HTTP_REST_MESSAGES["400"],
                    data=None,
                    errors=serializer.errors,
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


class LoginReviewerAPIView(generics.GenericAPIView):
    serializer_class = LoginReviewerSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                message = "User Successfully Login"
                return rest_utils.build_response(
                    status.HTTP_200_OK, message, data=serializer.data, errors=None
                )
            else:
                return rest_utils.build_response(
                    status.HTTP_400_BAD_REQUEST,
                    rest_utils.HTTP_REST_MESSAGES["400"],
                    data=None,
                    errors=serializer.errors,
                )

        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


class ForgetReviewerPasswordView(generics.GenericAPIView):
    serializer_class = ForgetReviewerPasswordSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)

            if serializer.is_valid():
                user = User.objects.filter(email=data.get("email")).last()
                return rest_utils.build_response(
                    status.HTTP_200_OK, "success", data=None, errors=None
                )
            else:
                return rest_utils.build_response(
                    status.HTTP_400_BAD_REQUEST,
                    rest_utils.HTTP_REST_MESSAGES["400"],
                    data=None,
                    errors=serializer.errors,
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )
