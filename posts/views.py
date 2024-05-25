from django.shortcuts import render , redirect
from .forms import *

# Create your views here.

def add_post(request):
    if request.method == 'POST':
        form = PostsForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect('home')
        
    else:
        form = PostsForm() 
    return render(request , 'posts/add-post.html' , {'form' : form})

    
