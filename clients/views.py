from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions

class ClientViewSet(viewsets.ModelViewSet):
    
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None