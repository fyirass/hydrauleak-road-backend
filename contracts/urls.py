from django.urls import path
from .views import *

urlpatterns = [
    path('', ContractsView.as_view()),
    path('search', SearchView.as_view()),
    path('<contract_title>', ContractView.as_view()),
]
