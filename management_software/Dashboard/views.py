from django.shortcuts import render
from Retail.models import *
from Inventories.models import *
from Jobs.models import *
from Accessories.models import *

# def daily_sale_report_dashboard(request):
#     jobs_list_total = []
#     daily_date = Daily_sale.objects.filter(date__date = datetime.datetime.today()).count()
    
    
#     daily_total = Daily_sale.objects.all()
    
    
#     for i in daily_total:
        
#         jobs_list_total.append(i.cost_deliver)
#     total_job = sum(jobs_list_total) 
    


    
#     context = {'daily_context':daily_date,
#                'daily_total_context':daily_total,
#                'total_job_context':total_job
#                }
#     return render(request,'Dashboard/daily_sale_report_dashboard.html', context)







def daily_sale_report_dashboard(request):
    date = datetime.datetime.now()
    
    jobs_list_total = []
    daily_total_list = []
    daily_total_date_list = []
    acc_list_total = []
    
    
    daily_date = Daily_sale.objects.filter(date__date = datetime.datetime.today()).count()
    if request.method == "POST":
        start_range = request.POST.get('start_range')
        end_range = request.POST.get('end_range')
        
        daily_total = Daily_totals.objects.filter(date__range=[start_range, end_range])
        
    else:
        
        daily_total = Daily_totals.objects.all()
        
    
    
    
    
    
    sold_acc_daily_sale = Sold_acc.objects.filter(date__date=date)
    
    for i in daily_total:
        
        daily_total_list.append(int(i.total))
    net_total = sum(daily_total_list)
        
    for i in daily_total:
        i = str(i.date)
        i = i[0:10]
        daily_total_date_list.append(str(i))
        
    for accessories in sold_acc_daily_sale:
        acc_list_total.append(int(accessories.retail_price))
        total_accessories = sum(acc_list_total)
        
        
    
        
    
    context = {'daily_context':daily_date,
               'daily_total_context':daily_total,
               'daily_total_list_context':daily_total_list,
               'daily_total_date_list_context':daily_total_date_list,
               'net_total_context':net_total,
               
               
               }
    return render(request,'Dashboard/daily_sale_report_dashboard.html', context)
















def client_dashboard(request):
    retail = Customer.objects.filter(client_type = 'retail').count()
    corporate = Customer.objects.filter(client_type = 'corporate').count()
    context = {'retail_count_context': retail,
               'corporate_count_context':corporate}
    return render(request,'Dashboard/client_dashboard.html', context)









def jobs_dashboard(request):
    pending_list = []
    pending_count = []
    complete_list = []
    waiting_for_parts_list =[]
    waiting_for_approval_list =[]
    
    jobs =  Jobs.objects.filter(job_status__job_status= 'pending')
    pending_jobs_count =  Jobs.objects.filter(job_status__job_status= 'pending').count()
    
    completed_jobs =  Jobs.objects.filter(job_status__job_status= 'Completed')
    completed_jobs_count =  Jobs.objects.filter(job_status__job_status= 'Completed').count()
    
    waiting_for_parts_jobs =  Jobs.objects.filter(job_status__job_status= 'waiting for parts')
    waiting_for_parts_jobs_count =  Jobs.objects.filter(job_status__job_status= 'waiting for parts').count()
    
    waiting_for_approval_jobs =  Jobs.objects.filter(job_status__job_status= 'Waiting for approval')
    waiting_for_approval_counts =  Jobs.objects.filter(job_status__job_status= 'Waiting for approval').count()
    
    
    for i in jobs:
        pending_list.append(i.cost)
    Total_pending_jobs = sum(pending_list)
    
    for i in completed_jobs:
        complete_list.append(i.cost)
    Total_complete_jobs = sum(complete_list)
    
    for i in waiting_for_parts_jobs:
        waiting_for_parts_list.append(i.cost)
    Total_waiting_for_parts_list = sum(waiting_for_parts_list)
    
    for i in waiting_for_approval_jobs:
        waiting_for_approval_list.append(i.cost)
    Total_waiting_for_approval_list = sum(waiting_for_approval_list)
    
    
    
    context = {
        'Total_pending_jobs':Total_pending_jobs,
        'pending_jobs_count':pending_jobs_count,
        'Total_complete_jobs':Total_complete_jobs,
        'completed_jobs_count':completed_jobs_count,
        'Total_waiting_for_parts_list':Total_waiting_for_parts_list,
        'waiting_for_parts_jobs_count':waiting_for_parts_jobs_count,
        'Total_waiting_for_approval_list':Total_waiting_for_approval_list,
        'waiting_for_approval_counts':waiting_for_approval_counts
    }
    return render(request,'Dashboard/jobs_dashboard.html',context)





















def Accessories_dashboard(request):
    mobile_acc_list =[]
    mobile_acc_retail_worth_list =[]
    
    
    laptop_acc_cost_list =[]
    laptop_acc_retail_worth_list = []
    tablet_acc_cost_list =[]
    tablet_acc_retail_cost_list =[]
    Total_accessories_net_cost_list = []
    
    mobile_acc = Retail_Accessories.objects.filter(devices__devices='Mobile')
    mobile_acc_retail_worth = Retail_Accessories.objects.filter(devices__devices='Mobile')
    mobile_acc_count = Retail_Accessories.objects.filter(devices__devices='Mobile').count()
    
    laptop_acc_cost = Retail_Accessories.objects.filter(devices__devices='Laptop')
    laptop_acc_retail_worth = Retail_Accessories.objects.filter(devices__devices='Laptop')
    laptop_acc_cost_count = Retail_Accessories.objects.filter(devices__devices='Laptop').count()
    
    tablet_acc_cost = Retail_Accessories.objects.filter(devices__devices='Tablet')
    tablet_acc_retail_cost = Retail_Accessories.objects.filter(devices__devices='Tablet')
    tablet_acc_cost_count = Retail_Accessories.objects.filter(devices__devices='Tablet').count()
    
    for i in mobile_acc:
        mobile_acc_list.append(i.cost)
    Total_mobile_acc_cost = sum(mobile_acc_list) 
    
    for i in mobile_acc_retail_worth:
        mobile_acc_retail_worth_list.append(i.retail_price)
    Total_mobile_acc_retail_worth_list = sum(mobile_acc_retail_worth_list) 
    
    for i in laptop_acc_cost:
        laptop_acc_cost_list.append(i.cost)
    total_laptop_acc_cost_list = sum(laptop_acc_cost_list) 
    
    for i in laptop_acc_retail_worth:
        laptop_acc_retail_worth_list.append(i.retail_price)
    total_laptop_acc_retail_worth_list = sum(laptop_acc_retail_worth_list) 
    
    for i in tablet_acc_cost:
        tablet_acc_cost_list.append(i.cost)
    Total_tablet_acc_cost_list = sum(tablet_acc_cost_list) 
    
    for i in tablet_acc_retail_cost:
        tablet_acc_retail_cost_list.append(i.retail_price)
    total_tablet_acc_retail_cost_list = sum(tablet_acc_retail_cost_list) 
    
    
    
    
    accessories_net_cost = Total_mobile_acc_cost + total_laptop_acc_cost_list + Total_tablet_acc_cost_list
    accessories_retail_worth = Total_mobile_acc_retail_worth_list + total_laptop_acc_retail_worth_list + total_tablet_acc_retail_cost_list
      
    total_quantity = mobile_acc_count + laptop_acc_cost_count + tablet_acc_cost_count
     
     
    context = { 'Total_mobile_acc_cost':Total_mobile_acc_cost,
               'Total_mobile_acc_retail_worth_list':Total_mobile_acc_retail_worth_list,
               'total_laptop_acc_cost_list':total_laptop_acc_cost_list,
               'total_laptop_acc_retail_worth_list':total_laptop_acc_retail_worth_list,
               'Total_tablet_acc_cost_list':Total_tablet_acc_cost_list,
               'total_tablet_acc_retail_cost_list':total_tablet_acc_retail_cost_list,
               'accessories_net_cost':accessories_net_cost,
               'accessories_retail_worth':accessories_retail_worth,
               'mobile_acc_count':mobile_acc_count,
               'laptop_acc_cost_count':laptop_acc_cost_count,
               'tablet_acc_cost_count':tablet_acc_cost_count,
               'total_quantity':total_quantity
         
     }
    return render(request,'Dashboard/Accessories_dashboard.html',context)



def parts_dashboard(request):
    
    available_list = []
    reserved_list = []
    ordered_list = []
    requested_list = []
    in_house_parts_list =[]
    
    
    parts_available = Inventories.objects.filter(part_status__p_status= 'Available')
    parts_available_count = Inventories.objects.filter(part_status__p_status= 'Available').count()
    
    parts_reserved = Inventories.objects.filter(part_status__p_status= 'Reserved')
    parts_reserved_count = Inventories.objects.filter(part_status__p_status= 'Reserved').count()
    
    parts_ordered = Ordered_parts.objects.filter(part_status__p_status= 'Ordered')
    parts_ordered_count = Ordered_parts.objects.filter(part_status__p_status= 'Ordered').count()
    

    parts_requested = Request_parts.objects.filter(part_status__p_status= 'Part Requested')
    parts_requested_count = Request_parts.objects.filter(part_status__p_status= 'Part Requested').count()
    
    
    
        
    for c in parts_available:
        available_list.append(c.cost)
    total_available = sum(available_list)
    
    for c in parts_reserved:
        reserved_list.append(c.cost)
    total_reserved = sum(reserved_list)
    
    for c in parts_ordered:
        ordered_list.append(c.requested_parts_ordered.buying_cost)
    total_ordered = sum(ordered_list)
    
    for c in parts_requested:
        requested_list.append(c.buying_cost)
    total_requested = sum(requested_list)
    
    total_worth_of_in_house_parts = total_available + total_reserved
    total_number_of_parts_in_house = parts_available_count + parts_reserved_count
     
        
        
        
        
    context = {
               
               'total_available_context':total_available,
               'total_reserved_context':total_reserved,
               'total_ordered_context':total_ordered,
               'total_requested_context':total_requested,
               'parts_available_count':parts_available_count,
               'parts_reserved_count':parts_reserved_count,
               'parts_ordered_count':parts_ordered_count,
               'parts_requested_count':parts_requested_count,
               'total_number_of_parts_in_house':total_number_of_parts_in_house,
               'total_worth_of_in_house_parts':total_worth_of_in_house_parts
            
               }
    return render(request,'Dashboard/parts_dashboard.html',context)



    

    


