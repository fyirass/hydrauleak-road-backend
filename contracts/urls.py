from django.urls import path
from .views import ClientList, ClientDetail, ContractList, ContractDetail

urlpatterns = [
    path('clients/', ClientList.as_view()),
    path('clients/<int:pk>/', ClientDetail.as_view()),
    path('contracts/', ContractList.as_view()),
    path('contracts/<int:pk>/', ContractDetail.as_view()),
]