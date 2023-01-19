from django.urls import path
from .views import SignupView, UserView
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('signup/', SignupView.as_view()),
    # path('signin/', SigninView.as_view()),
    path('me/', UserView.as_view()),
]