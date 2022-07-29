from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser

from accounts.models import User
from accounts.editor.serializers import (
    ForgetEditorPasswordSerializer,
    LoginEditorSerializer,
    RegisterEditorSerializer,
)
from forex_backends.common import app_logger, rest_utils

from journal import serializers
from journal.models import APC, Issue, JournalMatrix, Journals, Volume, Article, PageNumber, ArticleType, ScopeType
from journal.serializers import (
    ApcSerializers,
    ArticleTypeSerializer,
    IssueSerializers,
    JournalMatrixSerializers,
    JournalSerializers,
    VolumeSerializers,
    ArticleSerializer,
    PageNumberSerializers,
    ScopeTypeSerializer
)

# Create your views here.
class VolumeGetPostView(generics.GenericAPIView):
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
            

class VolumePutDeleteView(generics.GenericAPIView):
    serializer_class = VolumeSerializers   
    def put(self, request, id, format=None):
        try:
            volume = Volume.objects.get(id=id)
            serializer = self.serializer_class(volume, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Volume Successfully Updated"
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
            volume = Volume.objects.filter(id=id)
            if volume.exists():
                volume.delete()
                message = "Volume Successfully Deleted"
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

class IssuePutDeleteView(generics.GenericAPIView):
    serializer_class = IssueSerializers   
    def put(self, request, id, format=None):
        try:
            issue = Issue.objects.get(id=id)
            serializer = self.serializer_class(issue, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Issue Successfully Updated"
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
            issue = Issue.objects.filter(id=id)
            if issue.exists():
                issue.delete()
                message = "Issue Successfully Deleted"
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

class APCPutDeleteView(generics.GenericAPIView):
    serializer_class = ApcSerializers   
    def put(self, request, id, format=None):
        try:
            apc = APC.objects.get(id=id)
            serializer = self.serializer_class(apc, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "APC Successfully Updated"
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
            apc = APC.objects.filter(id=id)
            if apc.exists():
                apc.delete()
                message = "APC Successfully Deleted"
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

class JournalMatrixView(generics.GenericAPIView):
    serializer_class = JournalMatrixSerializers

    def get(self, request, format=None):
        try:
            journal_matrix_obj = JournalMatrix.objects.all()
            serializer = JournalMatrixSerializers(journal_matrix_obj, many=True)
            message = "Ok"
            return rest_utils.build_response(
                status.HTTP_200_OK, message, data=serializer.data, errors=None
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
            
class JournalMatrixPutDeleteView(generics.GenericAPIView):
    serializer_class = JournalMatrixSerializers   
    
    def put(self, request, id, format=None):
        try:
            journal_matrix_obj = JournalMatrix.objects.get(id=id)
            serializer = self.serializer_class(journal_matrix_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "JournalMatrix Successfully Updated"
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
            journal_matrix_obj = JournalMatrix.objects.filter(id=id)
            if journal_matrix_obj.exists():
                journal_matrix_obj.delete()
                message = "Journal Matrix Successfully Deleted"
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
            
            
class JournalsView(generics.GenericAPIView):
    serializer_class = JournalSerializers
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def get(self, request, format=None):
        try:
            journal_obj = Journals.objects.all()
            serializer = JournalSerializers(journal_obj, many=True)
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


class JournalsPutDeleteView(generics.GenericAPIView):
    serializer_class = JournalSerializers   
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    
    def put(self, request, id, format=None):
        try:
            journals_obj = Journals.objects.get(id=id)
            serializer = self.serializer_class(journals_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Journals Successfully Updated"
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
            journal_matrix_obj = JournalMatrix.objects.filter(id=id)
            if journal_matrix_obj.exists():
                journal_matrix_obj.delete()
                message = "Journals Successfully Deleted"
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
            
            
class ArticleView(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    parser_classes = (MultiPartParser,)
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
            

class PageNumberView(generics.GenericAPIView):
    serializer_class = PageNumberSerializers

    def get(self, request, format=None):
        try:
            PageNumber_obj = PageNumber.objects.all()
            serializer = PageNumberSerializers(PageNumber_obj, many=True)
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
            serializer = PageNumberSerializers(data=request.data)

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
            
            
class PageNumberPutDeleteView(generics.GenericAPIView):
    serializer_class = PageNumberSerializers   
    
    def put(self, request, id, format=None):
        try:
            PageNumber_obj = PageNumber.objects.get(id=id)
            serializer = self.serializer_class(PageNumber_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Page Number Successfully Updated"
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
            PageNumber_obj = PageNumber.objects.filter(id=id)
            if PageNumber_obj.exists():
                PageNumber_obj.delete()
                message = "Page Number Successfully Deleted"
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


class ArticleTypeView(generics.GenericAPIView):
    serializer_class = ArticleTypeSerializer

    def get(self, request, format=None):
        try:
            articletype_obj = ArticleType.objects.all()
            serializer = ArticleTypeSerializer(articletype_obj, many=True)
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
            serializer = ArticleTypeSerializer(data=request.data)

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
            
            
class ArticleTypePutDeleteView(generics.GenericAPIView):
    serializer_class = ArticleTypeSerializer   
    
    def put(self, request, id, format=None):
        try:
            articletype_obj = ArticleType.objects.get(id=id)
            serializer = self.serializer_class(articletype_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Article Type Successfully Updated"
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
            articletype_obj = ArticleType.objects.filter(id=id)
            if articletype_obj.exists():
                articletype_obj.delete()
                message = "Article Type Successfully Deleted"
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



class ScopeTypeView(generics.GenericAPIView):
    serializer_class = ScopeTypeSerializer

    def get(self, request, format=None):
        try:
            scopetype_obj = ScopeType.objects.all()
            serializer = ScopeTypeSerializer(scopetype_obj, many=True)
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
            serializer = ScopeTypeSerializer(data=request.data)

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
            
            
class ScopeTypePutDeleteView(generics.GenericAPIView):
    serializer_class = ScopeTypeSerializer   
    
    def put(self, request, id, format=None):
        try:
            scopetype_obj = ScopeType.objects.get(id=id)
            serializer = self.serializer_class(scopetype_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "Scop Type Successfully Updated"
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
            scopetype_obj = ScopeType.objects.filter(id=id)
            if scopetype_obj.exists():
                scopetype_obj.delete()
                message = "Scope Type Successfully Deleted"
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
