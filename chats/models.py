from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sender' )
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_message')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
    
class Group(models .Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_groups')
    members = models.ManyToManyField(User, related_name='chat_groups')

    def __str__(self):
        return self.name

class Mmessage(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='messages')
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username}: {self.content}'