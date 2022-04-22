import datetime

from django.db import models  # from djmoney.models.fields import MoneyField
from django.utils.translation import gettext as _
from django.core.validators import FileExtensionValidator

from accounts.models import User

# Create your models here.


class Volume(models.Model):
    def year_choices():

        return [(r, r) for r in range(1984, datetime.date.today().year + 1)]

    def current_year():

        return datetime.date.today().year

    volume = models.IntegerField()
    year = models.IntegerField(_("year"), choices=year_choices(), default=current_year)

    def __str__(self):
        return str(self.volume)


class Issue(models.Model):

    STATUS_CHOICES = (("open", "open"), ("close", "close"))

    issue = models.IntegerField()
    open_date = models.DateField(null=True, blank=True)
    close_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.issue)


class APC(models.Model):

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


class JournalsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role="User.role.Author")


class Journals(models.Model):

    SCOPE_CHOICES = (
        ("author", "author"),
        ("editor", "editor"),
        ("reviewer", "reviewer"),
        ("article_processing_charge", "article_processing_charge"),
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
    is_lock = models.BooleanField(default=False)
    journal_id = models.IntegerField(null=True, blank=True)
    journal_title = models.CharField(unique=True, max_length=200)
    journal_image = models.ImageField(upload_to="journal-image")
    description = models.TextField()
    scope = models.CharField(max_length=200)
    article_type = models.ManyToManyField(ArticleType, null=True, blank=True)
    ISSN_PRINT = models.CharField(
        max_length=50, null=True, blank=True
    )  # must be 4-digits
    ISSN_ONLINE = models.IntegerField()  # must be 4-digits
    DOI = models.CharField(max_length=1000)
    frequency = models.CharField(max_length=100, choices=FREQUENCY_CHOICES)
    publication_year = models.CharField(max_length=4)
    volume = models.ForeignKey(
        Volume, on_delete=models.CASCADE, related_name="subscriber_volume"
    )
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, related_name="subscriber_issue"
    )
    special_issue = models.CharField(max_length=2000, null=True, blank=True)
    journal_subscriber = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriber_journal",
        null=True,
        blank=True,
    )
    journal_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriber_author_journal",
        null=True,
        blank=True,
    )
    journal_reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriber_reviewer_journal",
        null=True,
        blank=True,
    )
    journal_matrix = models.ForeignKey(
        JournalMatrix,
        on_delete=models.CASCADE,
        related_name="journal_matrix",
        null=True,
        blank=True,
    )

    objects = models.Manager()

    user_role_objects = JournalsManager()

    def __str__(self):
        return self.journal_title


class Article(models.Model):

    FUNDINFG_SOURCE = (
        ("self", "self"),
        ("institute", "institute"),
        ("research_agancy", "research_agancy"),
        ("other", "other"),
    )

    ArticleStatus = (
        ("desc_rejected", "desc_rejected"),
        ("revised_submission_required", "revised_submission_required"),
        ("editor_assign_to_mamuscript", "editor_assign_to_mamuscript"),
        (
            "mamuscript_under_peer_review_process",
            "mamuscript_under_peer_review_process",
        ),
        ("revision_1_required", "revision_1_required"),
        ("revision_2_required", "revision_2_required"),
        ("peer_reviewed_completed", "peer_reviewed_completed"),
        ("copyright_from_submission_required", "copyright_from_submission_required"),
        ("article_accpeted_from_publication", "article_accpeted_from_publication"),
        ("rejected_after_peer_reviewed", "rejected_after_peer_reviewed"),
        ("withdrawl", "withdrawl"),
        ("payment_pending", "payment_pending"),
        ("payment_verified", "payment_verified"),
        ("preparing_gallery_proof", "preparing_gallery_proof"),
        ("article_in_press", "article_in_press"),
        ("article_published", "article_published"),
    )
    paper_id = models.CharField(max_length=225, unique=True)
    title = models.CharField(max_length=100, unique=True)
    refrence = models.TextField(null=True, blank=True)
    # article_type = models.ForeignKey(
    #     Journals, on_delete=models.CASCADE, related_name="article_type"
    # )
    article_type = models.ManyToManyField(ArticleType)
    journal = models.ForeignKey(
        Journals, on_delete=models.CASCADE, related_name="article_scope"
    )
    abstract = models.CharField(max_length=300)
    keywords = models.CharField(max_length=225)
    author_details = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_author_details"
    )
    funding_source = models.CharField(max_length=100, choices=FUNDINFG_SOURCE)
    upload = models.FileField(
        upload_to="foo/",
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "zip"])],
    )
    supplementary_file = models.FileField(
        upload_to="foo/",
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "zip"])],
    )
    copyright_form = models.FileField(
        upload_to="foo/",
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "pdf"])],
    )
    # apc_receipt = models.FileField(
    #     upload_to="foo/",
    #     validators=[FileExtensionValidator(allowed_extensions=["pdf", "img"])],
    # )
    apc_receipt = models.CharField(max_length=255, null=True, blank=True)
    reviewer_report = models.FileField(
        upload_to="foo/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "pdf",
                ]
            )
        ],
    )
    published_article = models.FileField(
        upload_to="foo/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "pdf",
                ]
            )
        ],
    )
    published_xml = models.FileField(
        upload_to="foo/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "xml",
                ]
            )
        ],
    )
    published_html = models.FileField(
        upload_to="foo/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "html",
                ]
            )
        ],
    )
    date_of_submission = models.DateField()
    date_of_acceptance = models.DateField()
    date_of_published = models.DateField()
    volume = models.CharField(max_length=225)
    issue = models.CharField(max_length=225)
    special_issue = models.CharField(max_length=225)
    page_number = models.ForeignKey(
        PageNumber, on_delete=models.CASCADE, related_name="article_page_number"
    )
    doi = models.CharField(max_length=225)
    article_status = models.CharField(max_length=100, choices=ArticleStatus)
    citation = models.CharField(max_length=225)
    download_count = models.CharField(max_length=225)
    view_count = models.CharField(max_length=225)
    multiple_image_in = models.CharField(max_length=225)
