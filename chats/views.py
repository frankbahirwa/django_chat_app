from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')        # to never allow the users to access this service without loging in
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'chats/send_message.html', {'form': form})   # passing the data to next page

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'chats/inbox.html', {'received_messages': received_messages})
