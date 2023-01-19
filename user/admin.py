from django.contrib import admin
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'is_admin', 'is_leaker', 'is_client')
    search_fields = ('email',)

admin.site.register(get_user_model(), UserAdmin)