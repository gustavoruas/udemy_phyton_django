from django.urls import path
from app1 import views as app1_views


# for calling via #when calling {% url 'app_name:name_from_path_param' %} 
#need the below
app_name = "app1"

urlpatterns = [
    path(r'',app1_views.index,name="index"),
    
    path(r'register/',app1_views.register_user,name="register_user"),
    path(r'user_login/',app1_views.user_login,name="user_login"),
    path(r'logout/',app1_views.user_logout,name="logout"),
    
    #list
    path(r'userProfileList/', app1_views.user_list,name="user_list"),
    
    #delete
    path(r'userDelete/<int:id>', app1_views.user_delete,name="user_delete")
]
