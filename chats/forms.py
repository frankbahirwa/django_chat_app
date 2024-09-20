from django import forms
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']
        
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class AddMemberForm(forms.Form):
    username = forms.CharField(max_length=150)
