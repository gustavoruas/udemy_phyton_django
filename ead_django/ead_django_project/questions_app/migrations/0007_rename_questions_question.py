# Generated by Django 4.2.4 on 2024-07-31 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0006_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
