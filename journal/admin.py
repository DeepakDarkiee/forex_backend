from django.contrib import admin

# Register your models here.
from journal.models import ArticleType, Journals,Volume,Issue,APC,JournalMatrix

admin.site.register(Journals)
admin.site.register(Volume)
admin.site.register(Issue)
admin.site.register(APC)
admin.site.register(JournalMatrix)
admin.site.register(ArticleType)

