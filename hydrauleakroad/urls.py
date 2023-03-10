from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('api/user/', include('user.urls')),
    
    
    path('api/', include('leakers.urls')),
    path('api/', include('clients.urls')),
    path('api/', include('admins.urls')),
    path('api/', include('contracts.urls')),
    path('api/', include('interventions.urls')),
    path('api/', include('maps.urls')),
    path('api/', include('reports.urls')),

    
    
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('djoser.social.urls')),
    
    
    
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]