from typing import Any
from django import apps
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.
class CustomUserManager(UserManager):
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            return ValueError("YOu have not provided a valid email")
        
                
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        #username = email.split("@")[0]
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_user(self,  email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self,email,password):
        user = self._create_user(email, password)        
        user.is_staff = True
        user.is_superuser = True 
        user.save(using=self.db)
    
#Example - https://github.com/j0pine4/django-base/tree/master/UserAut
    
class CustomUser(AbstractBaseUser, PermissionsMixin): 
    user_id = models.AutoField(primary_key=True)
    #username = models.CharField(blank=False, max_length=100, null=False, default="",unique=True)
    email = models.EmailField(blank=False, default="", unique=True)
    name = models.CharField(max_length=100,blank=True, default="")
    password = models.CharField(max_length=128)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    #Roles to be added    
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    
    
    class Meta:
        #defining DB tablename
        db_table = "tb_custom_users"
        verbose_name = "User"
        verbose_name_plural = "Users"
 
    def __str__(self):
        return self.email.split("@")[0]  
    
    def get_full_name(self, input_var):
        return self.name + "full name test" + str(input_var)
    
    def get_short_name(self):
        return self.email.split("@")[0]


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    is_active = models.BooleanField(default=True)
        
    def __str__(self):
        return self.name

    #Join Many to Many to user
    users = models.ManyToManyField(CustomUser,
                                   related_name="roles"   #needs to be defined, to reference as dependent attribute from user.
                                   ) 
    
    class Meta:
        #defining DB tablename
        db_table = "tb_custom_roles"
        #verbose_name = "Role"
        #verbose_name_plural = "Roles"  
        

#Normalization 3 needs a 3 object, and the join of object receives through
#class CustomRoleUser(models.Model):    
#    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#    role = models.ForeignKey(Role, on_delete=models.CASCADE)
#    
#    def __str__(self):
#        return "{} - {}".format(self.user.__str__(), self.role.__str__() )
#    
#    class Meta:
#        db_table = "tb_cust_roleuser"
#        verbose_name = "CustomRoleUser"
#        verbose_name_plural = "CustomRoleUser"         
    
    
    