from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Message, Group, Mmessage
from posts.models import Personal_Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PersonalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Profile
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp']

class GroupSerializer(serializers.ModelSerializer):
    admin = UserSerializer()
    members = UserSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'admin', 'members']

class MmessageSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    sender = UserSerializer()

    class Meta:
        model = Mmessage
        fields = ['id', 'group', 'sender', 'content', 'timestamp']
