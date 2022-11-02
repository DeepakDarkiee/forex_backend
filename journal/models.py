import datetime

from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import FileExtensionValidator

from tinymce.models import HTMLField

from accounts.models import User

from journal.base_model import BaseModel


class Volume(BaseModel):
    
    def year_choices():
        
        return [(r, r) for r in range(1984, datetime.date.today().year + 1)]

    def current_year():
        
        return datetime.date.today().year

    volume = models.IntegerField()
    year = models.IntegerField(_("year"), choices=year_choices(), default=current_year)

    def __str__(self):
        return str(self.volume)


class Issue(BaseModel):

    STATUS_CHOICES = (("open", "open"), ("close", "close"))

    issue = models.IntegerField()
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.issue)


class APC(BaseModel):
    
    fixed_amount = models.CharField(max_length=100000)
    discount_options = models.CharField(max_length=2)
    waive_off = models.CharField(max_length=10000)

    def __str__(self):
        return self.fixed_amount


class PageNumber(models.Model):
    
    page_from = models.CharField(max_length=100000)
    page_to = models.CharField(max_length=2)

    def __str__(self):
        return self.page_from
    

class JournalMatrix(BaseModel):

    submission_count = models.IntegerField()
    publication_count = models.IntegerField()
    rejected_count = models.IntegerField()
    withdrawl_count = models.IntegerField()
    citation_count = models.IntegerField()
    h_5 = models.IntegerField()
    h_index = models.IntegerField()
    download = models.CharField(max_length=1000)
    views = models.CharField(max_length=1000)

    def __str__(self):
        return self.views


class ArticleType(BaseModel):
    
    article_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.article_type
    
class ScopeType(BaseModel):
    
    scope_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.scope_type


class JournalsManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(role="User.role.Author")

class Journals(BaseModel):
    def year_choices():
        
        return [(r, r) for r in range(1984, datetime.date.today().year + 1)]

    def current_year():
        
        return datetime.date.today().year


    SCOPE_CHOICES = (
        ("author", "author"),
        ("editor", "editor"),
        ("reviewer", "reviewer"),
        ("article_processing_charge", "article_processing_charge"),
    )

    FREQUENCY_CHOICES = (
        ("monthly", "monthly"),
        ("bimonthly", "bimonthly"),
        ("quaterly", "quaterly"),
        ("half_yearly", "half_yearly"),
        ("yearly", "yearly"),
    )
    journal_title = models.CharField(unique=True, max_length=200)
    journal_slug = models.SlugField(max_length = 200)
    journal_image = models.ImageField(upload_to="journal-image")
    is_lock =models.BooleanField(default=False)
    description = HTMLField()    
    scope = models.CharField(max_length=200,null=True, blank=True)
    article_type = models.ManyToManyField(ArticleType, null=True, blank=True)
    ISSN_PRINT = models.CharField(max_length=50,null=True, blank=True)  # must be 4-digits
    ISSN_ONLINE = models.CharField(max_length=50,null=True, blank=True)  # must be 4-digits
    DOI = models.CharField(max_length=1000)
    frequency = models.CharField(max_length=100, choices=FREQUENCY_CHOICES,default="monthly")
    publication_year = models.IntegerField(_("publication_year"), choices=year_choices(), default=current_year)
    volume = models.ForeignKey(
        Volume, on_delete=models.CASCADE, related_name="subscriber_volume"
    )
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name="subscriber_issue"
    )
    special_issue = models.CharField(max_length=2000,null=True, blank=True)
    journal_subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriber_journal",null=True, blank=True, 
    )
    journal_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriber_author_journal",null=True, blank=True,limit_choices_to={'role__name': "Author"}
    )
    journal_reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriber_reviewer_journal",null=True, blank=True,limit_choices_to={'role__name': "Reviewer"}
    )
    journal_matrix = models.ForeignKey(JournalMatrix,on_delete=models.CASCADE, related_name="journal_matrix",null=True, blank=True)


    
    def __str__(self):
        return self.journal_title
    