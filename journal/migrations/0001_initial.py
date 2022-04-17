# Generated by Django 4.0.2 on 2022-04-17 08:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import journal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_amount', models.CharField(max_length=100000)),
                ('discount_options', models.CharField(max_length=2)),
                ('waive_off', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.IntegerField()),
                ('open_date', models.DateField(blank=True, null=True)),
                ('close_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('open', 'open'), ('close', 'close')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JournalMatrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_count', models.IntegerField()),
                ('publication_count', models.IntegerField()),
                ('rejected_count', models.IntegerField()),
                ('withdrawl_count', models.IntegerField()),
                ('citation_count', models.IntegerField()),
                ('h_5', models.IntegerField()),
                ('h_index', models.IntegerField()),
                ('download', models.CharField(max_length=1000)),
                ('views', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PageNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_from', models.CharField(max_length=100000)),
                ('page_to', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField()),
                ('year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=journal.models.Volume.current_year, verbose_name='year')),
            ],
        ),
        migrations.CreateModel(
            name='Journals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_id', models.IntegerField(blank=True, null=True)),
                ('journal_title', models.CharField(max_length=200, unique=True)),
                ('journal_image', models.ImageField(upload_to='journal-image')),
                ('description', models.TextField()),
                ('scope', models.CharField(choices=[('author', 'author'), ('editor', 'editor'), ('reviewer', 'reviewer'), ('article_processing_charge', 'article_processing_charge')], max_length=100)),
                ('ISSN_PRINT', models.CharField(max_length=50)),
                ('ISSN_ONLINE', models.IntegerField(blank=True, null=True)),
                ('DOI', models.CharField(max_length=1000)),
                ('frequency', models.CharField(choices=[('monthly', 'monthly'), ('bimonthly', 'bimonthly'), ('quaterly', 'quaterly'), ('half_yearly', 'half_yearly'), ('yearly', 'yearly')], max_length=100)),
                ('publication_year', models.CharField(max_length=4)),
                ('special_issue', models.CharField(max_length=2000)),
                ('journal_matrix', models.CharField(max_length=100)),
                ('article_type', models.ManyToManyField(blank=True, null=True, to='journal.ArticleType')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_issue', to='journal.issue')),
                ('journal_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_author_journal', to=settings.AUTH_USER_MODEL)),
                ('journal_reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_reviewer_journal', to=settings.AUTH_USER_MODEL)),
                ('journal_subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_journal', to=settings.AUTH_USER_MODEL)),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_volume', to='journal.volume')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.CharField(max_length=225, unique=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('abstract', models.CharField(max_length=300)),
                ('keywords', models.CharField(max_length=225)),
                ('funding_source', models.CharField(choices=[('self', 'self'), ('institute', 'institute'), ('research_agancy', 'research_agancy'), ('other', 'other')], max_length=100)),
                ('upload', models.FileField(upload_to='foo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'zip'])])),
                ('supplementary_file', models.FileField(upload_to='foo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'zip'])])),
                ('copyright_form', models.FileField(upload_to='foo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf'])])),
                ('apc_receipt', models.CharField(blank=True, max_length=255, null=True)),
                ('reviewer_report', models.FileField(upload_to='foo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('published_article', models.FileField(upload_to='foo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('published_xml', models.FileField(upload_to='foo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xml'])])),
                ('published_html', models.FileField(upload_to='foo/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html'])])),
                ('date_of_submission', models.DateField()),
                ('date_of_acceptance', models.DateField()),
                ('date_of_published', models.DateField()),
                ('volume', models.CharField(max_length=225)),
                ('issue', models.CharField(max_length=225)),
                ('special_issue', models.CharField(max_length=225)),
                ('doi', models.CharField(max_length=225)),
                ('article_status', models.CharField(choices=[('desc_rejected', 'desc_rejected'), ('revised_submission_required', 'revised_submission_required'), ('editor_assign_to_mamuscript', 'editor_assign_to_mamuscript'), ('mamuscript_under_peer_review_process', 'mamuscript_under_peer_review_process'), ('revision_1_required', 'revision_1_required'), ('revision_2_required', 'revision_2_required'), ('peer_reviewed_completed', 'peer_reviewed_completed'), ('copyright_from_submission_required', 'copyright_from_submission_required'), ('article_accpeted_from_publication', 'article_accpeted_from_publication'), ('rejected_after_peer_reviewed', 'rejected_after_peer_reviewed'), ('withdrawl', 'withdrawl'), ('payment_pending', 'payment_pending'), ('payment_verified', 'payment_verified'), ('preparing_gallery_proof', 'preparing_gallery_proof'), ('article_in_press', 'article_in_press'), ('article_published', 'article_published')], max_length=100)),
                ('citation', models.CharField(max_length=225)),
                ('download_count', models.CharField(max_length=225)),
                ('view_count', models.CharField(max_length=225)),
                ('multiple_image_in', models.CharField(max_length=225)),
                ('article_type', models.ManyToManyField(to='journal.ArticleType')),
                ('author_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_author_details', to=settings.AUTH_USER_MODEL)),
                ('page_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_page_number', to='journal.pagenumber')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_scope', to='journal.journals')),
            ],
        ),
    ]
