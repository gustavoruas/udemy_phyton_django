import os

#need for defining settings from proj
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_proj_2.settings")

import django
django.setup()

#Fake population script
import random
from app1.models import Webpage, Accessrecord, Topic
from faker import Faker

#instancing the Faker Class
fakegen = Faker()
topics = ["Search","Social","Marketplace","News","Games"]

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    
    for entry in range(N):
        
        top = add_topics()
        
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        webpage = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        acc_rec = Accessrecord.objects.get_or_create(name=webpage, date=fake_date)
        
if __name__ == "__main__":
    print("   ** pop script")
    populate(1)
    print("  ***POP script complete.")

