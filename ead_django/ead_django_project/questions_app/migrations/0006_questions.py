# Generated by Django 4.2.4 on 2024-07-31 22:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_app', '0005_alter_difficulty_difficulty_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('question_html_text', tinymce.models.HTMLField()),
                ('active', models.CharField(default='Y', max_length=1)),
                ('date_created', models.TimeField(default=django.utils.timezone.now, null=True)),
                ('date_updated', models.TimeField(blank=True, null=True)),
                ('question_difficulty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_difficulties', to='questions_app.difficulty')),
                ('question_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_subjects', to='questions_app.subject')),
            ],
            options={
                'db_table': 'tb_questions',
            },
        ),
    ]