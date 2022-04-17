from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from accounts.models import User
from accounts.serializers import UpdateProfileSerializer, UserDetailSerializer

from forex_backends.common import app_logger, rest_utils

# Create your views here.


class UpdateProfileApiView(generics.GenericAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        try:
            user_id = self.request.user.id
            user = User.objects.get(id=user_id)
            serializer = self.serializer_class(
                user, data=request.data, context={"request": request}
            )
            if serializer.is_valid():
                serializer.save()
                message = "Profile Successfully Updated"
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


class UserDetailApiView(generics.GenericAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            user_obj = User.objects.get(id=request.user.id)
            message = "Ok"
            serializer = UserDetailSerializer(user_obj, many=False)
            return rest_utils.build_response(
                    status.HTTP_200_OK,message, data=serializer.data, errors=None
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


