from rest_framework import serializers
from .models import Report
from user.serializers import UserSerializer

class ReportSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    user_name = user.name
    user_role = user.roles
    
    
    class Meta:
        model = Report
        fields = ('user_name', 'user_role','id', 'subject', 'message', 'add_sensor_coordinates', 'add_mark_coordinates', 'add_pipe_coordinates', 'add_pipe_access_coordinates'
                  'image', 'report_date', 'leaker',                 
                  )
        
        
        
