from rest_framework import serializers
from .models import Leaker

from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone')

class LeakerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Leaker
        fields = ('user', 'id', 'photo', 'description', 'address', 'inscription_date', 'status')
        
        
  