import datetime
from django.shortcuts import get_object_or_404
from .models import Difficulty, Subject, Answer, Question, Assessment
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE
import logging

logger = logging.getLogger(__name__)

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
    answer_html_text = forms.CharField(widget=TinyMCE(attrs={'cols':50, 'rows':12}))
    #customizing date format in the field
    date_created     = forms.DateTimeField(
        required=False,
        #define initial value of a field.
        initial=datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        input_formats=['%d-%m-%Y %H:%M'],
        error_messages={
            'invalid': 'Enter a valid date/time in DD-MM-YYYY HH:MM format.'
        }                                  
    )
    #default question handled in VIEW.py classes
    #question_answer  = forms.ModelChoiceField(required=False, queryset=Question.objects.all())
    correct_answer   = forms.ChoiceField(choices=Answer.active_choices)
    active           = forms.ChoiceField(choices=Answer.active_choices)
    
    class Meta:
        model = Answer
        fields = [
            'answer_html_text',
            'date_created',
            #'question_answer',
            'correct_answer',
            'active'
        ]
        
    #initialization of form into render page. As dropdown for question is not editable
    #autopopulates from parent question URL
    def __init__(self, *args, **kwargs):
        question_id =  kwargs.pop("question_id",None)
        question = get_object_or_404(Question, pk=question_id)        
        super(AnswerForm,self).__init__(*args,**kwargs)        
        instance = getattr(self,"instance", None)   # returns an Answer
        
        if instance and instance.answer_id:
            #self.instance.question_answer = question
            None
        else:
            self.instance.question_answer = question

        
        #Disabling question_answer field
        #when in edit mode
        #if instance and instance.answer_id:            
        #    self.fields["question_answer"].widget.attrs["disabled"] = "True"
        #    self.fields["question_answer"].required = "False"
        #else: #on create answer
        #    self.fields["question_answer"].widget.attrs["disabled"] = "True"
        #    self.fields["question_answer"].required = "False"            

        
    #https://stackoverflow.com/questions/49226763/how-to-raise-multiple-validationerror-on-django
    #https://docs.djangoproject.com/en/3.0/ref/forms/validation/#raising-multiple-errors
    #customizing validations on form submission by overwridding clean()
    def clean(self):
        # listing multiple ValidationError
        errors = []        
        cleaned_data = super().clean()
        question = cleaned_data.get("question_answer")
        current_correct_answer = cleaned_data.get("correct_answer")
        correct_answer_count = 0
        current_answer = self.instance    #fetches current Answer Object
                
        #if question_answer not returning, fetch from URL
        if not question:
            #retrieves question Parent from instance
            question = current_answer.question_answer
        
        #check if any answer already is the correct one of the father question. Only 1 allowed
        #question_answers is configured at FK in Answer, returns all related Answers to question attibute of this specific answer.        
        #filter all answers that are correct only
        for question_answers in question.question_answers.filter(correct_answer="Y"):  
            #pk is null then inserting
            print("question_answers:id:"+str(question_answers.answer_id)+":"+str(question_answers.answer_html_text))
            if current_answer.answer_id == None:
                if current_correct_answer == "Y":
                    correct_answer_count = correct_answer_count + 1
            else: #if exist, match if id is the same being updated               
                if current_answer.answer_id != question_answers.answer_id and current_correct_answer == "Y":
                    correct_answer_count = correct_answer_count + 1
        
        #check if no correct answers so far inserted after 3 already created. Fires at creation of fourth
        if question.question_answers.filter(correct_answer="N").count() == 3:
            #pk is null then inserting
            if current_answer.answer_id == None and current_correct_answer == "N":
                errors.append(ValidationError(
                    "At Least 1 answer must be correct."
                ))               
        
        if question:
            answer_count = question.question_answers.count()
            
            if answer_count > 4 :
                errors.append(ValidationError("A Question may have only 4 answers."))
                
        if correct_answer_count > 0:
            errors.append(ValidationError(
                "Only 1 correct answer per question allowed."
            ))
                
        if errors:
            raise ValidationError(errors)
                
        return cleaned_data
        
        
class QuestionForm(forms.ModelForm):

    description            = forms.CharField(required=True)
    # put {{ form.media }}, in order to load editor for tinyMCE in HTML template
    #https://stackoverflow.com/questions/71839445/django-tinymce-working-with-django-admin-but-not-working-in-form-template                
    question_html_text     = forms.CharField(widget=TinyMCE(attrs={'cols':100, 'rows':12}))                    
    question_difficulty    = forms.ModelChoiceField(queryset=Difficulty.objects.all())               
    question_subject       = forms.ModelChoiceField(queryset=Subject.objects.all())                   
    active                 = forms.ChoiceField(choices=Question.active_choices)
    date_created           = forms.DateTimeField(
        required=True,
        #define initial value of a field.
        initial=datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        input_formats=['%d-%m-%Y %H:%M'],
        error_messages={
            'invalid': 'Enter a valid date/time in DD-MM-YYYY HH:MM format.'
        }
    )
    
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


class AssessmentForm(forms.ModelForm):
           
    #Both fields will take PIPPED elements, isntead of single FK reference
    difficulties = forms.MultipleChoiceField(
        widget=forms.SelectMultiple
    )
    subjects = forms.MultipleChoiceField(
        widget=forms.SelectMultiple   #CheckboxSelectMultiple
    )
    
    status = forms.ChoiceField(choices=Assessment.STATUS_CHOICES)
    
    # assigned_to = forms.ModelChoiceField()
    
    date_created = forms.DateTimeField(
        required=True,
        initial=datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        input_formats=['%d-%m-%Y %H:%M'],
        error_messages={
            'invalid': 'Enter a valid date/time in DD-MM-YYYY HH:MM format.'
        }       
    )
    
    date_to_complete = forms.DateTimeField(
        required=True,
        initial=(datetime.datetime.now()+datetime.timedelta(days=10)).strftime("%d-%m-%Y %H:%M"),
        input_formats=['%d-%m-%Y %H:%M'],
        error_messages={
            'invalid': 'Enter a valid date/time in DD-MM-YYYY HH:MM format.'
        }        
    )
        
    class Meta:
        model = Assessment
        fields = [
            "difficulties",
            "subjects",
            "status",
            "assigned_to",
            "date_created",
            "date_to_complete"
        ]

    #initializing form function, to define list of valuie from DB in fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["difficulties"].choices =[
            #iterating each element from Difficulty in a list of elements
            (diff.difficulty_id, diff.difficulty_name ) for diff in Difficulty.objects.all()
        ]
        
        self.fields["subjects"].choices =[
            #iterating each element from Difficulty in a list of elements
            (subj.subject_id, subj.subject_name ) for subj in Subject.objects.all()
        ]
        
        #if fields already were pre populated, mark the values
        if self.instance and self.instance.difficulties:
            print("in instance of difficulties")
            self.fields["difficulties"].initial = self.instance.difficulties.split("|")
            
        if self.instance and self.instance.subjects:
            print("in instance of subjects")
            print(self.instance.subjects)
            self.fields["subjects"].initial = self.instance.subjects.split("|")
                       
               
    #defining both fields to save multiple elements piped by |
    def clean_difficulties(self):
        selected_values = self.cleaned_data.get("difficulties")
        return "|".join(selected_values)
    
    def clean_subjects(self):
        selected_values = self.cleaned_data.get("subjects")
        return "|".join(selected_values)
    
    #Clean_ fields must always return a vlue into the field they are validating. Clean runs at form POSTING
    def clean_status(self):
        #gets current instance of assignment
        current_assignment = self.instance
        #gets cleaned data from attribute assessment.status
        current_status = self.cleaned_data.get("status")
        
        #If current change of form is moved to incomplete and score has prev values, reset score
        if current_status == "INCOMPLETE" and current_assignment.score > 0:
            current_assignment.score = 0 # defines 
        
        return current_status
        
