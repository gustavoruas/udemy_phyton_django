from django.contrib import admin
from .models import CustomUser, Role

#Custom User admin page
class CustomUserAdmin(admin.ModelAdmin):
        
    list_display = ["email", "name","is_superuser","is_active"]


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)
#admin.site.register(CustomRoleUser)




