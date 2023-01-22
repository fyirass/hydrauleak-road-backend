from django.urls import path, include
from .views import ReportViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
