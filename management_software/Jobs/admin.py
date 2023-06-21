from django.contrib import admin
from .models import *

class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'devices']

class JobsAdmin(admin.ModelAdmin):
    list_display = ['customer','id','job_status','cost', 'device', 'make', 'model', 'imei', 'fault', 'payment_status']

class CompleteAdmin(admin.ModelAdmin):
    list_display = ['c_job', 'complete_update', 'completed_by', 'payment_status_com', 'cost_com', 'completed_on']

class DeliveredAdmin(admin.ModelAdmin):
    list_display = ['job_deliver', 'make_deliver', 'model_deliver', 'fault_deliver', 'imei_deliver','cost_deliver', 'delivered_on','delivered_by','delivery_comments']

admin.site.register([Make,Model,Fault, Accessories, Sale_item, Network, Job_status,Job_update, Fingerprints, Reciepts ,Job_rebook , Pictures])
admin.site.register(Devices,DevicesAdmin)
admin.site.register(Jobs,JobsAdmin)
admin.site.register(Complete_job,CompleteAdmin)
admin.site.register(Delivered,DeliveredAdmin)










