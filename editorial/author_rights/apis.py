from django.shortcuts import render
from editorial.models import Article
from editorial.author_rights.serializers import ArticleSerializer
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

    def get(self, request, format=None):
        try:
            user = self.request.user
            article = Article.objects.filter(author_details=user)
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

    def post(self, request, format=None):
        try:
            user = self.request.user
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author_details=user)
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

class SingleArticleView(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,FormParser,)
    permission_classes = [IsAuthenticated]

    def get(self, request,id, format=None):
        try:
            user = self.request.user
            article = Article.objects.filter(author_details=user, id=id)
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

    def put(self, request, id, format=None):
        try:
            user = self.request.user
            article = Article.objects.filter(author_details=user,id=id)
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

    def patch(self, request, id, format=None):
        try:
            user = self.request.user
            article = Article.objects.filter(author_details=user,id=id)
            serializer = self.serializer_class(
                article, data=request.data, partial=True
            )  # set partial=True to update a data partially
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

    def delete(self, request, id, format=None):
        try:
            user = self.request.user
            article = Article.objects.filter(author_details=user,id=id)
            if article.exists():
                article.delete()
                message = "Article Successfully Deleted"
                return rest_utils.build_response(
                        status.HTTP_204_NO_CONTENT, message, data=None, errors=None
                )
            else:
                return rest_utils.build_response(
                    status.HTTP_404_NOT_FOUND,
                    rest_utils.HTTP_REST_MESSAGES["404"],
                    data=None,
                    errors=None,
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )