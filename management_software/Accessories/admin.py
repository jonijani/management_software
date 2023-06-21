from django.contrib import admin
from .models import *

class Retail_AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['id','devices', 'make', 'model', 'acce_name', 'acce_colour', 'supplier', 'cost','retail_price',  'acce_status', 'user', 'date'  ]



admin.site.register([ Acceesories_name,Acceesories_status])

admin.site.register(Retail_Accessories,Retail_AccessoriesAdmin)


