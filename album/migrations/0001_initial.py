# Generated by Django 5.0.6 on 2024-06-02 14:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('img_banner', models.ImageField(null=True, upload_to='uploads/album/')),
                ('img_profile', models.ImageField(null=True, upload_to='uploads/album/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('release_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('totallike', models.IntegerField(default=0)),
                ('totalmusic', models.IntegerField(default=0)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_released', models.BooleanField(default=False)),
                ('is_disabled', models.BooleanField(default=False)),
                ('modified_by', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
