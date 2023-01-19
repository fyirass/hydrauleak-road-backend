from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import User

# class SignupSerializer(serializers.ModelSerializer):
#     re_password = serializers.CharField(write_only=True)
#     class Meta:
#         model = get_user_model()
#         fields = ('name', 'email', 'password', 're_password', 'phone', 'is_admin', 'is_leaker', 'is_client')
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
        
#     def validate(self, data):
#         # check if passwords match
#         if data['password'] != data['re_password']:
#             raise serializers.ValidationError("Passwords don't match")
#         return data

#     def create(self, validated_data):
#         del validated_data['re_password']
#         validated_data['is_client'] = True
#         user = get_user_model().objects.create_user(**validated_data)
#         return user
    
    
class SignupSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password', 're_password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        # check if passwords match
        if data['password'] != data['re_password']:
            raise serializers.ValidationError("Passwords don't match")
        return data
    
    def save(self):
        user = User.objects.create_user(
            self.validated_data['username'],
            self.validated_data['email'],
            self.validated_data['phone'],
            self.validated_data['password'],
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'phone', 'is_admin', 'is_leaker', 'is_client')