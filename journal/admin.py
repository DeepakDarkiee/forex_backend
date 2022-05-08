from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from journal.models import (
    ArticleType,
    Journals,
    Volume,
    Issue,
    APC,
    JournalMatrix,
    Article,
    PageNumber,
    ScopeType
)


class JournalsAdmin(ImportExportModelAdmin):

    model = Journals
    list_display = [
        "journal_title",
        "journal_image",
        "description",
        "ISSN_PRINT",
        "DOI",
        "frequency",
        "publication_year",
        "special_issue",
        "journal_matrix",
    ]
    list_filter = ("scope", "frequency")
    prepopulated_fields = {"journal_slug": ("journal_title",)}
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('journal_slug')
        return self.readonly_fields
    
    # def get_readonly_fields(self, request, obj = None):
    #     if obj and obj.lock_slug == True:
    #         return ('journal_slug',) + self.readonly_fields        
    #     return self.readonly_fields

class VolumeAdmin(ImportExportModelAdmin):

    model = Volume
    list_display = ["volume", "year"]
    list_filter = ["year"]


class IssueAdmin(ImportExportModelAdmin):

    model = Issue
    list_display = ["issue", "status"]
    list_filter = ["status"]


class APCAdmin(ImportExportModelAdmin):

    model = APC
    list_display = ["fixed_amount", "discount_options", "waive_off"]


class JournalMatrixAdmin(ImportExportModelAdmin):

    model = JournalMatrix
    list_display = ["download", "views"]


class ArticleTypeAdmin(ImportExportModelAdmin):

    model = ArticleType
    list_display = ["article_type"]
    
class ArticleAdmin(ImportExportModelAdmin):

    model = Article
    list_display = ["title","refrence"]  
    prepopulated_fields = {"article_slug": ("title",)}
    # readonly_fields=('article_slug', )
  
    
    
class PageNumberAdmin(ImportExportModelAdmin):

    model = PageNumber
    list_display = ["page_from","page_to"]    
    
class ScopeTypeAdmin(ImportExportModelAdmin):

    model = ScopeType
    list_display = ["scope_type"]      




admin.site.register(Journals, JournalsAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(APC, APCAdmin)
admin.site.register(JournalMatrix, JournalMatrixAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PageNumber, PageNumberAdmin)
admin.site.register(ScopeType, ScopeTypeAdmin)





