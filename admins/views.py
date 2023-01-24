from rest_framework import viewsets
from .models import Admin
from user.models import User
from .serializers import AdminSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, permissions

class AdminViewSet(viewsets.ModelViewSet):
    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.roles=="is_admin":
            return permissions.IsAuthenticated
        return IsAdminUser
      
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [has_permission]

        