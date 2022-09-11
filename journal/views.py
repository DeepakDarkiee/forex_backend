from django.shortcuts import render

from rest_framework import status
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser

from accounts.models import User
from forex_backends.common import app_logger, rest_utils

from journal import serializers
from journal.models import APC, Issue, JournalMatrix, Journals, Volume, PageNumber, ArticleType, ScopeType
from journal.serializers import (
    ApcSerializers,
    ArticleTypeSerializer,
    IssueSerializers,
    JournalMatrixSerializers,
    JournalSerializers,
    VolumeSerializers,
    PageNumberSerializers,
    ScopeTypeSerializer
)

# Create your views here.
class VolumeGetPostView(generics.GenericAPIView):
    serializer_class = VolumeSerializers
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def get(self, request, format=None):
        try:
            volume_obj = Volume.objects.all()
            serializer = VolumeSerializers(volume_obj, many=True)
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
            

class VolumePutDeleteView(generics.GenericAPIView):
    serializer_class = VolumeSerializers   
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def put(self, request, id, format=None):
        try:
            volume = Volume.objects.filter(id=id)
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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)
    def get(self, request, format=None):
        try:
            issue_obj = Issue.objects.all()
            serializer = IssueSerializers(issue_obj, many=True)
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
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

class IssuePutDeleteView(generics.GenericAPIView):
    serializer_class = IssueSerializers   
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def put(self, request, id, format=None):
        try:
            issue = Issue.objects.filter(id=id)
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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def get(self, request, format=None):
        try:
            apc_obj = APC.objects.all()
            serializer = ApcSerializers(apc_obj, many=True)
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
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

class APCPutDeleteView(generics.GenericAPIView):
    serializer_class = ApcSerializers  
    parser_classes = (MultiPartParser,FormParser,JSONParser,) 

    def put(self, request, id, format=None):
        try:
            apc = APC.objects.filter(id=id)
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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def get(self, request, format=None):
        try:
            journal_matrix_obj = JournalMatrix.objects.all()
            serializer = JournalMatrixSerializers(journal_matrix_obj, many=True)
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
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )
            
class JournalMatrixPutDeleteView(generics.GenericAPIView):
    serializer_class = JournalMatrixSerializers   
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def put(self, request, id, format=None):
        try:
            journal_matrix_obj = JournalMatrix.objects.filter(id=id)
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
            journals_obj = Journals.objects.filter(id=id)
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
            
class PageNumberView(generics.GenericAPIView):
    serializer_class = PageNumberSerializers
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def get(self, request, format=None):
        try:
            page_number_obj = PageNumber.objects.all()
            serializer = PageNumberSerializers(page_number_obj, many=True)
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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def put(self, request, id, format=None):
        try:
            page_number_obj = PageNumber.objects.filter(id=id)
            serializer = self.serializer_class(page_number_obj, data=request.data)
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
            page_number_obj = PageNumber.objects.filter(id=id)
            if page_number_obj.exists():
                page_number_obj.delete()
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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def put(self, request, id, format=None):
        try:
            articletype_obj = ArticleType.objects.filter(id=id)
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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

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
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def put(self, request, id, format=None):
        try:
            scopetype_obj = ScopeType.objects.filter(id=id)
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
