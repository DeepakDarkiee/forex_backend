from rest_framework import generics, status
from rest_framework.response import Response

from forex_backends.common import rest_utils

from .serializers import GoogleSocialAuthSerializer

# Create your views here.


class GoogleSocialAuthView(generics.GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        try:

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                data = (serializer.validated_data)["auth_token"]
                message = "User Successfully Created"
                return rest_utils.build_response(
                    status.HTTP_200_OK, message, data=data, errors=None
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
