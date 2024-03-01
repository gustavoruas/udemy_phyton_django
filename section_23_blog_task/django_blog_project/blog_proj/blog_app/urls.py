from django.urls import path, include
from blog_app import views as app_views

#must add variable in order to define dynamic URL building in HTML - TEMPLATE TAGGING -app_name ishardcoded
#when calling {% url 'app_name:name_from_path_param' %} - must receive the appname from settings.py
app_name = "blog_app"

urlpatterns = [
    path(r'', app_views.PostListView.as_view(), name="post_list_url"),
    path(r'about/', app_views.AboutView.as_view(), name="about_url"),   
    path(r'post/<int:pk>/', app_views.PostDetailView.as_view(), name="post_detail_url" ) ,
    path(r'post/new/', app_views.PostCreateView.as_view(), name = "post_create_url"),
    path(r'post/update/<int:pk>/', app_views.PostUpdateView.as_view(), name = "post_update_url"),
    path(r'post/delete/<int:pk>/', app_views.PostDeleteView.as_view(), name = "post_delete_url"),
    path(r'drafts/', app_views.DraftListView.as_view(), name = "post_draft_url"),
    path(r'post/<int:pk>/comment/', app_views.add_comment_to_post, name="add_comment_to_post_url"),
    path(r'comment/<int:pk>/approve/', app_views.comment_approve,name="comment_approve_url"),
    path(r'comment/<int:pk>/remove/', app_views.comment_remove, name= "comment_remove_url"),
    path(r'post/<int:pk>/publish/', app_views.post_publish, name="post_publish_url"),
]


