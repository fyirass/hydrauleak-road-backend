from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from leakers.models import Leaker


class Zone(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey('Map',related_name='map_zones', on_delete=models.CASCADE)
    zone_date = models.DateTimeField()
    zone_status = models.CharField(max_length=20,choices=[('notStart', 'Not Started'), ('Pending', 'Pending'), ('Completed', 'Completed')])
    zone_coordinates = ArrayField(models.FloatField(),size=200, default=list)
    
    def __str__(self):
        return self.zone_status
         
class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey('Map',related_name='map_sensors', on_delete=models.CASCADE)
    sensor_coordinates = ArrayField(models.FloatField(),size=2)
    sensor_creationdate = models.DateTimeField(default=datetime.now)
    sensor_photo = models.ImageField(upload_to='sensor', blank=True)
    sensor_type = models.CharField(max_length=50)
    sensor_title = models.CharField(max_length=100)
    sensor_description = models.TextField()
    sensor_frequency = ArrayField(ArrayField(models.FloatField(),size=2), blank=True)
    sensor_Indication = models.CharField(max_length=20,choices=[('critical', 'Critical'), ('notable', 'Notable'), ('good', 'Good'),('unknown', 'Unknown'), ('empty', 'Empty')])

    def __str__(self):
        return self.sensor_title

class LeakerVehicle(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey('Map',related_name='map_leaker_vehicles', on_delete=models.CASCADE)
    leaker = models.OneToOneField(Leaker, on_delete=models.CASCADE)
    leakervehicle_title = models.CharField(max_length=100)
    leakervehicle_description = models.TextField()

    def __str__(self):
        return self.leakervehicle_title
    
class PipeAcces(models.Model):
    id = models.AutoField(primary_key=True)
    pipe = models.ForeignKey('Pipe',related_name='pipe_accesses', on_delete=models.CASCADE)
    pipe_acces_coordinates = ArrayField(models.FloatField(),size=2)
    pipe_acces_title = models.CharField(max_length=100)
    pipe_acces_description = models.TextField()
    pipe_acces_type = models.CharField(max_length=20,choices=[('HouseValve', 'House Valve'), ('FirePole', 'Fire Pole'), ('FireHydrantValve', 'Fire Hydrant Valve'), ('Other', 'Other')])

    def __str__(self):
        return self.pipe_acces_title

class Mark(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey('Map',related_name='pipe_marks', on_delete=models.CASCADE)
    pipe = models.ForeignKey('Pipe',related_name='pipe_marks', on_delete=models.CASCADE)
    mark_points = ArrayField(models.FloatField(),size=2)
    mark_creation_date = models.DateTimeField(default=datetime.now)
    mark_photo = models.ImageField(upload_to='marks', blank=True)
    mark_description = models.TextField()

    def __str__(self):
        return self.mark_description

class Pipe(models.Model):
    id = models.AutoField(primary_key=True)
    map = models.ForeignKey('Map',related_name='map_pipes', on_delete=models.CASCADE)
    pipe_status = models.CharField(max_length=20,choices=[('good', 'Good'), ('unknown', 'Unknown'), ('critical', 'Critical')])
    pipe_description = models.TextField()
    pipe_creation_date = models.DateTimeField(default=datetime.now)
    pipe_type = models.CharField(max_length=50)
    pipe_title = models.CharField(max_length=100)
    pipe_length = models.FloatField()
    pipe_material = models.CharField(max_length=50)
    pipe_diametre = models.FloatField()
    pipe_acces_number = models.IntegerField(default=0)
    pipe_mark_number = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.pipe_acces_number = self.pipe_accesses.count()
        self.pipe_mark_number = self.pipe_marks.count()
        super(Pipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.pipe_title


class Map(models.Model):
    id = models.AutoField(primary_key=True)
    map_title = models.CharField(max_length=100)
    map_description = models.TextField()
    map_creation_date = models.DateTimeField(default=datetime.now)
    map_photo = models.ImageField(upload_to='maps', blank=True)
    zone_number = models.IntegerField(default=0)
    sensor_number = models.IntegerField(default=0)
    pipe_number = models.IntegerField(default=0)
    leakervehicle_number = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.zone_number = self.map_zones.count()
        self.sensor_number = self.map_sensors.count()
        self.pipe_number = self.map_pipes.count()
        self.leakervehicle_number = self.map_leaker_vehicles.count()
        super(Map, self).save(*args, **kwargs)

    def __str__(self):
        return self.map_title
   
        
# class ConcreteMap(Map):
#     objects = models.Manager()

#     class Meta:
#         proxy = True