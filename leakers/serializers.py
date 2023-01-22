from rest_framework import serializers
from .models import Leaker

class LeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaker
        fields = '__all__'