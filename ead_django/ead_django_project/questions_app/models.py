import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone
from user_auth_app import models as custom_user_models
import questions_app.aux_library.models_functions as models_functions
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
        
        dict_json_return = models_functions.action_delete_column(
            reverse("questions_app:difficulty_detail_url",args=[
                self.difficulty_id
                ]),
            reverse("questions_app:difficulty_delete_url",args=[
                self.difficulty_id
                ]),            
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
    
    
# Class for a database VIEW object.
#This class is to be used with a View query on a Json call for json_datatable_data
class QuestionFromView(models.Model):
    question_id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField(default=datetime.datetime.today, null=True)
    description = models.CharField(max_length=500)    
    active = models.CharField(max_length=1)
    difficulty_name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=200)    
    
    
    class Meta:
        managed = False # this avoids creating a table into DB.
        db_table = "tv1_questions"  # view name to be used
        
    def to_dict_json(self):
        class_attributes = {
             "date_created"     : self.date_created.strftime("%m-%d-%Y %H:%M") if self.date_created else "N/A"  #customize date format display in DataTables
            ,"description"      : self.description
            ,"active"           : self.active
            ,"difficulty_name"  : self.difficulty_name
            ,"subject_name"     : self.subject_name
        }
        
        dict_json_return = models_functions.action_delete_column(
            reverse("questions_app:question_detail_url",args=[
                  self.question_id
                ]),
            reverse("questions_app:question_delete_url",args=[
                self.question_id
                ]),
            class_attributes            
        )
                
        return dict_json_return        


class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(default=datetime.datetime.today, null=True)
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
    date_updated = models.DateTimeField(blank=True,default=datetime.datetime.today,null=True)
    
    class Meta:
        db_table = "tb_questions"
        
    def __str__(self):
        return "question_id" + str(self.question_id) + ":" + self.description

    
    def to_dict_json(self):
        class_attributes = {
             "description"          : self.description
            ,"active"               : self.active
            ,"question_difficulty"  : models_functions.get_fk_id(self.question_difficulty, "difficulty_id")
            ,"question_subject"     : models_functions.get_fk_id(self.question_subject,"subject_id")            
            ,"date_created"         : self.date_created.strftime("%m-%d-%Y %H:%M") #customize date format display in DataTables
        }
        
        dict_json_return = models_functions.action_delete_column(
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
        return "answer_id:" + str(self.answer_id) + ":question id:" + str(self.question_answer.question_id)
    
    def to_dict_json(self):
        
        class_attributes = {
             "date_created"     : self.date_created.strftime("%d-%m-%Y %H:%M:%S") if self.date_created else "N/A" #customize date format display in DataTables
            ,"answer_html_text" : self.answer_html_text 
            ,"correct_answer"   : self.correct_answer
            ,"active"           : self.active
            ,"question_answer"  : models_functions.get_fk_id(self.question_answer,"question_id")
        } 
        
        dict_json_return = models_functions.action_delete_column(
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


class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)        
    difficulties = models.TextField(blank=False)
    subjects = models.TextField(blank=False)
    score = models.IntegerField(default=0, blank=True)
    
    STATUS_CHOICES = [
        ("COMPLETE", "Complete"),
        ("INCOMPLETE", "Incomplete"),
        ("PENDING", "Pending")
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    assigned_to = models.ForeignKey(
        custom_user_models.CustomUser,
        db_column="assigned_to",
        related_name="assigned_to_user",
        on_delete=models.CASCADE,
        null=True
    )
    
    date_created = models.DateTimeField(default=datetime.datetime.today, null=False)
    date_completed = models.DateTimeField(null=True)
    
    class Meta:
        db_table = "tb_assessments"
    
    def __str__(self):
        return "assessment_id:" + str(self.assessment_id) + "status:" + self.status
    
    def to_dict_json(self):
        class_attributes = {
            "date_created"    : self.date_created.strftime("%m-%d-%Y %H:%M:%S")
            #can be null, so before formating date, check if not null
           ,"date_completed"  : self.date_completed.strftime("%m-%d-%Y %H:%M:%S") if self.date_completed else "N/A"
           ,"difficulties"    : self.difficulties
           ,"subjects"        : self.subjects
           ,"status"          : self.status
        }
        
        dict_json_return = models_functions.action_delete_column(
            reverse("questions_app:assessment_detail_url",args=[
                self.assessment_id
                ]),
            reverse("questions_app:assessment_delete_url",args=[
                self.assessment_id
                ]),
            class_attributes             
        )
        
        return dict_json_return

    def get_absolute_url(self):
        return reverse("questions_app:assessment_list_url")
    

#will be populated at background, not browsable
class AssessmentQuestions(models.Model):
    
    assessment_id = models.ForeignKey(
        Assessment,
        db_column="assessment_id",
        related_name="assessment_assessment",
        null=True,
        on_delete=models.SET_NULL        
    )
    
    question_id = models.ForeignKey(
        Question,
        db_column="question_id",
        related_name="assessment_question",
        null=True,
        on_delete=models.SET_NULL
    )
    answer_selected = models.IntegerField(null=True)
    correct_answer = models.IntegerField(null=True)
    
    class Meta:
        managed=True
        db_table = "tb_assess_questions"
        
    def __str__(self):
        return "question:" + str(self.question_id) + ":" + str(self.answer_selected)
    
    
    
    



