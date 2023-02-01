from django.shortcuts import render
from rest_framework import viewsets
from .models import Zone, Sensor, Pipe, PipeAcces, Mark, LeakerVehicle, Map
from .serializers import ZoneSerializer, SensorSerializer, PipeSerializer, PipeAccesSerializer, MarkSerializer, LeakerVehicleSerializer, MapSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        response = {'count': count, 'data': serializer.data}
        return Response(response)

    

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        response = {'count': count, 'data': serializer.data}
        return Response(response)

class PipeViewSet(viewsets.ModelViewSet):
    queryset = Pipe.objects.all()
    serializer_class = PipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        response = {'count': count, 'data': serializer.data}
        return Response(response)

class PipeAccesViewSet(viewsets.ModelViewSet):
    queryset = PipeAcces.objects.all()
    serializer_class = PipeAccesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        response = {'count': count, 'data': serializer.data}
        return Response(response)

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        response = {'count': count, 'data': serializer.data}
        return Response(response)

class LeakerVehicleViewSet(viewsets.ModelViewSet):
    queryset = LeakerVehicle.objects.all()
    serializer_class = LeakerVehicleSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        response = {'count': count, 'data': serializer.data}
        return Response(response)

class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        serializer = self.get_serializer(queryset, many=True)
        response = {'count': count, 'data': serializer.data}
        return Response(response)
