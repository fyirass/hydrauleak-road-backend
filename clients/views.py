from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions
from user.models import User

class ClientViewSet(viewsets.ModelViewSet):
    if User.is_client:  
        queryset = Client.objects.all()
        serializer_class = ClientSerializer
        permission_classes = [IsAuthenticated]
    else:
        Response({"error":"Is not an client"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
 