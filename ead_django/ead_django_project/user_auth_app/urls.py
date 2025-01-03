from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_auth_app_views
from django.views.generic import TemplateView

app_name = "user_auth_app"

urlpatterns = [
    path(
        r'login/',
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login_url"
    ),
    path(r'logout/',auth_views.LogoutView.as_view(),name="logout_url"),
    #path(r'signup/',user_auth_app_views.Signup.as_view(), name="signup_url"),
    path(r'signup/',user_auth_app_views.signup_user, name="signup_url"),
    path(r'change_password/'
         ,user_auth_app_views.CustomPasswordChangeView.as_view(template_name="change_password.html",
                                               success_url="/"
                                            )
         ,name="change_password_url"),
    #directing straight to a HTML page, without calling a class View, using TemplateView
    path(r'permission_denied/', TemplateView.as_view(template_name="permission_denied.html"),name="permission_denied")
    
]
