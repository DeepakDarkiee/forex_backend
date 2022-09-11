from rest_framework import serializers
from editorial.models import ArticleActivity

class ArticleActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleActivity
        fields = "__all__"