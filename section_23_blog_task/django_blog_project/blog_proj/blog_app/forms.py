from django import forms
from blog_app.models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields =("autor", "title", "text")
        
        #Customizing Forms fields with FORMS WIDGETS
        widgets = {
            "title":forms.TextInput(attrs={"class":"textinputclass"}),
            "text":forms.Textarea(attrs={"class":"editable medium-editor-textarea postcontent"})
        }
        
        
class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields=("author", "text")
        
        #Customizing Forms fields with FORMS WIDGETS
        widgets = {
            "author":forms.TextInput(attrs={"class":"textinputclass"}),
            "text":forms.Textarea(attrs={"class":"editable medium-editor-textarea"})
        }
        
        
        
        
        
        
        