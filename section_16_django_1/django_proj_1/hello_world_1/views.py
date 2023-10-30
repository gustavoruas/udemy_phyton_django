from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#First custom View/Page of the application
def index(request):
    return HttpResponse("Hello World from Page")


