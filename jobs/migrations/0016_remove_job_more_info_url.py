# Generated by Django 2.2.1 on 2019-11-21 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_job_detail_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='more_info_url',
        ),
    ]
