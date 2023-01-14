from django.urls import path
from .views import *

urlpatterns = [
    path('manage', ManageInterventionView.as_view()),
    
]
