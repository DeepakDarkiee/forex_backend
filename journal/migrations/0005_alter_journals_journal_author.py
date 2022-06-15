# Generated by Django 3.2 on 2022-05-31 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0004_alter_journals_publication_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journals',
            name='journal_author',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'Author'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_author_journal', to=settings.AUTH_USER_MODEL),
        ),
    ]