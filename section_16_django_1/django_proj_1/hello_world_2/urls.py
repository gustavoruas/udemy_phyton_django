from django.urls import path
from hello_world_2 import views as app2_views

#This is called in the main project urls.py file.
urlpatterns = [
    path(r'main_page/', app2_views.index, name="App 2 Home"),
    path(r'html_page1/',app2_views.page2,name="Html Page"),
    path(r'help/', app2_views.help_page,name="Help Page")
]