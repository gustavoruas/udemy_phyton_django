from django.contrib import admin

# Register your models here.
from . import models


# Ordering field order for a specific Object Model
class MovieAdmin(admin.ModelAdmin):
    
    #Displays the column name of the object attribute
    list_display = ["title","release_year","length"]
    
    #defines the fields of Model Movia via list
    fields = ["title","release_year","length"]
    
    #Adding search to specific fields
    search_fields = ["title","release_year"]
    
    #Adding a filter to the Model page Admin
    list_filter = ["release_year"]
    
    #Enables editing attribute in the list
    list_editable = ["release_year"]


class CustomerAdmin(admin.ModelAdmin):
    
    list_display = ["first_name", "last_name", "phone"]
    
    fields = ["first_name", "last_name", "phone"]


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Movie, MovieAdmin)

#Need to register the movie admin once created.
# admin.site.register(MovieAdmin)


