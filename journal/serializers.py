from rest_framework import serializers

from journal.models import APC, Issue, JournalMatrix, Journals, Volume, Article, ScopeType, ArticleType


class VolumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = "__all__"


class IssueSerializers(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class ApcSerializers(serializers.ModelSerializer):
    class Meta:
        model = APC
        fields = "__all__"


class JournalMatrixSerializers(serializers.ModelSerializer):
    class Meta:
        model = JournalMatrix
        fields = "__all__"


# class ScopeTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScopeType
#         fields = "__all__"
        
# class ArticleTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArticleType
#         fields = "__all__"   

class JournalSerializers(serializers.ModelSerializer):
    # scope = ScopeTypeSerializer(many=True)
    # article_type = ArticleTypeSerializer(many=True)
    class Meta:
        model = Journals
        fields = "__all__"
        
    def to_representation(self, instance):
        rep = super(JournalSerializers, self).to_representation(instance)
        rep['journal_author'] = instance.journal_author.username if instance.journal_author  else '' 
        rep['volume'] = instance.volume.volume if instance.volume  else '' 
        rep['issue'] = instance.issue.issue if instance.issue  else '' 
        rep['journal_subscriber'] = instance.journal_subscriber.username  if instance.journal_subscriber  else ''       
        rep['journal_reviewer'] = instance.journal_reviewer.username if instance.journal_reviewer  else  ''
        rep['journal_matrix'] = instance.journal_matrix.submission_count if instance.journal_matrix  else  ''
    

        return rep


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