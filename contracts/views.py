from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Contract
from .serializers import *
from rest_framework.decorators import permission_classes
# from clients.models import Client


class IsClient(permissions.BasePermission):
    
    
    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.roles=="is_client":
            return permissions.IsAuthenticated
        return False 
    
class IsLeaker(permissions.BasePermission):

    
    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.roles=="is_leaker":
            return permissions.IsAuthenticated
        return False 
    
class IsAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        if request.user.is_authenticated and request.user.roles=="is_admin":
            return permissions.IsAuthenticated
        return False 

class ContractList(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        if request.user.roles=="is_leaker" or request.user.roles=="is_admin" or request.user.roles=="is_client":
            contracts = Contract.objects.all()
            serializer = ContractSerializer(contracts, many=True)
            return Response(serializer.data)
        else:
            return Response({"UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self, request):
        if request.user.roles=="is_admin":
            serializer = ClientContractSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)

class ContractDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return Contract.objects.get(pk=pk)
        except Contract.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
  
    def get(self, request, pk):
        
        if request.user.roles=="is_leaker" or request.user.roles=="is_admin":
            contract = self.get_object(pk)
            serializer = ContractSerializer(contract)
            return Response(serializer.data)
        else:
            return Response({"UNAUTHORIZED"},status=status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, pk):
        if request.user.roles== "is_admin":
            contract = self.get_object(pk)
            serializer = ContractSerializer(contract, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"UNAUTHORIZED"},status=status.HTTP_401_UNAUTHORIZED)
        
    
    def delete(self, request, pk):
        if request.user.roles== "is_admin":    
            contract = self.get_object(pk)
            contract.delete()
            return Response({"success", "Contract deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"UNAUTHORIZED"},status=status.HTTP_401_UNAUTHORIZED)