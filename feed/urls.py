from django.contrib import admin
from django.urls import path, include
from feed import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
    
    # path('api/profiles/',views.profile_list),
    # path('api/Profiles/<int:id>', views.profile_detail),
    
    path('api/contracts/',views.contract_list),
    path('api/contracts/<int:id>', views.contract_detail),
    
    path('api/interventions/',views.intervention_list),
    path('api/interventions/<int:id>', views.intervention_detail),

    path('api/kpiTrackings/',views.kpiTracking_list),
    path('api/kpiTrackings/<int:id>', views.kpiTracking_detail),
    
    path('api/maps/',views.map_list),
    path('api/maps/<int:id>', views.map_detail),
    
    path('api/zones/',views.zone_list),
    path('api/zones/<int:id>', views.zone_detail),
    
    path('api/sensors/',views.sensor_list),
    path('api/sensors/<int:id>', views.sensor_detail),
    
    path('api/pipes/',views.pipe_list),
    path('api/pipes/<int:id>', views.pipe_detail),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)