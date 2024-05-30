from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message
from django.db.models import Q
from django.http import HttpResponseRedirect



# Create your views here.

# @login_required(login_url='login')        # to never allow the users to access this service without loging in
# def send_message(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = request.user
#             message.save()
#             return redirect('inbox')
#     else:
#         form = MessageForm()
#     return render(request, 'chats/send_message.html', {'form': form})   # passing the data to next page

@login_required
def inbox(request):
    users = User.objects.all().reverse()
    # received_messages =
    return render(request, 'chats/inbox.html', {'users': users})




@login_required
def chatView(request, username):
    users = User.objects.all().reverse()
    the_user = get_object_or_404(User, username=username)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=the_user, content=content)
            return HttpResponseRedirect(request.path_info)

    messages = Message.objects.filter(
        Q(sender=request.user, receiver=the_user) | Q(sender=the_user, receiver=request.user)
    ).order_by('timestamp')

    return render(request, 'chats/chat.html', { 'users': users, 'the_user': the_user, 'messages': messages })
