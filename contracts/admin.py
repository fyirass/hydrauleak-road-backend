from django.contrib import admin
from .models import Contract

class ContractAdmin(admin.ModelAdmin):
    contract_display = ('id', 'contract_title', 'is_published', 'contract_status', 'contract_date', 'client')
    contract_display_display_links = ('id', 'contract_title')
    contract_display_filter = ('client', )
    contract_display_editable = ('is_published', )
    search_fields = ('contract_title', 'contract_description', 'address', 'city', 'state', 'zipcode', 'contract_status')
    contract_display_per_page = 25

admin.site.register(Contract, ContractAdmin)
 