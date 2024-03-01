from django.urls import path
from cbvapp1 import views as cbvapp1_views

#for dynamic URL to work in templates {% url 'app_name:name_from_path_param' %}
app_name = "cbvapp1"

urlpatterns = [
    # Url for a function based Template
    # path(r'', cbvapp1_views.index,name="index"),
    
    #Url for a Class Based View
    path(r'',cbvapp1_views.Index.as_view(),name="index"),
    path(r'schoolList/',cbvapp1_views.SchoolListView.as_view(),name="school_list_url"),
    
    #detail page, where ID of school is used in the URL
    #P<pk> returns the id of School
    #path(r'^(?P<pk>[-\w]+)/$', cbvapp1_views.SchoolDetailView.as_view(),name="school_details")
    path(r'schoolList/<int:pk>/', cbvapp1_views.SchoolDetailView.as_view(),name="school_details_url"),
    path(r'create/', cbvapp1_views.SchoolCreateView.as_view(),name="school_create_url"),
    path(r'update/<int:pk>/', cbvapp1_views.SchoolUpdateView.as_view(),name="school_update_url"),
    path(r'delete/<int:pk>/', cbvapp1_views.SchoolDeleteView.as_view(),name="school_delete_url"),


    #students
    path(r'student/update/<int:pk>',cbvapp1_views.StudentUpdateView.as_view(),name="student_update_url")

]
