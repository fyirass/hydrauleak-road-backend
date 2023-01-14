from django.contrib import admin
from django.urls import path, include
from accounts import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignupView, RetrieveUserView

urlpatterns = [

    path('signup', SignupView.as_view()),
    path('me', RetrieveUserView.as_view()),
    
    ]

urlpatterns = format_suffix_patterns(urlpatterns)