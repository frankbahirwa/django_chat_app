from django.urls import path
from .views import *

urlpatterns = [
    path('', inboxx, name='inbox'),
    path('chat/<str:username>/', chatView, name='chat'),
    path('inboxx/', inbox, name='inboxx'),
    path('create_group/', create_group, name='create_group'),
    path('group/<int:group_id>/', group_chat, name='group_chat'),
    path('group/<int:group_id>/add_member/', add_member, name='add_member'),
]