from rest_framework import serializers
from .models import Contract

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('contract_title', 'contract_type', 'contract_status', 'contract_date', 'address', 'city', 'state')

class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
        lookup_field = 'contract_title'
