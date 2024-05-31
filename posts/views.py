from django.shortcuts import render , redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *

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

def post_details(request,id):
    post = Posts.objects.get(id = id)
    
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
        return render(request, 'posts/post_details.html',{'post':post,'form':form})
    
@login_required
def add_profile(request):
    if request.method == 'POST':
        form = Personal(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)  
            profile.user = request.user 
            profile.save()
            return redirect('home')
    else:
        form = Personal()
    return render(request, 'posts/add_profile.html', {'form': form})

@login_required
def upload_media(request):
    if request.method == 'POST':
        form = Story_Form(request.POST, request.FILES)
        if form.is_valid():
            story =  form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect('home')
    else:
        form = Story_Form()
    return render(request, 'posts/add_story.html', {'form': form})