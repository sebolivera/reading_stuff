# Generated by Django 3.2.4 on 2021-06-26 18:45

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readwrite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
    ]
