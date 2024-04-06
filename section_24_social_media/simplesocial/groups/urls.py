# Groups URL
from django.urls import path, include
from . import views as group_views

app_name = "groups"

urlpatterns = [
    path(r'',group_views.ListGroups.as_view(),name="group_all_url"),
    path(r'new/',group_views.CreateGroup.as_view(),name="group_create_url"),
    path(r'posts/in/(?P<slug>[-\w]+)/',
         group_views.SingleGroup.as_view(),
         name="group_single_url"),   
    path(r'join/(?P<slug>[-\w]+)/', group_views.JoinGroup.as_view(), name="group_join_url"),
    path(r'leave/(?P<slug>[-\w]+)/',group_views.LeaveGroup.as_view(), name = "group_leave_url"),
    
    
]



