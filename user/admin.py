from django.contrib import admin
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'roles')
    search_fields = ('email','name')

admin.site.register(get_user_model(), UserAdmin)