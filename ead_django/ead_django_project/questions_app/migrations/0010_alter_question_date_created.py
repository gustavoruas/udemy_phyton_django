# Generated by Django 4.2.4 on 2024-07-31 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0009_alter_question_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(default=datetime.date.today, null=True),
        ),
    ]
