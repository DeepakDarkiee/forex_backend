from pydoc import apropos
from re import T
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from tinymce.models import HTMLField

from accounts.models import User

from journal.models import Journals, PageNumber ,ArticleType

from journal.base_model import BaseModel
# Create your models here.


class Article(BaseModel):

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
    author_details = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="article_author_details",limit_choices_to={'role__name': "Author"}
    )
    editor_details = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_editor_details",limit_choices_to={'role__name': "Editor"},
        null=True,blank=True
    )
    funding_source = models.CharField(max_length=100, choices=FUNDINFG_SOURCE)
    upload = models.FileField(
        upload_to="foo/",
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "zip"])],
        null=True,blank=True
    )
    supplementary_file = models.FileField(
        upload_to="foo/",
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "zip"])],
        null=True,blank=True
    )
    copyright_form = models.FileField(
        upload_to="foo/",
        validators=[FileExtensionValidator(allowed_extensions=["doc", "docx", "pdf"])],
        null=True,blank=True
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
        null=True,blank=True
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
        null=True,blank=True
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
        null=True,blank=True
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
        null=True,blank=True
    )
    date_of_submission = models.DateField(null=True,blank=True)
    date_of_acceptance = models.DateField(null=True,blank=True)
    date_of_published = models.DateField(null=True,blank=True)
    volume = models.CharField(max_length=225,null=True,blank=True)
    issue = models.CharField(max_length=225,null=True,blank=True)
    special_issue = models.CharField(max_length=225)
    page_number = models.ForeignKey(
        PageNumber, on_delete=models.CASCADE, related_name="article_page_number",null=True,blank=True
    )
    doi = models.CharField(max_length=225,null=True,blank=True)
    article_status = models.CharField(max_length=100, choices=ArticleStatus)
    citation = models.CharField(max_length=225,null=True,blank=True)
    download_count = models.CharField(max_length=225,null=True,blank=True)
    view_count = models.CharField(max_length=225,null=True,blank=True)
    multiple_image_in = models.CharField(max_length=225,null=True,blank=True)

    def __str__(self):
        return self.title

STATUS_CHOICES = (
        ("Approved", "Approved"),
        ("Pending", "Pending"),
        ("Rejected", "Rejected"),
    )

class ArticleActivity(BaseModel):
    article = models.OneToOneField(
        Article, on_delete=models.CASCADE, related_name="article_activity"
    )
    status = models.CharField(choices=STATUS_CHOICES,default="Pending",max_length=10)
    comment = models.TextField(null=True,blank=True)
    commented_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="editor_article_feed",null=True, blank=True,limit_choices_to={'role': 2}
    )
    approved_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="Approver_article_feed",null=True, blank=True,
    )

    def __str__(self):
        return self.article.title

