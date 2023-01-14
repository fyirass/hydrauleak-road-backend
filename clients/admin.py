from django.contrib import admin
from .models import Client
# Register your models here.



class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_intervention')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Client, ClientAdmin)