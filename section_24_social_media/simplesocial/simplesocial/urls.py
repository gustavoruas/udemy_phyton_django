"""
URL configuration for simplesocial project.

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
from . import views as social_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',social_views.HomePage.as_view(),name="index_url"),
    #connecting with ACCPUNTS app
    path(r'accounts/',include("accounts.urls",namespace="accounts_namspace")),
    #injects all needed auth dependencies from django, that are configured in Accounts app
    path(r'accounts/',include("django.contrib.auth.urls")),
    path(r'posts/',include("posts.urls",namespace="posts_namespace")),
    path(r'groups/',include("groups.urls",namespace="groups_namespace")),
    path(r'test/', social_views.TestPage.as_view(), name = "test_url"),
    path(r'test/', social_views.ThanksPage.as_view(), name = "thanks_url"),
]

#Check if DEBUG in settings.py is enabled
if settings.DEBUG:
    import debug_toolbar
    
    urlpatterns = [
        path(r'__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns  #concatenats new URL 
    


    