from xml.etree.ElementInclude import include
from rest_framework import serializers
from editorial.models import ArticleActivity

class ArticleActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleActivity
        fields = "__all__"

class ArticleStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleActivity
        exclude = ("comment","commented_by",)

class ArticleCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleActivity
        exclude = ("status","approved_by",)