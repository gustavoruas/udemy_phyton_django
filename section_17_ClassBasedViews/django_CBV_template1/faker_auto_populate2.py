import os

#need for defining settings from proj
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_CBV_template1.settings")

import django
django.setup()

#Fake population script
import random
from cbvapp1.models import School, Students
from faker import Faker

#instancing the Faker Class
fakegen = Faker()

#Creating schools
def populate(loop_num=10):
    #creating schools
    p_school_name = fakegen.company()
    p_principal = fakegen.name()
    p_school_address= fakegen.address()
    
    p_school = School.objects.get_or_create(
        school_name    = p_school_name
       ,principal      = p_principal
       ,school_address = p_school_address
    )[0]
    
    #add students to created school
    for loop in range(loop_num):
        p_student_name = fakegen.name() 
        p_age          = fakegen.random_int(min=2,max=19)
        
        student = Students.objects.get_or_create(
             student_name = p_student_name
            ,age          = p_age
            ,school       = p_school
        )
        

print("starting faker for cbvapp1")

for loop in range(10):
    populate()

print("end faker")