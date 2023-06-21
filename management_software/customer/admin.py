from django.contrib import admin
from .models import *
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['created_date']

    list_display = ['id', 'client_type', 'first_name', 'last_name', 'email']
admin.site.register(Customer,CustomerAdmin)


