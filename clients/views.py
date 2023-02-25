
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ClientSerializer, ClientWriteSerializer
from .models import Client, ClienTFile, User


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = None
    
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return ClientWriteSerializer
        return ClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('user')

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(f"User with id {user_id} does not exist", status=400)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(methods=['get'], detail=True)
    def full(self, request, pk=None):
        client = self.get_object()
        serializer = ClientSerializer(client, context={'request': request})
        return Response(serializer.data, status=200)

    @action(methods=['post'], detail=True)
    def add_file(self, request, pk=None):
        client = self.get_object()
        file_obj = request.FILES.get('file')
        client_file = ClienTFile.objects.create(Client_file=file_obj)
        client.client_files.add(client_file)
        serializer = ClientSerializer(client, context={'request': request})
        return Response(serializer.data, status=200)

    @action(methods=['delete'], detail=True)
    def remove_file(self, request, pk=None):
        client = self.get_object()
        file_id = request.query_params.get('file_id')
        client.client_files.filter(id=file_id).delete()
        serializer = ClientSerializer(client, context={'request': request})
        return Response(serializer.data, status=200)