from django.apps import AppConfig


class QuestionsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'questions_app'

    #in order to make visible the SQL/Python functions to the application, must register them here.
    #def ready(self):
    #    # Connect to SQLite
    #    conn = sqlite3.connect(settings.CUSTOM_DIR_DATABASE)
#
    #    # Register the custom function with SQLite, at memory time
    #    conn.create_function("replace_subject_ids", 1, 
    #                         lambda ids: models_functions.replace_subjects_by_id(conn, ids))
     