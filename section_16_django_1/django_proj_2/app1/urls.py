from django.urls import path
from app1 import views as app1_views

#must add variable in order to define dynamic URL building in HTML - TEMPLATE TAGGING -app_name ishardcoded
#when calling {% url 'app_name:name_from_path_param' %} - must receive the appname from settings.py
app_name = "app1"

urlpatterns = [
    path(r'',app1_views.index,name="index"),
    path(r'accessRecordsList/',app1_views.access_record_list, name="access_record_list"),
    path(r'websiteList/', app1_views.website_list, name="website_list"),
    path(r'topicList/', app1_views.topic_list, name="topic_list"),
    path(r'userList/', app1_views.user_list, name="user_list"),
    
    #forms
    path(r'userForm/',app1_views.user_form, name="user_form"),
    path(r'topicForm/', app1_views.topic_form, name="topic_form"),
    path(r'webpageForm/', app1_views.webpage_form, name="webpage_form"),
    
    #edits
    path(r'editTopic/<int:id>',app1_views.topic_edit, name="topic_edit"),
    path(r'editUser/<int:id>',app1_views.user_edit, name="user_edit"),
    path(r'editWebpage/<int:id>', app1_views.webpage_edit, name="webpage_edit"),
    
    #deletes
    path(r'deleteTopic/<int:id>', app1_views.topic_delete, name = "topic_delete"),
    path(r'deleteUser/<int:id>', app1_views.user_delete, name = "user_delete" ),
    path(r'deleteWebpage/<int:id>',app1_views.webpage_delete, name="webpage_delete" )
]
