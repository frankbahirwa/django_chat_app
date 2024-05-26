from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import Posts

# Create your views here.
@login_required(login_url='login')
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
        posts = Posts.objects.all().order_by('created_at')
    return render(request , 'posts/add-post.html' , {'form' : form , 'posts': posts})

    
