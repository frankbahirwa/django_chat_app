from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message
from  posts.models import *
from django.db.models import Q
from django.http import HttpResponseRedirect



@login_required
def chatView(request, username):
    users = User.objects.all().reverse()
    the_user = get_object_or_404(User, username=username)
    profiles = Personal_Profile.objects.filter(user = request.user).order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=the_user, content=content)
            return HttpResponseRedirect(request.path_info)

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=the_user) | Q(sender=the_user, receiver=request.user)
    ).order_by('timestamp')

    return render(request, 'chats/chat.html', { 'users': users, 'the_user': the_user, 'messages': messages ,'profiles':profiles})
