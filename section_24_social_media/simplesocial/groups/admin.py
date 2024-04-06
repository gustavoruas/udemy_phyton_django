from django.contrib import admin
from . import models

# Register your models here.

#Child object is manageble in admin interface, as Group is father and GroupMember is child
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
