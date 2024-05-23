from django import forms
from django.contrib.auth.models import User

class userlogin(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'inputs'})
    )
    password = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'inputs'})
    )


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs=({'class':'inputs' , 'placeholder': 'Username'})),
            'email': forms.EmailInput(attrs=({'class':'inputs' , 'placeholder':'Email'})),
            'password': forms.PasswordInput(attrs=({'class':'inputs' , 'placeholder': 'Password'}))
        }
        
        labels = {
            'username':'',
            'email':'',
            'password':''
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user