from django.urls import path
from .views import *

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
]