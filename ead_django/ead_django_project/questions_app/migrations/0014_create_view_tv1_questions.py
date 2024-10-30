from django.db import migrations

# Custom Migration SQL create object.
class Migration(migrations.Migration):
    
    dependencies = [
        ('questions_app', '0013_alter_question_date_updated')
    ]
    
    operations = [
        migrations.RunSQL(
                """
                CREATE VIEW tv1_questions
                AS
                SELECT 
                  tq.question_id,
                  strftime('%m-%d-%Y %H:%M', tq.date_created) as date_created,
                  tq.description,
                  tq.active,
                  td.difficulty_name, 
                  ts.subject_name 
                FROM tb_questions tq 
                --LEFT join on column in the table that you want to return everything, the ooposite returns null if no join
                LEFT JOIN tb_difficulty td ON tq.question_difficulty_id = td.difficulty_id
                LEFT JOIN tb_subject ts  ON   tq.question_subject_id = ts.subject_id
                ;     
                """
            ,reverse_sql="DROP VIEW IF EXISTS tv1_questions;"
        )
    ]

