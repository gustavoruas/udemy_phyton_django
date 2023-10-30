from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.models import UserProfileInfo
from app1.forms import UserForm, UserProfileInfoForms

#imports needed for LOGIN/LOGOUT functionality
#from django.core.urlresolvers import reverse #deprecated, use django.urls
from django.urls import reverse
from django.contrib.auth.decorators import login_required    #notations
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,"app1/base.html")

#This like notation in SPring, calls a specific functionality
#This demands that to run this view, the user must be logged/authenticated
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("app1:index"))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        #authenticates the user here
        user_logged = authenticate(username =username , password=password)
        
        if user_logged:
            #check if user is not disabled
            if user_logged.is_active:
                #logs the user
                login(request,user_logged)
                #redirects with authentication
                return HttpResponseRedirect(reverse("app1:index"))
            else:
                return HttpResponse("Account is not Active")
        else:
            print("Failed login attempt with Username:{}".format(username) )
            return HttpResponse("Unable to login")
    
    else:
        return render(request,"app1/login.html",{})
            

def register_user(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForms(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            #criptographs the password that was informed in POST
            user.set_password(user.password)
            user.save()
            
            #saves profile information
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForms()
           
    #multiple dictionaries needed in the page.
    multi_dict = {"registered":registered
                  ,"user_form":user_form
                  ,"profile_form":profile_form
                  }
            
    return render(request,"app1/registration.html",multi_dict)

@login_required
def user_list(request):
    user_list = UserProfileInfo.objects.order_by("id")
    
    user_dict = {"user_dict":user_list}
    
    return render(request,"app1/user_list.html",user_dict)

def user_delete(request,id):
    user_to_delete = UserProfileInfo.objects.get(id=id)
    user_to_delete.delete()
    return redirect("app1:user_list")

