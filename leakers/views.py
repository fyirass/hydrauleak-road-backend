from rest_framework import viewsets
from .models import Leaker
from user.models import User
from .serializers import LeakerSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions

class LeakerViewSet(viewsets.ModelViewSet):
    if User.is_leaker:    
        queryset = Leaker.objects.all()
        serializer_class = LeakerSerializer
        permission_classes = [IsAuthenticated]
    else:
        Response({"error":"is not a leaker"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)