from rest_framework import viewsets
from .models import Admin
from user.models import User
from .serializers import AdminSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions

class AdminViewSet(viewsets.ModelViewSet):
    if User.is_admin:    
        queryset = Admin.objects.all()
        serializer_class = AdminSerializer
        permission_classes = [IsAuthenticated, IsAdminUser]
    else:
        Response({"error":"is not an admin"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)