from django.shortcuts import render , redirect ,get_object_or_404
from .forms import *
from django.http import HttpResponse
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

def post_details(request, id):
    post = get_object_or_404(Posts, id=id)
    comments= Comment.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('home')
        else:
            return HttpResponse(f'Comment not added. Errors: {comment_form.errors}')
    else:
        comment_form = CommentForm()
        return render(request, 'posts/post_details.html', {'post': post, 'form': comment_form,'comments':comments})

    
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