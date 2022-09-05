from django.shortcuts import render
from editorial.models import Article
from editorial.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from forex_backends.common import app_logger, rest_utils
from accounts.models import User

# Create your views here.
class ArticleView(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,FormParser,)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Created"
                return rest_utils.build_response(
                    status.HTTP_201_CREATED, message, data=serializer.data, errors=None
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

    def put(self, request, format=None):
        try:
            user_id = self.request.user.id
            user = User.objects.get(id=user_id)
            article = Article.objects.get(author_details=user_id)
            serializer = self.serializer_class(article, data=request.data)
            if serializer.is_valid():
                serializer.save(author_details=user)
                message = "Article Successfully Updated"
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

    def get(self, request, format=None):
        try:
            article = Article.objects.all()
            serializer = self.serializer_class(article, many=True)
            message = "Ok"
            return rest_utils.build_response(
                status.HTTP_200_OK, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

    def patch(self, request):
        try:
            user_id = self.request.user.id
            article = Article.objects.get(author_details=user_id)
            serializer = self.serializer_class(
                article, data=request.data, partial=True
            )  # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
                message = "Article Successfully Updated"
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