from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import CustomUser
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

#UserCreationForm
class CustomUserCreateForm(forms.Form, UserCreationForm ):
    
    #Adding the fields validation here
    email = forms.EmailField(required=True)
    
    name = forms.CharField(max_length=100, required=True)
    is_staff = forms.BooleanField(required=False)
        
    class Meta:
        fields = ("email", "name", "is_staff")
        model = get_user_model()    
        
 
    #cusomizing field 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].label = "Username"
        self.fields["email"].widget = forms.EmailInput(
            attrs={
                " placeholder":"Email as username"
            }
        )
        self.fields["name"].label = "Name"


#Custom password change form
class CustomPasswordChangeForm(PasswordChangeForm):

    #old_password = forms.CharField(
    #    label="New Password",
    #    widget=forms.PasswordInput(attrs={'class': 'form-control'})
    #)
#
    #new_password1 = forms.CharField(
    #    label="New Password",
    #    widget=forms.PasswordInput(attrs={'class': 'form-control'})
    #)
    #
    #new_password2 = forms.CharField(
    #    label="Confirm New Password",
    #    widget=forms.PasswordInput(attrs={'class': 'form-control'})
    #)
    
    class Meta:        
        fields = ("new_password1","new_password2")

