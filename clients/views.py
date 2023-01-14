from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Client
from .serializers import ClientSerializer

class ClientListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = None 

class ClientView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    # queryset = Client.objects.filter(top_seller=True)
    serializer_class = ClientSerializer
    pagination_class = None