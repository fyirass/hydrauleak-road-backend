from django.urls import path
from .views import SignupView, UserView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('me/', UserView.as_view()),
]