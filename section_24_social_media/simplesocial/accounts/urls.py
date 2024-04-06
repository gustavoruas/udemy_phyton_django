from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as account_views

app_name = "accounts_app"

urlpatterns = [
    path(r'login/'
         ,auth_views.LoginView.as_view(template_name="accounts/login.html")
         ,name="login_url"
         ),
    path(r'logout/',auth_views.LogoutView.as_view(),name="logout_url"),
    path(r'signup/',account_views.SignUp.as_view(),name="signup_url"),    
]




