from django.urls import path
from .views import *

urlpatterns = [
    path('', userslogin , name='login'),
    path('home/', home , name='home'),
    path('logout/', userlogout , name='logout'),
]
