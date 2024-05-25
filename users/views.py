from django.shortcuts import render, redirect
from .forms import UserForm, userlogin
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Posts



@login_required(login_url='login')
def home(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request, "users/home.html" , {'posts':posts})


def userslogin(request):
    login_form = userlogin()
    signup_form = UserForm()
    
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = userlogin(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
            
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password")
        elif 'signup' in request.POST:
            signup_form = UserForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                username = signup_form.cleaned_data['username']
                raw_password = signup_form.cleaned_data['password']
                user = authenticate(request, username=username, password=raw_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "User created and logged in successfully")
                    return redirect('home')
                else:
                    messages.error(request, "User creation failed. Please try again.")
            else:
                messages.error(request, "User not created. Please check the form for errors.")

    return render(request, 'users/credentials.html', {'login_form': login_form, 'signup_form': signup_form})



def userlogout(request):
    logout(request)
    return redirect('login')