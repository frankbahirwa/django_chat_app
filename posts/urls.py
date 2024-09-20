from django.urls import path
from .views import *

urlpatterns = [
   path('' , add_post , name='add-post'),
   path('post/<int:id>/' , post_details, name='post_details'),
   path('add_story/' , upload_media , name='story'), 
]
