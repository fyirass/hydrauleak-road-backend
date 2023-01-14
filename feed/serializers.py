from dataclasses import fields
import imp
from rest_framework import serializers
from .models import *
# from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'email', 'first_name', 'last_name', 'password')

# # class ProfileSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Profile
# #         fields = '__all__'
        
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        
class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = '__all__'


class KpiTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = KpiTracking
        fields = '__all__'
        
        
class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
        
        
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'
        
        
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
        
        
class PipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipe
        fields = '__all__'
        
        
class Pipe_accesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipe_acces
        fields = '__all__'
        
