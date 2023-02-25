from rest_framework import serializers
from .models import Client
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','roles', 'name', 'phone')


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'user', 'photo', 'description', 'address', 'inscription_date', 'client_files')
        read_only_fields = ('id',)


class ClientWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('user', 'photo', 'description', 'address', 'inscription_date', 'client_files')
