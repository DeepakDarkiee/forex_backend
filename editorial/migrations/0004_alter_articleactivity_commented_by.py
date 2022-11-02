# Generated by Django 3.2.16 on 2022-11-02 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editorial', '0003_auto_20221103_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleactivity',
            name='commented_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 2}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='editor_article_feed', to=settings.AUTH_USER_MODEL),
        ),
    ]
