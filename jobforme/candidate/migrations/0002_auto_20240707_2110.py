# Generated by Django 3.1.14 on 2024-07-07 15:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20240707_2110'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myjoblist',
            new_name='MyApplyJobList',
        ),
    ]
