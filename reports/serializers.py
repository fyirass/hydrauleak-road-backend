from rest_framework import serializers
from .models import Report
from user.serializers import UserSerializer

class ReportSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    user_name = serializers.SerializerMethodField()
    user_role = serializers.SerializerMethodField()

    def get_user_name(self, obj):
        return obj.user.name

    def get_user_role(self, obj):
        return obj.user.roles
    
    class Meta:
        model = Report
        fields = ('user_name', 'user_role','id', 'subject', 'message', 'add_sensor_coordinates', 'add_mark_coordinates', 'add_pipe_coordinates', 'add_pipe_access_coordinates'
                  'image', 'report_date', 'leaker',                 
                  )
        
        
        
