from django.db import models
from datetime import datetime
from user.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator

class Report(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    user_name = models.CharField(max_length=100, blank=True)
    user_role = models.CharField(max_length=100, blank=True)
    
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    
    add_sensor_coordinates = models.CharField(max_length=100, blank=True)
    add_mark_coordinates = models.CharField(max_length=100, blank=True)
    add_pipe_coordinates = models.CharField(max_length=100, blank=True)
    add_pipe_access_coordinates = models.CharField(max_length=100, blank=True)
    
    image = models.ImageField(upload_to='report_image', blank=True)
    
    report_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.subject
    
