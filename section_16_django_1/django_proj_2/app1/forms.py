from django import forms 
from django.core import validators
from app1.models import *

class UserForm(forms.ModelForm):
    
    #connecting form to the Model class
    class Meta:
        #model = User
        #specifies which fields to show
        #fields = ['first_name','last_name','email']        
        #shows all fields
        #fields = '__all__'        

        #https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
        #defining each field attributes using Widgets
        # This approach must be within the Meta class
        # model = User
        # fields = ['first_name', 'last_name', 'email']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 
        #                                          'placeholder': 'Enter First Name'}                                                                                  
        #                                   ),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 
        #                                         'placeholder': 'Enter Last Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control',
        #                                      'label': 'test label', 
        #                                      'placeholder': 'Enter Email'}),
        # }
        
        #defining each field attributes using Widgets #2
        model = User
        fields = ["first_name", "last_name", "email"]
    
    # Must be idented as a function of UserForm, and not Class META    
    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        self.fields["first_name"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Enter First Name'})
        
        self.fields["last_name"].widget = forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter Last Name'})                                            
        
        self.fields["email"].widget = forms.EmailInput(attrs={'class': 'form-control',                                                                  
                                                                  'placeholder': 'Enter Email'})
        
        self.fields["email"].label = "Emailszz"
                              
                                            
class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ["top_name"]
        
    def __init__(self,*args, **kwargs):
        super(TopicForm,self).__init__(*args, **kwargs)
        
        self.fields["top_name"].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Topic Name'
                }
        )
                 
class WebpageForm(forms.ModelForm):
    
    class Meta:
        model = Webpage
        fields = ["topic","name","url"]
        
    def __init__(self, *args, **kwargs):
        super(WebpageForm,self).__init__(*args, **kwargs)
        
        topic_list = Topic.objects.order_by("top_name")
        
        #Need to iterate into a tuple, to pass in choices= 
        topic_choices = [(topic_loop.id,topic_loop.top_name) for topic_loop in topic_list]
        
        for loop in topic_list:
            print(loop.top_name)
        
        self.fields["topic"].widget = forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Topic Name'
                }
            ,choices=topic_choices
        )
        
        self.fields["topic"].label = "Select a Topic"            
        
        self.fields["name"].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Webpage Name'
                }            
        )       
        self.fields["name"].label = "Webpage Name"
        
        self.fields["url"].widget = forms.URLInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Url'
                }          
        )
            
           