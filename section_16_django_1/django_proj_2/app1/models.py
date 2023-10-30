from django.db import models

# Create your models here.

# Available model fields DJANGO
#https://docs.djangoproject.com/en/4.2/ref/models/fields/

#Use of Forms class with models example
#https://stackoverflow.com/questions/18946746/django-form-error-messages-not-showing

class Topic(models.Model):
    #Varchar(264) field
    top_name = models.CharField(max_length=264,unique=True)
    
    #Customizing .str() function to return field when Topic.str() is called
    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    #Foreign key poiting to parent Topic class
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    #PK
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name
    
class Accessrecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.SET_NULL,null=True)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    #Custom str return
    def __str__(self):
        return self.first_name + " " + self.last_name


