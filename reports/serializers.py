from rest_framework import serializers
from .models import Report
from user.serializers import UserSerializer

class ReportSerializer(serializers.ModelSerializer):
    
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Report
        fields = ('user','id', 'subject', 'message', 'add_sensor_coordinates', 'add_mark_coordinates', 'add_pipe_coordinates', 'add_pipe_access_coordinates',
                  'image', 'report_date'                 
                  )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
