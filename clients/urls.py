from django.urls import path, include
from .views import *



urlpatterns = [
    
    path('', ClientListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', ClientView.as_view()),
    
]

