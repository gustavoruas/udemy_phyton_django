import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from questions_app.aux_library.models_functions import action_delete_column
from tinymce import models as mce_models 

# Create your models here.

class Difficulty(models.Model):
    difficulty_id = models.AutoField(primary_key=True)
    
    difficulty_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "tb_difficulty"
        
    def __str__(self):
        return self.difficulty_name
    
    def to_dict_json(self):
                
        class_attributes = {
            "difficulty_name" : self.difficulty_name
        }
        
        dict_json_return = action_delete_column(
            "questions_app:difficulty_detail_url",
            "questions_app:difficulty_delete_url",
            self.difficulty_id,
            class_attributes
        )
        
        return dict_json_return
    
    #needed URL for creating the class via views.py, in the SchoolCreateView class
    def get_absolute_url(self):
        return reverse("questions_app:difficulty_list_url")


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=200)
    
    class Meta:
        db_table = "tb_subject"
        
    def __str__(self):
        return self.subject_name
    
    #needed URL for creating the class via views.py, in the SchoolCreateView class
    def get_absolute_url(self):
        return reverse("questions_app:subject_list_url")
    

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500)
    question_html_text = mce_models.HTMLField()
    
    question_difficulty = models.ForeignKey(
        Difficulty, 
        related_name= "question_difficulties",
        on_delete=models.SET_NULL,
        null=True
    )
    
    question_subject = models.ForeignKey(
        Subject,
        related_name="question_subjects",
        on_delete=models.SET_NULL,
        null=True
    )
    
    # Creating defined dropdown attributes from model
    active_choices = [
        ("Y","Yes"),
        ("N","No"),
    ]
    
    active = models.CharField(max_length=1, choices=active_choices, default="Y")
    date_created = models.DateTimeField(default=datetime.datetime.today, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = "tb_questions"
        
    def __str__(self):
        return str(self.question_id) + ":" + self.description
    
    def to_dict_json(self):
        class_attributes = {
             "description"          : self.description
            ,"active"               : self.active
            ,"question_difficulty"  : self.question_difficulty.difficulty_id    
            ,"question_subject"     : self.question_subject.subject_id
            ,"date_created"         : self.date_created
        }
        
        dict_json_return = action_delete_column(
            reverse("questions_app:question_detail_url",args=[
                self.question_id
                ]),
            reverse("questions_app:question_delete_url",args=[
                self.question_id
                ]),
            class_attributes            
        )
                
        return dict_json_return
    
    #NEED TO DO - reverse and absolute_url
    def get_absolute_url(self):
        return reverse("questions_app:question_list_url")
    
    
    
class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer_html_text = mce_models.HTMLField()    
    date_created = models.DateTimeField(default=datetime.datetime.today, null= True)
    
    question_answer = models.ForeignKey(
        Question,
        related_name="question_answers",
        on_delete=models.SET_NULL,
        null=True
    )
    
    # Creating defined dropdown attributes from model
    active_choices = [
        ("Y","Yes"),
        ("N","No"),
    ]
    
    correct_answer = models.CharField(max_length=1, choices=active_choices, default="Y")
    active = models.CharField(max_length=1, choices=active_choices, default="Y")
    
    class Meta:
        db_table = "tb_question_answers"
    
    def __str__(self):
        return str(self.answer_id) + ":question id:" + str(self.question_answer.question_id)
    
    def to_dict_json(self):
        
        class_attributes = {
             "date_created"     : self.date_created  
            ,"answer_html_text" : self.answer_html_text 
            ,"correct_answer"   : self.correct_answer
            ,"active"           : self.active
            ,"question_answer"  : self.question_answer.question_id
        } 
        
        dict_json_return = action_delete_column(
            reverse("questions_app:answer_detail_url",args=[
                self.question_answer.question_id,
                self.answer_id
                ]),
            reverse("questions_app:answer_delete_url",args=[
                self.question_answer.question_id,
                self.answer_id
                ]),          
            class_attributes            
        )
        
        return dict_json_return
    
        
    #NEED TO DO - reverse and absolute_url
    def get_absolute_url(self):
        return reverse("questions_app:answer_list_url")



