from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<b>This is another app page</b><h1></h1>")

def page2(request):
    #this is a inserted code from python into HTML. the tag in HTML must be same name in here
    page_dictionary = {"inserted_text":"This text is coming from:" + str(__file__)}
    
    #As in settings the folder for hello_world_2 only points to template folder
    #you must add the folder name/filename.html before
    #if mapped in project settings.py, no need to add here
    return render(request,"hello_world_2/html_page_1.html",context=page_dictionary) 

def help_page(request):
    page_dictionary = {
        "help_text":"This is the help page"
    }
    return render(request,"hello_world_2/help_page.html",context=page_dictionary)
