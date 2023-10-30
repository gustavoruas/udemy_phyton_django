from django import forms 
from django.contrib.auth.models import User
from app1.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields = ("username","email","password")
        
    def __init__(self,*args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        
        self.fields["username"].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Username Name'
                }
        )   

        self.fields["email"].widget = forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Email'
                }
        )   
        
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
                }
        )           
             
        
class UserProfileInfoForms(forms.ModelForm):
    
    class Meta:
        model = UserProfileInfo
        fields = ("portfolio_site",)
        
    def __init__(self,*args, **kwargs):
        super(UserProfileInfoForms,self).__init__(*args, **kwargs)
        
        self.fields["portfolio_site"].widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Portfolio'
            }
        )








