from .models import *
from django import forms

class PostsForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = ['title','content','image']
        
        widgets = {
            'title': forms.TextInput(attrs=({'class':'inputs' , 'placeholder': 'Title'})),
            'content': forms.Textarea(attrs=({'class':'inputs' , 'placeholder':'main-content'})),
            'image': forms.FileInput(attrs=({'class':'inputs'}))
        }
        