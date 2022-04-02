from django.shortcuts import render
from rest_framework.views import APIView
from journal import serializers

from journal.models import APC, Issue, JournalMatrix, Journals, Volume
from journal.serializers import ApcSerializers, IssueSerializers, JournalMatrixSerializers, JournalSerializers, VolumeSerializers
from rest_framework.response import Response
from rest_framework import status
from accounts.editor.serializers import (
    ForgetEditorPasswordSerializer,
    LoginEditorSerializer,
    RegisterEditorSerializer,
)
from rest_framework import generics, status


# Create your views here.
class VolumeView(generics.GenericAPIView):
    serializer_class = VolumeSerializers

    def get(self, request, format=None):
        volume_obj = Volume.objects.all()
        volume_serializer = VolumeSerializers(volume_obj,many=True)
        return Response(volume_serializer.data)
    
    def post(self, request, format=None):
        volume_serializer = VolumeSerializers(data=request.data)

        if volume_serializer.is_valid():
            volume_serializer.save()
            return Response(volume_serializer.data, status=status.HTTP_201_CREATED)
        return Response(volume_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssueView(generics.GenericAPIView):
    serializer_class = IssueSerializers

    def get(self, request, format=None):
        issue_obj = Issue.objects.all()
        issue_serializer = IssueSerializers(issue_obj,many=True)
        return Response(issue_serializer.data)
    
    def post(self, request, format=None):
        issue_serializer = IssueSerializers(data=request.data)

        if issue_serializer.is_valid():
            issue_serializer.save()
            return Response(issue_serializer.data, status=status.HTTP_201_CREATED)
        return Response(issue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APCView(generics.GenericAPIView):
    serializer_class = ApcSerializers

    def get(self, request, format=None):
        apc_obj = APC.objects.all()
        apc_serializer = ApcSerializers(apc_obj,many=True)
        return Response(apc_serializer.data)

    def post(self, request, format=None):
        apc_serializer = ApcSerializers(data=request.data)

        if apc_serializer.is_valid():
            apc_serializer.save()
            return Response(apc_serializer.data, status=status.HTTP_201_CREATED)
        return Response(apc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalMatrixView(generics.GenericAPIView):
    serializer_class = JournalMatrixSerializers

    def get(self, request, format=None):
        journal_matrix_obj = JournalMatrix.objects.all()
        journal_matrix_serializer = JournalMatrixSerializers(journal_matrix_obj,many=True)
        return Response(journal_matrix_serializer.data)

    def post(self, request, format=None):
        journal_matrix_serializer = JournalMatrixSerializers(data=request.data)

        if journal_matrix_serializer.is_valid():
            journal_matrix_serializer.save()
            return Response(journal_matrix_serializer.data, status=status.HTTP_201_CREATED)
        return Response(journal_matrix_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalsView(generics.GenericAPIView):
    serializer_class = JournalSerializers

    def get(self, request, format=None):
        journal_obj = Journals.objects.all()
        journal_serializer = JournalSerializers(journal_obj,many=True)
        return Response(journal_serializer.data)

    def post(self, request, format=None):
        journal_serializer = JournalSerializers(data=request.data)

        if journal_serializer.is_valid():
            journal_serializer.save()
            return Response(journal_serializer.data, status=status.HTTP_201_CREATED)
        return Response(journal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)