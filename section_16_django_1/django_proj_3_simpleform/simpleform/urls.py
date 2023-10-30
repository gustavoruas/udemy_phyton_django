from django.urls import path
from simpleform import views as simpleform_views

urlpatterns = [
    path(r'',simpleform_views.index, name="index page"),
    path(r'simpleForm/', simpleform_views.simple_form, name="simple form")
]
