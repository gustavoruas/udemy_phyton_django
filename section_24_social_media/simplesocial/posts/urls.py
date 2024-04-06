from django.urls import path,reverse
from . import views as post_views

app_name = "posts"

urlpatterns = [
    path(r'',post_views.PostList.as_view(), name="post_all_url"),
    path(r'new/',post_views.CreatePost.as_view(),name="post_create_url"),
    path(r'by/(?P<username>[-\w]+)',post_views.UserPosts.as_view(),name="post_for_user_url"),
    path(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/',post_views.PostDetail.as_view(),name="post_single_url"),
    path(r'delete/(?P<pk>\d+)/',post_views.DeletePost.as_view(),name="post_delete_url")
]
