from rest_framework import viewsets
from .serializers import InterventionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Intervention

class InterventionViewSet(viewsets.ModelViewSet):
    
    permissions_classes = [IsAuthenticated]
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    
    
    
