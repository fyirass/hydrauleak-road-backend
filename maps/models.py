from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from leakers.models import Leaker

class Map(models.Model):
    id = models.AutoField(primary_key=True)
    map_coordinate = ArrayField(models.FloatField(),size=2, default=list)
    map_title = models.CharField(max_length=100)
    map_description = models.TextField()
    map_creation_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.map_title
    
class Zone(models.Model):
    
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.SET_NULL, related_name="maps", null=True, blank=True)
    zone_num = models.IntegerField(default=0)
    zone_date = models.DateTimeField(default=datetime.now)
    zone_status = models.CharField(max_length=20,choices=[('notStart', 'Not Started'), ('Pending', 'Pending'), ('Completed', 'Completed')], default= "notStart")
    zone_color = models.CharField(max_length=20,choices=[('#97c900', 'Green'), ('#fc8d49', 'Orange'), ('#ff1919', 'Red')], default= "#fc8d49")
    zone_area = models.FloatField(default=0)
    zone_coordinates = ArrayField(
        ArrayField(models.FloatField(max_length=255)), 
        size=None, # size = None means it can be a dynamic array
    )
    def __str__(self):
        return self.zone_status
         
class Sensor(models.Model):
    
    id = models.AutoField(primary_key=True)
    pipe = models.ForeignKey('Pipe',related_name='pipe_sensors', on_delete=models.CASCADE, null=True, blank=True)
    sensor_coordinates = ArrayField(models.FloatField(),size=2)
    sensor_creation_date = models.DateTimeField(default=datetime.now)
    sensor_photo = models.ImageField(upload_to='sensor', blank=True)
    sensor_type = models.CharField(max_length=50)
    sensor_title = models.CharField(max_length=100)
    sensor_description = models.TextField()
    sensor_diameter_range = models.FloatField(default=0)
    sensor_frequency = ArrayField(ArrayField(models.FloatField()), blank=True,size=2)
    sensor_Indication = models.CharField(max_length=20,choices=[('critical', 'Critical'), ('notable', 'Notable'), ('good', 'Good'),('unknown', 'Unknown'), ('empty', 'Empty')], default='unknown')

    def __str__(self):
        return self.sensor_title

class LeakerVehicle(models.Model):
    
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.SET_NULL, null=True, blank=True)
    leaker = models.OneToOneField(Leaker, on_delete=models.CASCADE)
    leaker_coordinates = ArrayField(models.FloatField(), size=2)
    leaker_vehicle_title = models.CharField(max_length=100)
    leaker_vehicle_description = models.TextField()

    def __str__(self):
        return self.leaker_vehicle_title
    
class PipeAcces(models.Model):
    id = models.AutoField(primary_key=True)
    pipe = models.ForeignKey('Pipe',related_name='pipe_accesses', on_delete=models.CASCADE)
    pipe_access_coordinates = ArrayField(models.FloatField(),size=2)
    pipe_access_title = models.CharField(max_length=100)
    pipe_access_description = models.TextField()
    pipe_access_type = models.CharField(max_length=20,choices=[('HouseValve', 'House Valve'), ('FirePole', 'Fire Pole'), ('FireHydrantValve', 'Fire Hydrant Valve'), ('Other', 'Other')], default='other')

    def __str__(self):
        return self.pipe_access_title

class Mark(models.Model):
    id = models.AutoField(primary_key=True)
    pipe = models.ForeignKey('Pipe',related_name='pipe_marks', on_delete=models.CASCADE)
    mark_coordinates = ArrayField(models.FloatField(),size=2)
    mark_creation_date = models.DateTimeField(default=datetime.now)
    mark_photo = models.ImageField(upload_to='marks', blank=True)
    mark_description = models.TextField()

    def __str__(self):
        return self.mark_description

class Pipe(models.Model):
    
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey(Map, on_delete=models.SET_NULL, null=True, blank=True)
    pipe_status = models.CharField(max_length=20,choices=[('good', 'Good'), ('unknown', 'Unknown'), ('critical', 'Critical')], default='unknown')
    pipe_description = models.TextField()
    pipe_coordinates = ArrayField(
        ArrayField(models.FloatField(max_length=255)), 
        size=None, # size = None means it can be a dynamic array
    )
    pipe_creation_date = models.DateTimeField(default=datetime.now)
    pipe_type = models.CharField(max_length=50)
    pipe_title = models.CharField(max_length=100)
    pipe_length = models.FloatField()
    pipe_material = models.CharField(max_length=50)
    pipe_diameter = models.FloatField()
    pipe_access_number = models.IntegerField(default=0, blank=True)
    pipe_mark_number = models.IntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        self.pipe_access_number = self.pipe_accesses.count()
        self.pipe_mark_number = self.pipe_marks.count()
        super(Pipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.pipe_title


