# Generated by Django 2.2.14 on 2020-07-19 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gogoanime', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VideoLink',
            new_name='Link',
        ),
        migrations.RenameModel(
            old_name='VideoSite',
            new_name='Site',
        ),
    ]