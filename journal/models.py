from django.db import models
from django.utils.translation import gettext as _

import datetime

from accounts.models import User



class Volume(models.Model):

    def year_choices():
        return [(r,r) for r in range(1984, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year

    volume = models.IntegerField()
    open_year = models.IntegerField(_('year'), choices=year_choices(), default=current_year)
    close_year = models.IntegerField(_('year'), choices=year_choices(), default=current_year)


class Issue(models.Model):
    issue = models.IntegerField()
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)

class APC(models.Model):
    fixed_amount = models.CharField(max_length=100000)
    discount_options = models.CharField(max_length=2)
    waive_off = models.CharField(max_length=10000)
# Create your models here.

class JournalMatrix(models.Model):

    submission_count = models.IntegerField()
    publication_count = models.IntegerField()
    rejected_coount = models.IntegerField()
    withdrawl_coount = models.IntegerField()
    citation_coount = models.IntegerField()
    h_5 = models.IntegerField()
    h_index = models.IntegerField()
    download = models.CharField(max_length=1000)
    views = models.CharField(max_length=1000)

    def __str__(self):
        return self.views


class Journals(models.Model):

    SCOPE_CHOICES = (
    ("author", "author"),
    ("editor", "editor"),
    ("reviewer", "reviewer"),
    ("article_processing_charge", "article_processing_charge")
)

    ARTICLE_TYPE = (
    ("book_review", "book_review"),
    ("clinical_case_study", "clinical_case_study"),
    ("clinical_trial", "clinical_trial"),
    ("dissertation_report", "dissertation_report"),
    ("letters", "letters"),
    ("opnion", "opnion"),
    ("research_article", "research_article"),
    ("review_article", "review_article"),
    ("survey_report", "survey_report"),
    ("conference_report", "conference_report"),
)

    FREQUENCY_CHOICES = (
    ("monthly", "monthly"),
    ("bimonthly", "bimonthly"),
    ("quaterly", "quaterly"),
    ("half_yearly", "half_yearly"),
    ("yearly", "yearly"),
)


    journal_id = models.IntegerField(null=True, blank=True)
    journal_title = models.CharField(unique=True,max_length=200)
    journal_image = models.ImageField(upload_to="journal-image")
    description = models.TextField()
    scope = models.CharField(max_length=100 , choices=SCOPE_CHOICES)
    article_type = models.CharField(max_length=100,choices=ARTICLE_TYPE)
    ISSM_PRINT = models.IntegerField() # must be 4-digits
    ISSM_ONLINE = models.IntegerField() # must be 4-digits
    DOI = models.CharField(max_length=1000)
    frequency = models.CharField(max_length=100, choices=FREQUENCY_CHOICES)
    publication_year = models.CharField(max_length=4)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    special_issue = models.CharField(max_length=2000)
    journal_subscriber = models.ForeignKey(User, on_delete=models.CASCADE,related_name="subscriber_journal")
    journal_author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="author_journal")
    journal_reviewer = models.ForeignKey(User, on_delete=models.CASCADE,related_name="reviewer_journal")
    journal_matrix = models.CharField(max_length=100)


    




