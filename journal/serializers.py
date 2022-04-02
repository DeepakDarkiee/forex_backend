from rest_framework import serializers

from journal.models import APC, Issue, JournalMatrix, Journals, Volume


class VolumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = "__all__"

class IssueSerializers(serializers.ModelSerializer):
    class Meta:
        model= Issue
        fields = "__all__"

class ApcSerializers(serializers.ModelSerializer):
    class Meta :
        model = APC
        fields = "__all__"

class JournalMatrixSerializers(serializers.ModelSerializer):
    class Meta :
        model = JournalMatrix
        fields = "__all__"

class JournalSerializers(serializers.ModelSerializer):
    class Meta :
        model = Journals
        fields = "__all__"