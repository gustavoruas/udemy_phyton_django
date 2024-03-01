from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    school_id = models.AutoField(primary_key=True) #forces the name of ID column
    school_name = models.CharField(max_length=250, null=False)
    principal = models.CharField(max_length=200)
    school_address= models.CharField(max_length=700)
    
    #a to_string custom method
    def __str__(self):
        return (str(self.school_id)+"|" + self.school_name+"|" + self.principal ) 
    
    #needed URL for creating the class via views.py, in the SchoolCreateView class
    def get_absolute_url(self):
        #Need to provide the view/detail name in (urls.py of project), to redirect once created
        #to which page should go after creation
        #the second arg is the ID to load in the Details screen "pk"
        return reverse("cbvapp1:school_details_url", kwargs={"pk": self.pk})
    


class Students(models.Model):
    student_id = models.AutoField(primary_key=True) #forces the name of ID column
    student_name = models.CharField(max_length=300, null=False)
    # positive Integers above 0
    age = models.PositiveIntegerField()
    
    #Joininkg FK with table Scholl, need on delete rule
    #related_name="students" = is what is used on HTML files as dictionary object when loading Schools
    school = models.ForeignKey(School,on_delete=models.SET_NULL,null=True,related_name="students")
    
    def __str__(self):
        return(str(self.student_id)+"|"+self.student_name+"|"+str(self.age))
    
    def get_absolute_url(self):
        return reverse("cbvapp1:student_update_url", kwargs={"pk": self.pk})
    
 
 
    
    
    

