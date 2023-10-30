from django.shortcuts import render
from django.http import HttpResponse
from simpleform import forms   #import form class into views 

# Create your views here.

def index(request):
    title_text = {"title_text":"This is the Index page for Simpleform"}
    
    return render(request,"simpleform/index.html", title_text)

def simple_form(request):
    simpleform = forms.FormName()       
    
    #If form gets POST with form info
    if request.method == "POST":
        form_post = forms.FormName(request.POST)
        
        #checks if the form object posted is valid
        if form_post.is_valid():
            print("Post successful")            
            #cleaned_data cleans return info from posted field.
            print("Name: " + form_post.cleaned_data["name"])       
            print("email: " + form_post.cleaned_data["email"])   
            print("text: " + form_post.cleaned_data["text"])
        #In order for VALIDATOR in Forms.py to work, the same Forms object from post must be returned.
        else:
            simpleform = form_post   #forms.FormName()
                    
    form_dict = {"form_dict":simpleform}
    
    return render(request, "simpleform/simpleform_page.html",form_dict)

