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
        
    from django.db import models

    class ContractWorkType(models.TextChoices):
        FIRE_HYDRANT_INSPECTION = 'Fire Hydrant Inspection'
        ALL_CITY_INSPECTIONS = 'All City Inspections'
        CLARIFY_LEAK_LOCATION = 'Clarifying the location of the leak'
        SOLVE_HIGH_CONSUMPTION = 'Solve high consumption problem but the leak is not identified'

    class InterventionPublished(models.TextChoices):
        IS_PUBLISHED = 'is_published'
        IS_NOT_PUBLISHED = 'iq_not_published'    
    
    client = models.ForeignKey(Client, on_delete=models.SET_NULL , related_name='contracts', null=True, blank=True)
    zone = models.OneToOneField(Zone, on_delete=models.CASCADE, blank=True, null=True)
    contract_title = models.CharField(max_length=150, blank=True)
    contract_description = models.TextField(blank=True)
    contract_type = models.CharField(max_length=50, choices=ContractType.choices, default=ContractType.SIMPLE, blank=True)
    contract_status = models.CharField(max_length=50, choices=ContractStatus.choices, default=ContractStatus.NOTSTART, blank=True)
    
    contract_work_type = models.CharField(max_length=200, choices=ContractWorkType.choices, default=ContractWorkType.FIRE_HYDRANT_INSPECTION, blank=True)
     
    contract_date = models.DateField(default=now, blank=True)
    
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)
    
    is_published = models.CharField(max_length=50, choices=InterventionPublished.choices, default=InterventionPublished.IS_NOT_PUBLISHED)
    

    def __str__(self):
        return self.contract_title