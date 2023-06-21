from django.contrib import admin
from .models import *


class InventoriesAdmin(admin.ModelAdmin):
    list_display = [ 'part_no','part_status','barcode', 'devices','make', 'model', 'part_name', 'part_colour',  'supplier', 'cost','created_date', 'created_by']

class Request_partsAdmin(admin.ModelAdmin):
    list_display = [ 'id' ,'devices','make', 'model', 'part_name', 'part_colour',  'supplier', 'buying_cost', 'created_date', 'created_by']


# class Ordered_partsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'devices','make', 'model', 'part_name', 'part_colour',  'supplier', 'buying_cost','eta', 'comments', 'created_date', 'created_by']


class Ordered_partsAdmin(admin.ModelAdmin):
    list_display = ['requested_parts_ID','id', 'part_status', 'eta', 'comments', 'created_date', 'created_by']




admin.site.register([ Part_name, Part_colour, Supplier,Part_status])

admin.site.register(Inventories,InventoriesAdmin)
admin.site.register(Request_parts,Request_partsAdmin)
admin.site.register(Ordered_parts,Ordered_partsAdmin)






