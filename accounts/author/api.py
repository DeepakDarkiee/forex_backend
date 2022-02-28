from accounts.models import User
from accounts.author.serializers import (
    RegisterAuthorSerializer,
    LoginAuthorSerializer,
    ForgetPasswordSerializer,
)
from accounts.utils import (
    create_user,
    verify_email_password,
    forget_user_password,
    forget_password_message_send,
)
from drf_yasg.utils import swagger_serializer_method
from forex_backends.common import app_logger, rest_utils
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated


class RegisterAuthorView(generics.GenericAPIView):
    serializer_class = RegisterAuthorSerializer

    def post(self, request):

        try:
            data = request.data
            serializer = self.serializer_class(data=data)

            if serializer.is_valid():
                user = serializer.save(email=data.get("email"))
                result, message, response_data = create_user(user, data)
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


class LoginAuthorAPIView(generics.GenericAPIView):
    serializer_class = LoginAuthorSerializer

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


class ForgetPasswordView(generics.GenericAPIView):
    serializer_class = ForgetPasswordSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer_class(data=data)

            if serializer.is_valid():
                user = User.objects.filter(email=data.get("email")).last()
                # if user:
                #     random_password = random.randint(0,999999)
                #      # create method for send sms with random_password to that particular contact number
                #     result, message, response_data = forget_user_password(user, random_password)
                #     result, message, response_data = forget_password_message_send(request.data["contact"],random_password)

                # if result:
                # data = serializer.data
                # data["token"] = user.tokens().get("access")
                # data["refresh_token"] = user.tokens().get("refresh")
                return rest_utils.build_response(
                    status.HTTP_200_OK, "success", data=None, errors=None
                )
                # else:
                #     return rest_utils.build_response(
                #         status.HTTP_400_BAD_REQUEST, message, data=None, errors=message
                #     )
            else:
                return rest_utils.build_response(
                    status.HTTP_400_BAD_REQUEST,
                    rest_utils.HTTP_REST_MESSAGES["400"],
                    data=None,
                    errors=serializer.errors,
                )
            # logger.debug('Log whatever you want')
            # logger.error("Test!!")
            # logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )
