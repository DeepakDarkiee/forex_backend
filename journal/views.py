from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from accounts.models import User
from accounts.editor.serializers import (
    ForgetEditorPasswordSerializer,
    LoginEditorSerializer,
    RegisterEditorSerializer,
)
from forex_backends.common import app_logger, rest_utils

from journal import serializers
from journal.models import APC, Issue, JournalMatrix, Journals, Volume, Article
from journal.serializers import (
    ApcSerializers,
    IssueSerializers,
    JournalMatrixSerializers,
    JournalSerializers,
    VolumeSerializers,
    ArticleSerializer,
)

# Create your views here.
class VolumeView(generics.GenericAPIView):
    serializer_class = VolumeSerializers

    def get(self, request, format=None):
        try:
            volume_obj = Volume.objects.all()
            serializer = VolumeSerializers(volume_obj, many=True)
            # return Response(volume_serializer.data)
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
            serializer = VolumeSerializers(data=request.data)

            if serializer.is_valid():
                serializer.save()
                # return Response(volume_serializer.data, status=status.HTTP_201_CREATED)
                message = "Created"
                return rest_utils.build_response(
                    status.HTTP_201_CREATED, message, data=serializer.data, errors=None
                )
            # return Response(volume_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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


class IssueView(generics.GenericAPIView):
    serializer_class = IssueSerializers

    def get(self, request, format=None):
        try:
            issue_obj = Issue.objects.all()
            serializer = IssueSerializers(issue_obj, many=True)
            # return Response(issue_serializer.data)
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
            serializer = IssueSerializers(data=request.data)

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
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


class APCView(generics.GenericAPIView):
    serializer_class = ApcSerializers

    def get(self, request, format=None):
        try:
            apc_obj = APC.objects.all()
            serializer = ApcSerializers(apc_obj, many=True)
            # return Response(serializer.data)
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
            serializer = ApcSerializers(data=request.data)

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
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


class JournalMatrixView(generics.GenericAPIView):
    serializer_class = JournalMatrixSerializers

    def get(self, request, format=None):
        try:
            journal_matrix_obj = JournalMatrix.objects.all()
            serializer = JournalMatrixSerializers(journal_matrix_obj, many=True)
            message = "Ok"
            return rest_utils.build_response(
                status.HTTP_201_CREATED, message, data=serializer.data, errors=None
            )
            # return Response(serializer.data)
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

    def post(self, request, format=None):
        try:
            serializer = JournalMatrixSerializers(data=request.data)

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
            #     return Response(
            #         serializer.data, status=status.HTTP_201_CREATED
            #     )
            # return Response(
            #     serializer.errors, status=status.HTTP_400_BAD_REQUEST
            # )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


class JournalsView(generics.GenericAPIView):
    serializer_class = JournalSerializers

    def get(self, request, format=None):
        try:
            journal_obj = Journals.objects.all()
            serializer = JournalSerializers(journal_obj, many=True)
            # return Response(serializer.data)
            message = "Ok"
            return rest_utils.build_response(
                status.HTTP_201_CREATED, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

    def post(self, request, format=None):
        try:
            serializer = JournalSerializers(data=request.data)

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
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


class ArticleView(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    # parser_classes = (MultiPartParser,)
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
                status.HTTP_201_CREATED, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

    def patch(self, request):
        try:
            user_id = self.request.user.id
            user = User.objects.get(id=user_id)
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
