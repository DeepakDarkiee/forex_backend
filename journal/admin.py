from django.contrib import admin

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
)


class JournalsAdmin(admin.ModelAdmin):

    model = Journals
    list_display = [
        "journal_title",
        "journal_image",
        "description",
        "scope",
        "ISSN_PRINT",
        "DOI",
        "frequency",
        "publication_year",
        "special_issue",
        "journal_matrix",
    ]
    list_filter = ("scope", "frequency")


class VolumeAdmin(admin.ModelAdmin):

    model = Volume
    list_display = ["volume", "year"]
    list_filter = ["year"]


class IssueAdmin(admin.ModelAdmin):

    model = Issue
    list_display = ["issue", "status"]
    list_filter = ["status"]


class APCAdmin(admin.ModelAdmin):

    model = APC
    list_display = ["fixed_amount", "discount_options", "waive_off"]


class JournalMatrixAdmin(admin.ModelAdmin):

    model = JournalMatrix
    list_display = ["download", "views"]


class ArticleTypeAdmin(admin.ModelAdmin):

    model = ArticleType
    list_display = ["article_type"]


admin.site.register(Journals, JournalsAdmin)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(APC, APCAdmin)
admin.site.register(JournalMatrix, JournalMatrixAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Article)
admin.site.register(PageNumber)
