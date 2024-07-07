from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Difficulty(models.Model):
    difficulty_id = models.AutoField(primary_key=True)
    difficulty_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "tb_difficulty"
        
    def __str__(self):
        return self.difficulty_name
    
    def to_dict_json(self):
        return {            
            "difficulty_name" : self.difficulty_name,
            "action"          : 
            "<a href=" + chr(34) + reverse("questions_app:difficulty_detail_url",args=[self.difficulty_id]) + chr(34) +">" +
            "  <span class=" + chr(34) + "glyphicon glyphicon-edit" + chr(34) + "></span> " + 
            "</a> / "  +          
            "<a href=" + chr(34) + reverse("questions_app:difficulty_delete_url",args=[self.difficulty_id]) + chr(34) +">" +
            "  <span class="+ chr(34) +"glyphicon glyphicon-remove"+ chr(34) +"></span>" +
            "</a>"
        }
    
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
    
    def get_absolute_url(self):
        return reverse("questions_app:subject_list_url")
    


