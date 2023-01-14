import imp
from pickle import FROZENSET
from re import T
import re
from urllib import response
from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()


    
@api_view(['GET', 'POST'])
def contract_list(request):
    if request.method == 'GET':
        contracts = Contract.objects.all()
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def contract_detail (request, id, format=None) :
    
    try:
        contract = Contract.objects.get(pk=id)
    except Contract.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = ContractSerializer(contract)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = ContractSerializer(contract, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        contract.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'POST'])
def intervention_list(request):
    if request.method == 'GET':
        orders = Intervention.objects.all()
        serializer = InterventionSerializer(orders, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = InterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def intervention_detail (request, id, format=None) :
    
    try:
        intervention = Intervention.objects.get(pk=id)
    except Intervention.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = InterventionSerializer(intervention)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = InterventionSerializer(intervention, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        intervention.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'POST'])
def intervention_list(request):
    if request.method == 'GET':
        interventions = Intervention.objects.all()
        serializer = InterventionSerializer(interventions, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = InterventionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def kpiTracking_detail (request, id, format=None) :
    
    try:
        kpiTracking = KpiTracking.objects.get(pk=id)
    except KpiTracking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = KpiTrackingSerializer(kpiTracking)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = KpiTrackingSerializer(kpiTracking, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        kpiTracking.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
    
@api_view(['GET', 'POST'])
def kpiTracking_list(request):
    if request.method == 'GET':
        kpiTrackings = KpiTracking.objects.all()
        serializer = KpiTrackingSerializer(kpiTrackings, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = KpiTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def map_detail (request, id, format=None) :
    
    try:
        map = Map.objects.get(pk=id)
    except Map.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = MapSerializer(map)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = MapSerializer(map, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        map.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
    
@api_view(['GET', 'POST'])
def map_list(request):
    if request.method == 'GET':
        maps = Map.objects.all()
        serializer = MapSerializer(maps, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def zone_detail (request, id, format=None) :
    
    try:
        zone = Zone.objects.get(pk=id)
    except Zone.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = ZoneSerializer(zone)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = ZoneSerializer(zone, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        zone.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'POST'])
def zone_list(request):
    if request.method == 'GET':
        zones = Zone.objects.all()
        serializer = ZoneSerializer(zones, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ZoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def sensor_detail (request, id, format=None) :
    
    try:
        sensor = Sensor.objects.get(pk=id)
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = SensorSerializer(sensor, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        sensor.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'POST'])
def sensor_list(request):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        

@api_view(['GET', 'PUT', 'DELETE'])
def pipe_detail (request, id, format=None) :
    
    try:
        pipe = Pipe.objects.get(pk=id)
    except Pipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = PipeSerializer(pipe)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = PipeSerializer(pipe, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    elif request.method =='DELETE':
        pipe.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
    
    
    
@api_view(['GET', 'POST'])
def pipe_list(request):
    if request.method == 'GET':
        pipes = Pipe.objects.all()
        serializer = PipeSerializer(pipes, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        


        
        
# @api_view(['GET', 'POST'])
# def order_list(request):
#     if request.method == 'GET':
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def order_detail (request, id, format=None) :
    
#     try:
#         order = Order.objects.get(pk=id)
#     except Order.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
    
#     if request.method == 'GET':
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)
    
#     elif request.method =='PUT':
#         serializer = OrderSerializer(order, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
#     elif request.method =='DELETE':
#         order.delete()
#         return Response (status=status.HTTP_204_NO_CONTENT)
    
    


# @api_view(['GET', 'POST'])
# def profile_list(request):
#     if request.method == 'GET':
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def profile_detail (request, id, format=None) :
    
#     try:
#         profile = Profile.objects.get(pk=id)
#     except Profile.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
    
#     if request.method == 'GET':
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)
    
#     elif request.method =='PUT':
#         serializer = ProfileSerializer(profile, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
#     elif request.method =='DELETE':
#         profile.delete()
#         return Response (status=status.HTTP_204_NO_CONTENT)
 