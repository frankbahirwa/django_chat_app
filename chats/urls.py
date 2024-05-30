from django.urls import path
from .views import *

urlpatterns = [
    path('', inbox, name='inbox'),
    path('<str:username>/', chatView, name='chat')
]