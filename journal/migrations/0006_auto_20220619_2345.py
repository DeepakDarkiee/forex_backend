# Generated by Django 3.2 on 2022-06-19 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0005_alter_journals_journal_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author_details',
            field=models.ForeignKey(limit_choices_to={'role': 'Author'}, on_delete=django.db.models.deletion.CASCADE, related_name='article_author_details', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='journals',
            name='journal_reviewer',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'Reviewer'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_reviewer_journal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='journals',
            name='journal_subscriber',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'Subscriber'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_journal', to=settings.AUTH_USER_MODEL),
        ),
    ]