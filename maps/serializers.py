from rest_framework import serializers
from .models import Zone, Sensor, Pipe, PipeAcces, Mark, LeakerVehicle, Map

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

class PipeAccesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PipeAcces
        fields = '__all__'

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

class LeakerVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeakerVehicle
        fields = '__all__'

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
