# Generated by Django 5.0.6 on 2024-06-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customizeable', '0004_customtheme_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtheme',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]