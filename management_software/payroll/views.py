from unicodedata import name
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from datetime import datetime, time
from datetime import datetime
import datetime as dt








def staff_salary_package(request):
    salary = Staff_salary_package.objects.all() 
    
    context = {'salary':salary,
        
             }
        
    return render(request,'staff_salary_package.html',context)










def staff(request):
    
    
    if request.method == "POST":
        date = request.POST.get('date_name')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')  
        diff_time = request.POST.get('diff_name')   
       
        
        date = datetime.now()
        user = request.user
        
        a = start_time
        b = end_time
        
        t1 = datetime.strptime(a, "%H:%M")
        print('Start time:', t1.time())
        
        t2 = datetime.strptime(b, "%H:%M")
        print('End time:', t2.time())
        
        time_diff1 = t2 - t1
        
        
        
        staff_v = Staff_salary_package.objects.filter(staff=request.user).first()
        data = Staff_times(
            name = staff_v,
            d_date = date,
            start_time = start_time,
            end_time = end_time,
            hours_worked_field = time_diff1,
            
            date = date,
            
        )
        data.save()
    

        time_converion = str(data.hours_worked_field)[:3].replace(':','')
        if time_converion == "10":
            time_converion= "01"
        elif time_converion =="20":
            time_converion="02" 
        elif time_converion =="30":
            time_converion="03"
        elif time_converion =="40":
            time_converion="04" 
        elif time_converion =="50":
            time_converion="05" 
        elif time_converion =="60":
            time_converion="06" 
        elif time_converion =="70":
            time_converion="07" 
        elif time_converion =="80":
            time_converion="08" 
        elif time_converion =="90":
            time_converion="09" 
        
       
        # minutes_worked = time_converion * 60   
            
        hour_into_time1 =  int(time_converion) * data.name.Hour_salary()   
        hour_into_time = "{:.2f}".format(hour_into_time1)
        
        # print(time_converion,data.name.minutes_salary())
        data_v = Staff_times.objects.filter(id=data.id).update(hourly_wages=hour_into_time)
        
    hours_worked = Staff_times.objects.filter(name__staff=request.user)    
    context = {'hours_worked_context':hours_worked
               }
      
    return render(request,'staff.html',context)







    
# def time_and_wages(request):
#     # a = Staff_times.objects.filter(name__staff=request.user)
#     h_hours = Staff_times.objects.all()
    
    
#     context = {'hours_context':h_hours}
    
        
#     return render(request,'staff.html',context)







