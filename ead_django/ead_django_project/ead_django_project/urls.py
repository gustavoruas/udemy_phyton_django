"""
URL configuration for ead_django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as ead_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="admin_url"),
    path(r'', ead_view.IndexPage.as_view(), name="index_url"),
    #connecting with ACCOUNTS app
    path(r'accounts/',include("user_auth_app.urls", namespace="user_auth_namespace")),
    #connecting question_app
    path(r'ead/',include("questions_app.urls", namespace="questions_namespace")),
    path(r'accounts/',include("django.contrib.auth.urls")),
    #Adding tinyMCE via django
    path(r'tinymce/', include('tinymce.urls')),
]

#Enabling debug tab if enabled in settings.py
if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
