from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . models import *
from datetime import datetime, time
from datetime import datetime
import time


def login_user(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Login successfull')
            return redirect('dashboard')

        
        else:
            messages.error(request,'login Failed')
            return redirect('login_user')
            # return HttpResponse('Invalid username or password')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')



# def staff(request):
#     hours = Staff_times.objects.filter(created_by=request.user)
    
    
#     if request.method == "POST":
#         start_time = request.POST.get('start_time')
        
#         end_time = request.POST.get('end_time')
        
#         date = datetime.now()
#         user = request.user
        
#         data = Staff_times(
#             start_time = start_time,
#             end_time = end_time,
#             date = date,
#             created_by = user
#         )
#         data.save()
        
#     context = {'hours_context':hours
#                }
        
        
#     return render(request,'staff.html',context)



        


