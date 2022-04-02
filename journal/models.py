from django.db import models
from django.utils.translation import gettext as _
from accounts.models import User

import datetime





class Volume(models.Model):

    def year_choices():
        return [(r,r) for r in range(1984, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year

    volume = models.IntegerField()
    year = models.IntegerField(_('year'), choices=year_choices(), default=current_year)

    def __str__(self):
        return str(self.volume)

class Issue(models.Model):

    STATUS_CHOICES =(
        ('open','open'),
        ('close','close')
    )

    issue = models.IntegerField()
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.issue)

class APC(models.Model):
    fixed_amount = models.CharField(max_length=100000)
    discount_options = models.CharField(max_length=2)
    waive_off = models.CharField(max_length=10000)

    def __str__(self):
        return self.fixed_amount
# Create your models here.

class JournalMatrix(models.Model):

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

class ArticleType(models.Model):
    article_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.article_type

class Journals(models.Model):

    SCOPE_CHOICES = (
    ("author", "author"),
    ("editor", "editor"),
    ("reviewer", "reviewer"),
    ("article_processing_charge", "article_processing_charge")
)

#     ARTICLE_TYPE = (
#     ("book_review", "book_review"),
#     ("clinical_case_study", "clinical_case_study"),
#     ("clinical_trial", "clinical_trial"),
#     ("dissertation_report", "dissertation_report"),
#     ("letters", "letters"),
#     ("opnion", "opnion"),
#     ("research_article", "research_article"),
#     ("review_article", "review_article"),
#     ("survey_report", "survey_report"),
#     ("conference_report", "conference_report"),
# )

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
    article_type = models.ManyToManyField(ArticleType,null=True, blank=True)
    ISSN_PRINT = models.CharField(max_length=50) # must be 4-digits
    ISSN_ONLINE = models.IntegerField(max_length=50) # must be 4-digits
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

    def __str__(self):
        return self.journal_title




