# Generated by Django 5.0.6 on 2024-06-09 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_rename_comment_commentreplylike_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentreplylike',
            old_name='reply',
            new_name='comment',
        ),
    ]