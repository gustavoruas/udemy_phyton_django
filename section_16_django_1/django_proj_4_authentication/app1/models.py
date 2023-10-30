from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    
    #connects auth django.contrib.auth.models.User to custom UserProfileInfo
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    
    portfolio_site = models.URLField(blank=True)
    
    #printout method
    def __str__(self):
        return self.user.username


