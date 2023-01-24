from rest_framework import viewsets
from .models import Leaker
from .serializers import LeakerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions

class LeakerViewSet(viewsets.ModelViewSet):
    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.roles=="is_leaker":
            return permissions.IsAuthenticated
        return IsAdminUser    
    queryset = Leaker.objects.all()
    serializer_class = LeakerSerializer
    permission_classes = [IsAuthenticated]
