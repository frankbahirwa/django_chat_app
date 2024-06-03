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
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content','attachment']
        widgets = {
            'content': forms.Textarea(attrs=({'class': 'inputs','placeholder':'Type Your Comment'})),
            'attachment': forms.FileInput(attrs=({'label':''}))
        }

class Story_Form(forms.ModelForm):
    class Meta:
        model = Add_Story
        fields = ['image', 'audio', 'text']

class Personal(forms.ModelForm):
    class Meta:
        model = Personal_Profile
        fields = ['image','caption']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'caption'}),
            'image': forms.FileInput(attrs={'class': 'inputs'})
            }