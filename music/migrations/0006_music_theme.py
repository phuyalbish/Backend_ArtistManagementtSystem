# Generated by Django 5.0.6 on 2024-06-11 04:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customizeable', '0002_remove_customtheme_user_customtheme_is_deleted_and_more'),
        ('music', '0005_comment_created_at_like_is_like_music_img_cover_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='theme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customizeable.customtheme'),
        ),
    ]