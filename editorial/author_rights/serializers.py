from rest_framework import serializers

from accounts.models import User
from editorial.models import Article
from forex_backends.common.validations import Validator

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        
    def to_representation(self, instance):
        rep = super(ArticleSerializer, self).to_representation(instance)
        rep['journal'] = instance.journal.journal_title if instance.journal  else ''    
        rep['author_details'] = instance.author_details.email if instance.author_details  else '' 
        rep['page_number'] = instance.page_number.page_from if instance.page_number  else ''     
            
         
        return rep