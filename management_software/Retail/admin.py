from django.contrib import admin

from .models import *

class Customer_cartAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_job_id',  'deliver_cost','get_imei', 'get_make', 'get_model','delivery_comments', 'payment_type',]

class Daiy_saleAdmin(admin.ModelAdmin):
    list_display = ['id', 'job_deliver', 'device_deliver','make_deliver', 'model_deliver', 'fault_deliver', 'imei_deliver', 'cost_deliver','payment_type_daily_sale',  'sale_person','date']

# class Acce_CartAdmin(admin.ModelAdmin):
#     list_display = ['id', 'cart.acce_name']

class Sold_accAdmin(admin.ModelAdmin):
    list_display = ['id', 'payment_type', 'delivery_comments',   'retail_price',  'user', 'date'  ]

class Daily_totalsAdmin(admin.ModelAdmin):
    list_display = ['total', 'date'  ]



admin.site.register([Payment_type, Acce_Cart, Email_admin_list  ])


admin.site.register(Customer_cart,Customer_cartAdmin )  
admin.site.register(Daily_sale,Daiy_saleAdmin)
#admin.site.register(Acce_Cart,Acce_CartAdmin)

admin.site.register(Sold_acc,Sold_accAdmin)
admin.site.register(Daily_totals,Daily_totalsAdmin)