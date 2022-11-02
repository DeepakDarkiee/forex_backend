# Generated by Django 3.2.16 on 2022-11-02 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0002_auto_20221101_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journals',
            name='journal_author',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_author_journal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='journals',
            name='journal_reviewer',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 3}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_reviewer_journal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='journals',
            name='journal_subscriber',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_journal', to=settings.AUTH_USER_MODEL),
        ),
    ]