from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeakerViewSet

router = DefaultRouter()
router.register(r'leakers', LeakerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

