from django.db import models

from PIL import Image






# class users(models.Model):
#     user_first_name = models.CharField(max_length=100)
#     user_last_name = models.CharField(max_length=100)
#     user_email = models.CharField(max_length=100)
#     user_password = models.CharField(max_length=10, null=True)

# class Profile(models.Model):
    
#     #user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
#     profile_pic = models.ImageField(default="profile2.png", null=True, blank=True, upload_to='profile_pics')
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     gender = models.CharField(max_length=200, default="Male", blank=True)
#     language = models.CharField(max_length=200, null=True, default="English", blank=True)
#     title = models.CharField(max_length=200, null=True, blank=True, default="None")
#     user_phone = models.CharField(max_length=200, null=True, blank=True, default="0000000000")
#     cell_phone = models.CharField(max_length=200, null=True, blank=True, default="0000000000")
#     fax_number = models.CharField(max_length=200, null=True, blank=True, default="0000000000")
#     postal = models.CharField(max_length=200, null=True, blank=True, default="None")
    
    
    
#     def __str__(self):
#         return f'{self.user.username} Profile'
    
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         super().save(force_insert, force_update, using, update_fields)
        
#         img = Image.open(self.profile_pic.path)
        
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.profile_pic.path)
            
 


class Report(models.Model):
    
    # profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    
    id = models.IntegerField(primary_key=True)
    reportObject = models.CharField( max_length=50)
    senderName = models.CharField( max_length=50)
    senderType = models.CharField( max_length=50)
    reportDate = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.reportObject
    

class Contract(models.Model):
    
    # profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    
    id = models.IntegerField(primary_key=True)   
    clientNameContract = models.CharField( max_length=50)
    contractData = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.clientNameContract
    
    
class Intervention(models.Model):
    
    # profile = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    
    id = models.IntegerField(primary_key=True)
    interventionObject = models.CharField( max_length=50)
    interventionType = models.CharField( max_length=50)
    
    interventionDate = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.intervetionObject   
    
    
    
class KpiTracking(models.Model):
    
    # profile = models.OneToOneField(Profile , null=True, on_delete=models.CASCADE)
    
    id = models.IntegerField(primary_key=True)
    LeakerKpi = models.CharField( max_length=50)
    NumberOfLeak = models.IntegerField()
    numWaterHyd = models.CharField( max_length=50)
    distance = models.CharField( max_length=50)
    
    leakerStartTime = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.LeakerKpi  
    
    
    
class Map(models.Model):
    
    id = models.IntegerField(primary_key=True)
    country = models.CharField( max_length=50)
    cityNumber = models.IntegerField()
    stateNumber = models.IntegerField()
    streets = models.CharField( max_length=50) 
    
    def __str__(self):
        return self.country  

 
class Zone(models.Model):
    
    map = models.ForeignKey(Map, null=True, on_delete= models.SET_NULL)
    
    id = models.IntegerField(primary_key=True)
    zoneCity = models.CharField( max_length=50)
    zoneColor = models.CharField( max_length=50)
    zoneCoordinates = models.IntegerField()
     
    
    def __str__(self):
        return self.zoneCity  
    
class Sensor(models.Model):
    
    map = models.ForeignKey(Map, null=True, on_delete= models.SET_NULL)
    
    id = models.IntegerField(primary_key=True)
    sensorNumber = models.IntegerField()
    sensorType = models.CharField( max_length=50)
    sensorCoordinates = models.IntegerField()
    sensorDetectionLength = models.IntegerField() 
    
    def __str__(self):
        return self.sensorNumber 
    
    
class Pipe(models.Model):
    
    map = models.ForeignKey(Map, null=True, on_delete= models.SET_NULL)
    
    id = models.IntegerField(primary_key=True)
    pipeNumber = models.IntegerField()
    pipeStreet = models.CharField( max_length=50)
    valves = models.CharField( max_length=50)
    pipeType = models.CharField( max_length=50)
    pipeColor = models.CharField( max_length=50)
    pipeAcces = models.CharField( max_length=50)
    
    
    def __str__(self):
        return self.pipeNumber 
    
    
class Pipe_acces(models.Model):
    
    pipe = models.ForeignKey(Pipe, null=True, on_delete= models.SET_NULL)
    
    id = models.IntegerField(primary_key=True)
   
    streetValveCor = models.CharField( max_length=50)
    houseValveCor = models.CharField( max_length=50)
    fireValveCor = models.CharField( max_length=50)
    
    
    
    def __str__(self):
        return self.id