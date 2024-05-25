from django.urls import path
from .views import *

urlpatterns = [
   path('' , add_post , name='add-post')   
]
