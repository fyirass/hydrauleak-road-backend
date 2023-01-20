from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZoneViewSet, SensorViewSet, PipeViewSet, PipeAccesViewSet, MarkViewSet, LeakerVehicleViewSet, MapViewSet

router = DefaultRouter()
router.register(r'zones', ZoneViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'pipes', PipeViewSet)
router.register(r'pipeacces', PipeAccesViewSet)
router.register(r'marks', MarkViewSet)
router.register(r'leakervehicles', LeakerVehicleViewSet)
router.register(r'maps', MapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]