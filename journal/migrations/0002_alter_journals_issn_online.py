# Generated by Django 3.2 on 2022-05-29 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journals',
            name='ISSN_ONLINE',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]