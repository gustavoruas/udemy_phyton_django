import math
from django.shortcuts import render, get_list_or_404, redirect
from django.db.models.query import QuerySet
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView
                                  )
from .models import Difficulty, Subject
from .forms import DifficultyForm, SubjectForm
from questions_app.aux_library.json_datatables import json_datatable_data
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage #Needed for paging
from django.contrib.auth.decorators import login_required  #for Function based Views
from django.contrib.auth.mixins import LoginRequiredMixin  #for Class based Views
from django.http import JsonResponse


#----------------------------------------------------------------------------Difficulty
# Create your views here.
class DifficultyListView(LoginRequiredMixin,ListView):
    model = Difficulty
    #custom context
    context_object_name = "difficulty_list"
    template_name = "difficulty/difficulty_list.html"
    paginate_by =5
    
    #customize queryset
    def get_queryset(self):
        query = "SELECT * FROM tb_difficulty"
        
        #fetches get request from order column
        ordering = self.request.GET.get("orderby", None)        

        if ordering != None:
            query = query + " ORDER BY difficulty_name DESC" 
        else:
            query = query + " ORDER BY difficulty_name ASC"      
        
        
        diff_return = Difficulty.objects.raw(query)        
        #diff_return.order_by("difficulty_name")
        
        return diff_return
    

#@login_required
#returns Json to interact with datatables JS
def DifficultyJson(request):
    
    response = {}
    
    query = "SELECT * FROM tb_difficulty"     
    
    response = json_datatable_data(
        request,
        Difficulty,
        "tb_difficulty",
        query,
        ["difficulty_name"]    
    )  
    
    return JsonResponse(response)  


class DifficultyDetailView(LoginRequiredMixin, DetailView):
    model = Difficulty
    template_name = "difficulty/difficulty_detail.html"
    context_object_name = "difficulty_context"
    

class DifficultyCreateView(LoginRequiredMixin, CreateView):
    model=Difficulty
    form_class = DifficultyForm
    template_name = "difficulty/difficulty_form.html"       
    
    redirect_field_name = "difficulty/difficulty_list.html"
    
    #customizing context to render in template
    #Django default, context for form is named "form"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["difficulty_form"] = context["form"]     
        #defining a context to difer from Update/Create   
        context["is_update"] = False
        return context
    

class DifficultyUpdateView(LoginRequiredMixin, UpdateView):
    model = Difficulty
    form_class = DifficultyForm
    template_name = "difficulty/difficulty_form.html"
    context_object_name = "difficulty_context"
    redirect_field_name = "difficulty/difficulty_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["difficulty_form"] = context["form"] 
        #defining a context to difer from Update/Create   
        context["is_update"] = True       
        return context
    
    
class DifficultyDeleteView(LoginRequiredMixin, DeleteView):
    model = Difficulty
    template_name = "difficulty/difficulty_confirm_delete.html"
    context_object_name = "difficulty_context"
    success_url = reverse_lazy("questions_app:difficulty_list_url")
        

#----------------------------------------------------------------------------Subject
class SubjectListView(LoginRequiredMixin,ListView):
    model=Subject
    context_object_name = "subject_list"
    template_name = "subject/subject_list.html"
    
    #for pagination enabled, by default pagination context name is page_obj
    paginate_by = 5
    
    #custom query to return list
    def get_queryset(self):
        query = "SELECT * FROM tb_subject"
        
        ordering = self.request.GET.get("orderby",None)
        
        if ordering != None:
            query = query + " ORDER BY subject_name DESC"        
        else:
            query = query + " ORDER BY subject_name ASC"
                        
        #Running query, returning as a list of objects
        subject_return = Subject.objects.raw(query)
        
        return subject_return
        

class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = "subject/subject_detail.html"
    context_object_name = "subject_context"
    

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject/subject_form.html"
    
    redirect_field_name = "subject/subject_list.html"

    #customizing context to render in template
    #Django default, context for form is named "form"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subject_form"] = context["form"]
        #flag to identify UPDATE/CREATE
        context["is_update"] = False
        return context
    
    
class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject/subject_form.html"    
    context_object_name = "subject_context"
    redirect_field_name = "subject/subject_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subject_form"] = context["form"]
        context["is_update"] = True
        return context
    

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model=Subject
    template_name = "subject/subject_confirm_delete.html"
    context_object_name = "subject_context"
    success_url = reverse_lazy("questions_app:subject_list_url")



