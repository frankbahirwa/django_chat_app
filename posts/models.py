from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/' , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    attachment = models.FileField(upload_to='images/comments',null=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('Posts',on_delete=models.CASCADE , related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'comment by -> {self.author} on post {self.post}'

class Add_Story(models.Model):
    
    image = models.ImageField(upload_to='stories/')
    audio = models.FileField(upload_to='audio/')
    text = models.TextField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  f"Post by -> {self.user.username}"
    
class Personal_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"Post by -> {self.user.username}" 