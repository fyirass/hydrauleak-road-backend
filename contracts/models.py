from django.db import models
from django.utils.timezone import now
from clients.models import Client
# from maps.models import Zone

class Contract(models.Model):
    
    class ContractType(models.TextChoices):
        HIGHT = 'Hight'
        SIMPLE = 'Simple'
        PIPESEARCH = 'PipeSearch'
        
    class ContractStatus(models.TextChoices):
        NOTSTART = 'NotStart'
        PENDING = 'Pending'
        COMPLETED = 'expired'
        
    from django.db import models

    class ContractWorkType(models.TextChoices):
        FIRE_HYDRANT_INSPECTION = 'Fire_Hydrant_Inspection'
        ALL_CITY_INSPECTIONS = 'All_City_Inspections'
        CLARIFY_LEAK_LOCATION = 'Clarifying_the_location_of_the_leak'
        SOLVE_HIGH_CONSUMPTION = 'Solve_high_consumption_problem_but_the_leak_is_not_identified'

    class InterventionPublished(models.TextChoices):
        IS_PUBLISHED = 'Published'
        IS_NOT_PUBLISHED = 'Not Published'    
    
    client = models.ForeignKey(Client, on_delete=models.SET_NULL , related_name='contracts', null=True, blank=True)
    contract_title = models.CharField(max_length=150, blank=True)
    contract_description = models.TextField(blank=True)
    contract_type = models.CharField(max_length=50, choices=ContractType.choices, default=ContractType.SIMPLE, blank=True)
    contract_status = models.CharField(max_length=50, choices=ContractStatus.choices, default=ContractStatus.NOTSTART, blank=True)
    
    contract_work_type = models.CharField(max_length=200, default="Fire_Hydrant_Inspection", blank=True)
     
    contract_date = models.DateField(default=now, blank=True) 
    contract_estimate_end_date = models.DateField( blank=True) 

    
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=15, blank=True)
    
    is_published = models.CharField(max_length=50, choices=InterventionPublished.choices, default=InterventionPublished.IS_NOT_PUBLISHED)
    

    def __str__(self):
        return self.contract_title