import os

#need for defining settings from proj
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_proj_2.settings")

import django
django.setup()

#Fake population script
import random
from app1.models import Webpage, Accessrecord, Topic, User
from faker import Faker

#instancing the Faker Class
fakegen = Faker()
topics = ["Search","Social","Marketplace","News","Games"]

def add_topics():
    #Instanciates new Class if non Existent.
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    #Commits into DBlite table.
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):
        
        top = add_topics()
        
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        #Instanciates new Class if non Existent.
        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        acc_rec = Accessrecord.objects.get_or_create(name=webpage, date=fake_date)

def populate_users(N=10):
    
    for user_entry in range(N):
        user = User.objects.get_or_create(
             first_name = fakegen.first_name()
            ,last_name  = fakegen.last_name()
            ,email      = fakegen.email()
        )

        

if __name__ == "__main__":
    print("   ** pop script")
    # populate(20)
    populate_users(10)
    print("  ***POP script complete.")

