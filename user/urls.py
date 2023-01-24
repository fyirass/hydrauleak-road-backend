from django.urls import path, include
from .views import SignupViewSet, UserViewSet, UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'me', UserView)
router.register(r'', UserViewSet)
router.register(r'signup', SignupViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
]