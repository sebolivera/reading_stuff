# Generated by Django 3.2.4 on 2021-06-27 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readwrite', '0006_alter_user_favorites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
    ]
