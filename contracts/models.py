from django.db import models
from django.utils.timezone import now
from clients.models import Client
from maps.models import Zone

class Contract(models.Model):
    
    class ContractType(models.TextChoices):
        HIGHT = 'Hight'
        SIMPLE = 'Simple'
        PIPESEARCH = 'PipeSearch'
        
    class ContractStatus(models.TextChoices):
        NOTSTART = 'NotStart'
        PENDING = 'Pending'
        COMPLETED = 'Completed'

    
    client = models.ForeignKey(Client, on_delete=models.SET_NULL , related_name='contracts')
    zone = models.OneToOneField(Zone, on_delete=models.CASCADE, blank=True, null=True)
    contract_title = models.CharField(max_length=150)
    contract_description = models.TextField(blank=True)
    contract_type = models.CharField(max_length=50, choices=ContractType.choices, default=ContractType.SIMPLE)
    contract_status = models.CharField(max_length=50, choices=ContractStatus.choices, default=ContractStatus.NOTSTART)
    
     
    contract_date = models.DateTimeField(default=now, blank=True)
    
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    
    is_published = models.BooleanField()
    

    def __str__(self):
        return self.contract_title