from .models import Difficulty, Subject
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class DifficultyForm(forms.ModelForm):
    difficulty_name = forms.CharField(max_length=100,required=True)
        
    class Meta():
        model = Difficulty    
        fields = ["difficulty_name"]
        

class SubjectForm(forms.ModelForm):
    subject_name = forms.CharField(max_length=200, required=True)
    
    class Meta:
        model = Subject
        fields = ["subject_name"]
