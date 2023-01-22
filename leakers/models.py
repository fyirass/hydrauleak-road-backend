from django.db import models
from datetime import datetime
from user.models import User
from django.contrib.postgres.fields import ArrayField

   
class Leaker(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100,blank=True)
    inscription_date = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=20,choices=[('Active', 'active'), ('InBreak', 'in break'), ('NotWorking', 'not working')], default='not working')
    
   
    def __str__(self): 
        return (self.user.name)      
    
