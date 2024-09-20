from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from  posts.models import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.conf import settings

@login_required
def inboxx(request):
    profiles = Personal_Profile.objects.filter(user = request.user).order_by('-created_at')
    users = User.objects.all().reverse()
    # received_messages =
    return render(request, 'chats/inbox.html', {'users': users,'perofiles':profiles})

@login_required
def chatView(request, username):
    users = User.objects.all().reverse()
    the_user = get_object_or_404(User, username=username)
    profiles = Personal_Profile.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=the_user, content=content)
            return HttpResponseRedirect(request.path_info)

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=the_user) | Q(sender=the_user, receiver=request.user)
    ).order_by('timestamp')

    return render(request, 'chats/chat.html', {
        'users': users,
        'the_user': the_user,
        'messages': messages,
        'profiles': profiles,
    })

@login_required
def inbox(request):
  
    users = User.objects.all().reverse()
    groups = request.user.chat_groups.all()
    return render(request, 'chats2/temps/inbox.html', {'users': users,  'groups': groups})


@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            group.members.add(request.user)
            return redirect('inbox')
    else:
        form = GroupForm()
    return render(request, 'chats2/temps/create_group.html', {'form': form})

@login_required
def add_member(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user != group.admin:
        messages.error(request, "Only the group admin can add members.")
        return redirect('group_chat', group_id=group_id)

    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            if user:
                group.members.add(user)
                messages.success(request, f'{username} has been added to the group.')
            else:
                messages.error(request, f'User {username} does not exist.')
            return redirect('group_chat', group_id=group_id)
    else:
        form = AddMemberForm()
    return render(request, 'chats2/temps/add_member.html', {'form': form, 'group': group})

@login_required
def group_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user not in group.members.all():
        messages.error(request, "You are not a member of this group.")
        return redirect('inbox')

    messages = group.messages.all().order_by('timestamp')
    return render(request, 'chats2/temps/group_chat.html', {'group': group, 'messages': messages})