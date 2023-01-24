from django.db import models
from django.utils.timezone import now
from contracts.models import Contract
from maps.models import Zone

class Intervention(models.Model):
    
    
    
    class InterventionType(models.TextChoices):
        HIGHT = 'Hight'
        SIMPLE = 'Simple'
        PIPESEARCH = 'PipeSearch'
        
    class InterventionStatus(models.TextChoices):
        NOTSTART = 'NotStart'
        PENDING = 'Pending'
        COMPLETED = 'Completed'

    contract = models.ForeignKey(Contract, on_delete=models.DO_NOTHING)
    zone = models.OneToOneField(Zone, on_delete=models.CASCADE, blank=True, null=True)
    intervention_title = models.CharField(max_length=150)
    intervention_description = models.TextField(blank=True)
    
    intervention_type = models.CharField(max_length=50, choices=InterventionType.choices, default=InterventionType.SIMPLE)
    intervention_status = models.CharField(max_length=50, choices=InterventionStatus.choices, default=InterventionStatus.NOTSTART)
    
    intervention_date = models.DateTimeField(default=now, blank=True) 
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    
    is_published = models.BooleanField(default=True)
    

    def __str__(self):
        return self.intervention_title