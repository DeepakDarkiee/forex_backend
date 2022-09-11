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
    PageNumber,
    ScopeType,
)
from editorial.models import Article

class ArticleInline1(admin.StackedInline):
    model = Article
    extra = 1 

class ScopeTypeInline(admin.StackedInline):
    pass

class JournalsAdmin(ImportExportModelAdmin):

    model = Journals
    list_display = [
        "journal_title",
        "journal_image",
        "ISSN_PRINT",
        "DOI",
        "frequency",
        "publication_year",
        "special_issue",
        "journal_matrix",
    ]
    list_filter = ("scope", "frequency")
    prepopulated_fields = {"journal_slug": ("journal_title",)}
    inlines = [
    ArticleInline1,
    ]


class JournalsInline1(admin.StackedInline):
    model = Journals
    extra = 1  
class VolumeAdmin(ImportExportModelAdmin):

    model = Volume
    list_display = ["volume", "year"]
    list_filter = ["year"]
    inlines = [
    JournalsInline1,
    ]

class JournalsInline2(admin.StackedInline):
    model = Journals
    extra = 1  
class IssueAdmin(ImportExportModelAdmin):

    model = Issue
    list_display = ["issue", "status"]
    list_filter = ["status"]
    inlines = [
    JournalsInline2,
    ]


class APCAdmin(ImportExportModelAdmin):

    model = APC
    list_display = ["fixed_amount", "discount_options", "waive_off"]

class JournalsInline3(admin.StackedInline):
    model = Journals
    extra = 1 
class JournalMatrixAdmin(ImportExportModelAdmin):

    model = JournalMatrix
    list_display = ["download", "views"]
    inlines = [
    JournalsInline3,
    ]


class ArticleTypeAdmin(ImportExportModelAdmin):

    model = ArticleType
    list_display = ["article_type"]


class ArticleAdmin(ImportExportModelAdmin):

    model = Article
    list_display = ["title"]  
    prepopulated_fields = {"article_slug": ("title",)}


class ArticleInline2(admin.StackedInline):
  model = Article
  extra = 1

class PageNumberAdmin(ImportExportModelAdmin):

    model = PageNumber
    list_display = ["page_from","page_to"]    
    inlines = [
    ArticleInline2,
    ]

class ScopeTypeAdmin(ImportExportModelAdmin):

    model = ScopeType
    list_display = ["scope_type"]

class ArticleInline(admin.StackedInline):
  model = Article

      
    
admin.site.register(Journals, JournalsAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(APC, APCAdmin)
admin.site.register(JournalMatrix, JournalMatrixAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PageNumber, PageNumberAdmin)
admin.site.register(ScopeType, ScopeTypeAdmin)
