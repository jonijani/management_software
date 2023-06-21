from django.contrib import admin
from .models import *

class Staff_salary_packageAdmin(admin.ModelAdmin):
    list_display = ['staff', 'total_yearly_salary','weekly_salary', 'daily_salary','Hour_salary',  'minutes_salary', 'date']
    
class Staff_times_Admin(admin.ModelAdmin):
    list_display = ['name', 'd_date', 'start_time', 'end_time','hours_worked_field','hourly_wages', 'date']
    

class staff_infoAdmin(admin.ModelAdmin):
    list_display = ['U_name','first_name', 'last_name','home_number', 'mobile','nationility',  'passport_no', 'adress','postcode', 'bank_details']

admin.site.register(Staff_times,Staff_times_Admin)


admin.site.register(Staff_salary_package,Staff_salary_packageAdmin)
admin.site.register(staff_info,staff_infoAdmin)