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
     
]

