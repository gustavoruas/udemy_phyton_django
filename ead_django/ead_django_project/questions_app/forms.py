import datetime
from .models import Difficulty, Subject, Answer, Question
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE

class DifficultyForm(forms.ModelForm):
    
    difficulty_name = forms.CharField(max_length=100,required=True,
                                      #widget=TinyMCE(attrs={'cols': 122, 'rows': 30})
                                      # within the attributes load in the form you must
                                      # put {{ form.media }}, in order to load editor for tinyMCE
                                      #https://stackoverflow.com/questions/71839445/django-tinymce-working-with-django-admin-but-not-working-in-form-template
                                      )
        
    class Meta():
        model = Difficulty    
        fields = ["difficulty_name"]

class SubjectForm(forms.ModelForm):
    subject_name = forms.CharField(max_length=100,required=True,)
    
    class Meta:
        model = Subject
        fields = ["subject_name"]

class AnswerForm(forms.ModelForm):
    # put {{ form.media }}, in order to load editor for tinyMCE in HTML template
    #https://stackoverflow.com/questions/71839445/django-tinymce-working-with-django-admin-but-not-working-in-form-template
    answer_html_text = forms.CharField(widget=TinyMCE(attrs={'cols':100, 'rows':12}))
    date_created     = forms.DateTimeField(required=False)
    question_answer  = forms.ModelChoiceField(queryset=Question.objects.all())
    correct_answer   = forms.ChoiceField(choices=Answer.active_choices)
    active           = forms.ChoiceField(choices=Answer.active_choices)
    
    class Meta:
        model = Answer
        fields = [
            'answer_html_text',
            'date_created',
            'question_answer',
            'correct_answer',
            'active'
        ]
        
class QuestionForm(forms.ModelForm):

    description            = forms.CharField(required=True)
    # put {{ form.media }}, in order to load editor for tinyMCE in HTML template
    #https://stackoverflow.com/questions/71839445/django-tinymce-working-with-django-admin-but-not-working-in-form-template                
    question_html_text     = forms.CharField(widget=TinyMCE(attrs={'cols':100, 'rows':12}))                    
    question_difficulty    = forms.ModelChoiceField(queryset=Difficulty.objects.all())               
    question_subject       = forms.ModelChoiceField(queryset=Subject.objects.all())                   
    active                 = forms.ChoiceField(choices=Question.active_choices)
    date_created           = forms.DateTimeField(required=False)
    
    class Meta:
        model = Question
        fields = [
            "description",
            "question_html_text" ,
            "question_difficulty",
            "question_subject"   ,
            "active",
            "date_created"
        ]
           
    
