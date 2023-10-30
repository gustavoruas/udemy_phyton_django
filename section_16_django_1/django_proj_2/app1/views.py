from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from app1.models import Webpage, Accessrecord, Topic, User
from app1.forms import *

#Full CRUD example
#https://www.javatpoint.com/django-crud-application    
#https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform


# Create your views here.

def index(request):
    #adding injection text
    title_text = {"title_text":"This is the index page for app1"}
    
    return render(request,"app1/base.html",title_text)

def access_record_list(request):
    #Creating injetion object from  the models in the project
    access_record_list = Accessrecord.objects.order_by("date")
    
    access_record_dict = {"access_record_dict":access_record_list}
    
    return render(request,"app1/access_records_list.html",access_record_dict)
    

def user_list(request):
    user_list = User.objects.order_by("first_name")
    
    user_dict = {"user_dict":user_list}
    
    return render(request, "app1/user_list.html", user_dict)

def user_form(request):
    user_form_var = UserForm()
    
    if request.method == "POST":
        user_form_var = UserForm(request.POST)
        
        if user_form_var.is_valid():
            
            #with commit it commits into DB
            user_form_var.save(commit=True)            
            #Other view functions can be called in order to redirect to another page
            #return index(request)
            
            #clears out UserForm object
            user_form_var = UserForm()
            
    # if form validation returns false, return empy form with errors
    else:
        user_form_var = UserForm()                   
    
    user_form_dict = {"user_form_dict":user_form_var}    
    return render(request,"app1/userform_page.html",user_form_dict)

def user_edit(request, id):#ID param must be same NAME of Model attribute/DB column name
    selected_user = User.objects.get(id=id)
    
    if request.method == "POST":
        user_form_return = UserForm(request.POST, instance=selected_user)
        
        if user_form_return.is_valid():
            user_form_return.save(commit=True)
            return redirect("app1:user_list")                   
        
    else: #returns formobj loaded ith obj
        user_form_return = UserForm(instance=selected_user)
        user_form_dict = {"user_form_dict":user_form_return}
        return render(request,"app1/useredit_page.html",user_form_dict)

def user_delete(request,id):
    user_to_delete = User.objects.get(id=id)
    user_to_delete.delete()
    return redirect("app1:user_list")

def topic_list(request):
    topic_list = Topic.objects.order_by("top_name")
    
    topic_dict = {"topic_dict":topic_list}
    
    return render(request,"app1/topic_list.html", topic_dict)

def topic_form(request):
    topic_form = TopicForm()
    
    if request.method == "POST":
        topic_form = TopicForm(request.POST)
        
        if topic_form.is_valid():
            topic_form.save(commit=True)
            topic_form=TopicForm()       
        else:
            topic_form=TopicForm()
            
    else:
        topic_form=TopicForm()
    
    topic_form_dict = {"topic_form_dict":topic_form}
    
    return render(request,"app1/topicform_page.html",topic_form_dict)

#Full CRUD example
#https://www.javatpoint.com/django-crud-application    
#https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django/7349667-update-a-model-object-with-a-modelform
def topic_edit(request,id):  #ID param must be same NAME of Model attribute/DB column name
    topic = Topic.objects.get(id=id) 
    
    #For posting changes on edit
    if request.method == "POST":
        ##gets updated posted object
        topic_form_return = TopicForm(request.POST, instance=topic)
        
        if topic_form_return.is_valid():
            topic_form_return.save()
            #insted of render, redirect navigates to URL
            return redirect("app1:topic_list")
        
    # this is for loading object into fomr and page
    else:
        topic_form_return = TopicForm(instance=topic)
        
        topic_form_dict = {"topic_form_dict":topic_form_return}
         
        #returns edit page populated with loaded object ID
        return render(request, "app1/topicedit_page.html",topic_form_dict)  
      
            
def topic_delete(request,id):#ID param must be same NAME of Model attribute/DB column name
    topic_to_delete = Topic.objects.get(id=id)
    topic_to_delete.delete()        
    return redirect("app1:topic_list")

def website_list(request):
    website_list = Webpage.objects.order_by("name")
    
    webpage_dict = {"webpage_dict":website_list}
    
    return render(request, "app1/website_list.html", webpage_dict)


def webpage_form(request):
    webpage_form = WebpageForm()
    
    if request.method == "POST":
        webpage_form = WebpageForm(request.POST)
        
        if webpage_form.is_valid():
            webpage_form.save()            
        else:
            webpage_form = WebpageForm()            
    else:
        webpage_form = WebpageForm()
        
    webpage_form_dict = {"webpage_form_dict":webpage_form}
    
    return render(request,"app1/webpageform_page.html",webpage_form_dict)

def webpage_edit(request,id):
    webpage = Webpage.objects.get(id=id)
    
    if request.method == "POST":
        webpage_form = WebpageForm(request.POST, instance=webpage)
        
        if webpage_form.is_valid():
            webpage_form.save()
            return redirect("app1:website_list")
                    
    else:
        webpage_form = WebpageForm(instance=webpage)
        webpage_dict = {"webpage_dict":webpage_form}
        return render(request,"app1/webpageedit_page.html",webpage_dict)
        
def webpage_delete(request,id):
    webpage_delete = Webpage.objects.get(id=id)
    webpage_delete.delete()
    return redirect("app1:website_list")


        