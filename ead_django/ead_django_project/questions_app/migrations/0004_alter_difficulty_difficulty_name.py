# Generated by Django 4.2.4 on 2024-07-31 20:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0003_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficulty',
            name='difficulty_name',
            field=tinymce.models.HTMLField(),
        ),
    ]