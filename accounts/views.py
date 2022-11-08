from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from accounts.models import Role, User
from accounts.serializers import UpdateProfileSerializer, UpdateRolePermissionSerializer, UserDetailSerializer, UserListSerializer
from forex_backends.common import rest_utils
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from django.shortcuts import get_object_or_404
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
    def patch(self, request, format=None):
        try:
            user_id = self.request.user.id
            user = User.objects.get(id=user_id)
            serializer = self.serializer_class(
                user, data=request.data, context={"request": request},
                partial=True
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
                status.HTTP_200_OK, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

class SingleUserDetailApiView(generics.GenericAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request,id, format=None):
        try:
            user_obj = User.objects.get(id=id)
            message = "Ok"
            serializer = UserDetailSerializer(user_obj, many=False)
            return rest_utils.build_response(
                status.HTTP_200_OK, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

class SingleUserUpdateApiView(generics.GenericAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def put(self,request, id,format=None):
        try:
            user_id = id
            user = User.objects.get(id=user_id)
            serializer = self.serializer_class(
                user, data=request.data, context={"request": request}
            )
            if serializer.is_valid():
                serializer.save()
                message = "User Successfully Updated"
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
    def patch(self, request,id, format=None):
        try:
            user_id = id
            user = User.objects.get(id=user_id)
            serializer = self.serializer_class(
                user, data=request.data, context={"request": request},partial=True
            )
            if serializer.is_valid():
                serializer.save()
                message = "User Successfully Updated"
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

class UserListApiView(generics.GenericAPIView):
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            role = self.request.query_params.get('role')
            if role:
                user_obj = User.objects.filter(role__name=role)
            else:
                user_obj = User.objects.all()
            message = "Ok"
            serializer = UserDetailSerializer(user_obj, many=True)
            return rest_utils.build_response(
                status.HTTP_200_OK, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

class UpdateRoleApiView(generics.GenericAPIView):
    serializer_class = UpdateRolePermissionSerializer
    # permission_classes = [IsAuthenticated]

    def put(self, request,role, format=None):
        try:
            role = Role.objects.get(name=role)
            serializer = self.serializer_class(
                role, data=request.data, context={"request": request}
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
    def patch(self, request,role, format=None):
        try:
            role = Role.objects.get(name=role)
            serializer = self.serializer_class(
                role, data=request.data, context={"request": request}
            )
            serializer = self.serializer_class(
                role, data=request.data, context={"request": request},
                partial=True
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