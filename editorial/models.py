from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from tinymce.models import HTMLField

from accounts.models import User

from journal.models import Journals, PageNumber ,ArticleType

# Create your models here.


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
    title = models.CharField(max_length=100, unique=True)
    article_slug = models.SlugField(max_length=225)
    refrence = HTMLField()
    article_type = models.ManyToManyField(ArticleType)
    journal = models.ForeignKey(
        Journals, on_delete=models.CASCADE, related_name="article_scope"
    )
    abstract = models.CharField(max_length=300)
    keywords = models.CharField(max_length=225)
    author_details = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_author_details",limit_choices_to={'role': 'Author'}
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
