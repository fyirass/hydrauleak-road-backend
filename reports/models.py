from django.db import models
from datetime import datetime
from leakers.models import Leaker
from clients.models import Client
from django.contrib.postgres.fields import ArrayField
from django.core.validators import FileExtensionValidator

class Report(models.Model):
    
    
    leaker = models.ForeignKey(Leaker, on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    
    add_sensor_coordinates = ArrayField(models.FloatField(),size=2)
    add_mark_coordinates = ArrayField(models.FloatField(),size=2)
    add_pipe_coordinates = ArrayField(models.FloatField(),size=2)
    add_pipe_access_coordinates = ArrayField(models.FloatField(),size=2)
    
    image = models.ImageField(upload_to='report_image', blank=True)
    
    report_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
    
