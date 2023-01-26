from rest_framework import serializers
from .models import Client, Contract
from user.models import User
from clients.serializers import ClientSerializer

class ContractSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = Contract
        fields = ('client','id', 'zone', 'contract_title', 'contract_description', 'contract_type',
                    'contract_status', 'contract_work_type', 'contract_date', 'address', 'city', 'state', 'zipcode', 'is_published')