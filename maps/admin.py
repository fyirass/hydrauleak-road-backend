from django.contrib import admin
from .models import Zone, Sensor, Pipe, PipeAcces, Mark, LeakerVehicle, Map

admin.site.register(Zone)
admin.site.register(Sensor)
admin.site.register(Pipe)
admin.site.register(PipeAcces)
admin.site.register(Mark)
admin.site.register(LeakerVehicle)
admin.site.register(Map)