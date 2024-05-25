from .models import *
from django import forms

class PostsForm(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = ['title','content','image']