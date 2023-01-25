from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions

class ClientViewSet(viewsets.ModelViewSet):
    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.roles=="is_client" or request.user.roles=="is_admin":
            return permissions.IsAuthenticated
        return IsAdminUser
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [has_permission]
    