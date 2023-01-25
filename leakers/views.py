from rest_framework import viewsets
from .models import Leaker
from .serializers import LeakerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions

class LeakerViewSet(viewsets.ModelViewSet):
      
    queryset = Leaker.objects.all()
    serializer_class = LeakerSerializer
    permission_classes = [IsAuthenticated]
