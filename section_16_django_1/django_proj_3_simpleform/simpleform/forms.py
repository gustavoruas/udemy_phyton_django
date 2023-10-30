from django import forms 
from django.core import validators

#custom validator function, the value parameter is a MUST to be used in validators=
#in each field.
def check_initial_z(value):

    if value[0].lower() != "z":        
        raise forms.ValidationError("Text area must start with a Z")



class FormName(forms.Form):
       
    name = forms.CharField(validators=[validators.MaxLengthValidator(4,"Text name must be up to 4 chars Max")])
    
    email = forms.EmailField(required=True) 
    
    verify_email = forms.EmailField(required=True                                    
                                    ) 
    
    text = forms.CharField(
                            validators=[check_initial_z] #adding custom func validation, ,ultiple can be added
                           ,widget=forms.Textarea
                           )
    
    #hidden field in page
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput
                                 ) 
    
    #custom method that calls cleaned_data() to all fields, and validates at POST for al lfields
    #any custom validation existing.
    def clean(self):
        all_clean_data = super().clean()
        
        #selects field from collection, to validate their values
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]

        if str(email).lower() != str(verify_email).lower():
            print("inside email error validation")
            raise forms.ValidationError("Emails field are not the same")
    
    
    


        
    
    


