from rest_framework import serializers
from .models import Report
from clients.serializers import ClientSerializer

class ReportSerializer(serializers.ModelSerializer):
    
    Client = ClientSerializer(read_only=True)
    
    
    class Meta:
        model = Report
        fields = ('Client','id', 'subject', 'message', 'add_sensor_coordinates', 'add_mark_coordinates', 'add_pipe_coordinates', 'add_pipe_access_coordinates'
                  'image,' 'report_date,' 'leaker,'
                  
                  
                  )
        
        
        
