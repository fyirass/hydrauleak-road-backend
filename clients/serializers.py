from rest_framework import serializers
from .models import Client
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone')

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Client
        fields = ('user','id', 'photo', 'description',  'address',  'inscription_date', 'client_files')
        
