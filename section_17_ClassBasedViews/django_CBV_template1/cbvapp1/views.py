from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
# needed to implement Class Based Views
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView,                                 
                                )
from . import models  # from app dir, import models.py 


# calling views templates via Function
# def index(request):
#     return render(request,"cbvapp1/index.html")

# Calling templates via Class Based Views
class Index(TemplateView):
    # class attribute
    template_name = "cbvapp1/index.html"
    
    # *args - returns as a tuple
    # **kwargs - returns as a dictionary
    # class method as function def
    def get_context_data(self,**kwargs):
        # fetches all context references stired within template
        context = super().get_context_data(**kwargs)  ##returns them as a list
        context["header_context_2"] = "This text comes from a context dictionary inject"
        context["header_context_3"] = "This one too"
        return context

class SchoolListView(ListView):
    #defining a custom object to return, otherwise it returns "school"s_list (schools_list)
    #class model attribute hardcoded
    context_object_name = "dict_school_listview"  #this is used in HTML
    
    model = models.School   #references the models.py file     
    
    
class SchoolDetailView(DetailView):
    #Custom dictionary
    context_object_name = "dict_school_detailview"
    
    model = models.School
    template_name = "cbvapp1/school_detail.html"
    

class SchoolCreateView(CreateView):
    model = models.School
    #Need to specify which fields are allowed to be used in create funcion
    fields = ('school_id'
              ,'school_name'
              ,'principal'
              ,'school_address')
    #Specify webpage/template name
    template_name = "cbvapp1/school_form.html"
    
class SchoolUpdateView(UpdateView):
    model = models.School
    #Need to specify which fields are allowed to be used in update funcion
    fields = ('school_id'
              ,'school_name'
              ,'principal'
              ,'school_address')
    #Specify webpage/template name
    template_name = "cbvapp1/school_form.html"
    
class SchoolDeleteView(DeleteView):
    model = models.School

    #Custom dictionary
    context_object_name = "dict_school_delete"
         
    #attribute for redirecting to URL page when deleted successfully
    success_url = reverse_lazy("cbvapp1:school_list_url")
    
    template_name = "cbvapp1/school_confirm_delete.html"
    
    
    

class StudentUpdateView(UpdateView):
    model = models.Students
    context_object_name = "form_student"
        
    fields = (
         "student_id"
        ,"student_name"
        ,"age"
        ,"school"
    )
    
    template_name = "cbvapp1/student_form.html"
 
    
    
    