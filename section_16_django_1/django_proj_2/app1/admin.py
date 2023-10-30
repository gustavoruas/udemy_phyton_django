from django.contrib import admin
#import Models from project into here
from app1.models import *


# Register your models here.
admin.site.register(Accessrecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)

