from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Contract
from .serializers import ContractSerializer,ContractDetailSerializer
from datetime import datetime, timezone, timedelta

class ContractsView(ListAPIView):
    queryset = Contract.objects.order_by('-contract_date').filter(is_published = True)
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContractSerializer
    lookup_field = 'contract_title'
    
class ContractView(RetrieveAPIView):
    queryset = Contract.objects.order_by('-contract_date').filter(is_published = True)
    serializer_class = ContractDetailSerializer
    lookup_field = 'contract_title'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContractSerializer
    
    def post(self, request, format=None):
        queryset = Contract.objects.order_by('-contract_date').filter(is_published = True)
        data = self.request.data
        
        contract_type = data['contract_type']
        queryset = queryset.filter(contract_type__iexact=contract_type)
        
        serializer = ContractSerializer(queryset, many=True)

        return Response(serializer.data)