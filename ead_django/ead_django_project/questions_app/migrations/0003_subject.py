# Generated by Django 4.2.4 on 2024-06-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0002_alter_difficulty_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tb_subject',
            },
        ),
    ]
