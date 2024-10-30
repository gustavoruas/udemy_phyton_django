from django.urls import path 
from questions_app import views as question_views

app_name = "questions_app"

urlpatterns = [
    #----------------------------------------------------------Difficulty URLS
    path(r'difficulties/',question_views.DifficultyListView.as_view(),name="difficulty_list_url"),
    path(r'difficulties/<int:pk>', question_views.DifficultyDetailView.as_view(), name="difficulty_detail_url"),
    path(r'difficulties/new/', question_views.DifficultyCreateView.as_view(),name="difficulty_create_url"),
    path(r'difficulties/update/<int:pk>', question_views.DifficultyUpdateView.as_view(),name="difficulty_update_url"),
    path(r'difficulties/delete/<int:pk>', question_views.DifficultyDeleteView.as_view(),name="difficulty_delete_url"),
    path(r'difficulties/json',question_views.DifficultyJson, name="difficulty_list_json_url"),

    #----------------------------------------------------------Subject URLS
    path(r'subjects/',question_views.SubjectListView.as_view(),name="subject_list_url"),
    path(r'subjects/<int:pk>', question_views.SubjectDetailView.as_view(), name="subject_detail_url"),
    path(r'subjects/new/', question_views.SubjectCreateView.as_view(),name="subject_create_url"),
    path(r'subjects/update/<int:pk>', question_views.SubjectUpdateView.as_view(),name="subject_update_url"),
    path(r'subjects/delete/<int:pk>', question_views.SubjectDeleteView.as_view(),name="subject_delete_url"),
    
    #----------------------------------------------------------Answer URLS
    # as it is a child of Question, to be inlet written in question, must reference father as a parameter
    #in this case, with question_id    
    path(r'questions/<int:question_id>/answers/<int:pk>', question_views.AnswerDetailView.as_view(), name="answer_detail_url"),
    path(r'questions/<int:question_id>/answers/new/', question_views.AnswerCreateView.as_view(),name="answer_create_url"),
    #question_id is used as a reference to father object
    path(r'questions/<int:question_id>/answers/update/<int:pk>', question_views.AnswerUpdateView.as_view(),name="answer_update_url"),
    path(r'questions/<int:question_id>/answers/delete/<int:pk>', question_views.AnswerDeleteView.as_view(),name="answer_delete_url"), 
    #question_id referes as a mapping name, so it can be fetched in the JsonView function
    path(r'questions/<int:question_id>/answers/json',question_views.AnswerJson, name="answer_list_json_url"),
    
    path(r'questions/render_test',question_views.render_test1, name="question_render1"),
            
    #----------------------------------------------------------Question URLS
    path(r'questions/',question_views.QuestionListView.as_view(),name="question_list_url"),
    path(r'questions/<int:pk>', question_views.QuestionDetailView.as_view(), name="question_detail_url"),
    path(r'questions/new/', question_views.QuestionCreateView.as_view(),name="question_create_url"),
    path(r'questions/update/<int:pk>', question_views.QuestionUpdateView.as_view(),name="question_update_url"),
    path(r'questions/delete/<int:pk>', question_views.QuestionDeleteView.as_view(),name="question_delete_url"),
    path(r'questions/json',question_views.QuestionJson, name="question_list_json_url"),
    
    #----------------------------------------------------------Assessment URLS
    path(r'assessments/',question_views.AssessmentListView.as_view(), name="assessment_list_url"),
    path(r'assessments/<int:pk>', question_views.AssessmentDetailView.as_view(), name="assessment_detail_url"),
    path(r'assessments/new/', question_views.AssessmentCreateView.as_view(),name="assessment_create_url"),
    path(r'assessments/update/<int:pk>', question_views.AssessmentUpdateView.as_view(),name="assessment_update_url"),
    path(r'assessments/delete/<int:pk>', question_views.AssessmentDeleteView.as_view(),name="assessment_delete_url"),
    path(r'assessments/json',question_views.AssessmentJson, name="assessment_list_json_url"),
    
]

