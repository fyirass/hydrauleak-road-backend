from django.db import models
from django.utils.timezone import now
from contracts.models import Contract
# from maps.models import Zone

class Intervention(models.Model):
    
    
    
    class InterventionType(models.TextChoices):
        HIGHT = 'Hight'
        SIMPLE = 'Simple'
        PIPESEARCH = 'PipeSearch'
        
    class InterventionStatus(models.TextChoices):
        NOTSTART = 'NotStart'
        PENDING = 'Pending'
        COMPLETED = 'Completed'
        
    class InterventionPublished(models.TextChoices):
        IS_PUBLISHED = 'Published'
        IS_NOT_PUBLISHED = 'Not Published'
        

    contract = models.ForeignKey(Contract, on_delete=models.DO_NOTHING)
    # zone = models.OneToOneField(Zone, on_delete=models.CASCADE, blank=True, null=True)
    intervention_title = models.CharField(max_length=150)
    intervention_description = models.TextField(blank=True)
    
    intervention_estimate_time = models.DateField(blank=True)
    intervention_leak_tool = models.CharField(max_length=50, blank=True)
    
    intervention_type = models.CharField(max_length=50, choices=InterventionType.choices, default=InterventionType.SIMPLE)
    intervention_status = models.CharField(max_length=50, choices=InterventionStatus.choices, default=InterventionStatus.NOTSTART)
    
    intervention_date = models.DateField(default=now, blank=True) 
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)
    
    is_published = models.CharField(max_length=50, choices=InterventionPublished.choices, default=InterventionPublished.IS_NOT_PUBLISHED)
    

    def __str__(self):
        return self.intervention_title