
from django.shortcuts import render, redirect 
#from .models import Customer
import datetime
from django.http import HttpResponse
from Inventories.models import  *
from Jobs.models import *
from django.db.models import Q
from django.db import IntegrityError



def inventories_dashboard(request):
    return render(request,'inventories_dashboard.html') 

def Add_new_part(request):
    part = Inventories.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    device = Devices.objects.all()
    part_name = Part_name.objects.all()
    colour = Part_colour.objects.all()
    supplier = Supplier.objects.all()
    part_status = Part_status.objects.all()

    if request.method == "POST":
        device_name = request.POST.get('device_mobile')
        make_name = request.POST.get('make_name')
        model_name = request.POST.get('model_name')
        part_name = request.POST.get('part_name')
        part_colour = request.POST.get('colour_name')
        supplier_name = request.POST.get('supplier_name')
        quantity_name = request.POST.get('quantity_name')
        cost_name = request.POST.get('cost_name')   
        # part_status_name = request.POST.get('part_status_name')

        device_v = Devices.objects.get(devices=device_name)
        make_v = Make.objects.get(make=make_name)
        model_v = Model.objects.get(model=model_name)
        
        # p_status_v = Part_status.objects.get(p_status=part_status_name)
        part_name_v = Part_name.objects.get(part_name=part_name)
        part_colour_v = Part_colour.objects.get(colour=part_colour)
        supplier_v = Supplier.objects.get(supplier=supplier_name)
        
        for i in range(int(quantity_name)):#this for loop tells form to execute depends on quantity numbers .
        

            data = Inventories( devices = device_v,
                                make = make_v,
                                model = model_v,
                                part_name = part_name_v,
                                part_colour = part_colour_v,
                                supplier = supplier_v,
                                quantity = quantity_name,
                                cost = cost_name,
                                # part_status=p_status_v,
                                created_by = request.user,
                                created_date = datetime.datetime.now() 
                                )
            data.save()
            
        return redirect('part_added',id=data.id)

        

    
    context = {'part_context':part,
                'make_context':make,
                'model_context':model,
                'device_context':device,
                'part_name_context':part_name,
                'colour_context':colour,
                'supplier_context':supplier,
                'part_status_context':part_status


                }
    return render(request,'Add_new_part.html',context)

def part_added(request,id):
    part = Inventories.objects.get(id=id)
    context = {'part_context':part}
    return render(request,'part_added.html',context)


def part_detail(request,id):
    part = Inventories.objects.get(id=id)
    context = {'part_detail_context':part}
    return render(request,'part_detail.html',context)



def request_part(request,id):
    jobs = Jobs.objects.get(id=id)
    part_order = Inventories.objects.all()
    
    make = Make.objects.all()
    model = Model.objects.all()
    device = Devices.objects.all()
    part_name = Part_name.objects.all()
    colour = Part_colour.objects.all()
    supplier = Supplier.objects.all()
    part_status = Part_status.objects.all()

    if request.method == "POST":
        device_name = request.POST.get('device_name')
        make_name = request.POST.get('make_name')
        model_name = request.POST.get('model_name')
        part_name = request.POST.get('part_name')
        part_colour = request.POST.get('colour_name')
        supplier_name = request.POST.get('supplier_name')
        quantity_name = request.POST.get('quantity_name')
        buying_cost_name = request.POST.get('buying_cost_name')   
        part_des_name = request.POST.get('part_des_name')
        part_status_name = request.POST.get('part_status_name')
        
        part_status_checkbox_name = request.POST.get('part_status_checkbox_name')
        part_status_checkbox_name == part_status_name
        
        
        
        

        device_v = Devices.objects.get(devices=device_name)
        make_v = Make.objects.get(make=make_name)
        model_v = Model.objects.get(model=model_name)
        part_name_v = Part_name.objects.get(part_name=part_name)
        part_colour_v = Part_colour.objects.get(colour=part_colour)
        supplier_v = Supplier.objects.get(supplier=supplier_name)
        part_status_v = Part_status.objects.get(p_status=part_status_name)
        
        
        
        for i in range(int(quantity_name)): #this for loop tells form to execute depends on quantity numbers .
            data = Request_parts( job = jobs,
                                devices = device_v,
                                make = make_v,
                                model = model_v,
                                part_name = part_name_v,
                                part_colour = part_colour_v,
                                supplier = supplier_v,
                                quantity = quantity_name,
                                buying_cost = buying_cost_name,
                                part_description = part_des_name,
                                part_status=part_status_v,
                                
                                created_by = request.user,
                                created_date = datetime.datetime.now() 
                                )
            
            data.save()
          
            return redirect("all_requested_parts")
        # return redirect('')   

        

    context = {'part_order_context':part_order,
                'jobs_context':jobs,
                
                'make_context':make,
                'model_context':model,
                'device_context':device,
                'part_name_context':part_name,
                'colour_context':colour,
                'supplier_context':supplier,
                'part_status_context':part_status
 }
    return render(request,'request_part.html',context)




def all_requested_parts(request):
    parts_ordered = Request_parts.objects.all()
    context = {'parts_ordered_context':parts_ordered}
    return render(request,'all_requested_parts.html',context)



def ordered_parts(request):
    parts_ordered = Ordered_parts.objects.all()
    requested_parts = Request_parts.objects.all()
    context = {'waiting_for_parts_context':parts_ordered, 'requested_parts_context':requested_parts}
    return render(request,'ordered_parts.html',context)








def requested_part_detail(request,id):
    parts_requested = Request_parts.objects.get(id=id)
    
    # device = Devices.objects.all()
    # make = Make.objects.all()
    # model = Model.objects.all()
    # device = Devices.objects.all()
    # part_name = Part_name.objects.all()
    # colour = Part_colour.objects.all()
    # supplier = Supplier.objects.all()
    part_status = Part_status.objects.all()
    
    if request.method == "POST":
        
        part_status_name = request.POST.get('part_status_name1')
        eta_name = request.POST.get('eta')
        part_order_comments_name = request.POST.get('part_order_comments')
        
        part_status_v = Part_status.objects.get(p_status=part_status_name)
        
        
        data = Ordered_parts(
                    part_status = part_status_v,
                    
                    eta = eta_name,
                    comments = part_order_comments_name,
                    created_date = datetime.datetime.now(),
                    created_by = request.user

                    )
        
                 
        data.save()
        return redirect('all_requested_parts') 
        
    
    
    context = {'parts_requested_context':parts_requested,
                'part_status_context':part_status}
    return render(request,'requested_part_detail.html',context)


def update_requested_part(request,id):# once part ordered this transfer from requested part to ordered parts.
    if request.method == "POST":
        part_status_name = request.POST.get('part_status_name1')
        eta_name = request.POST.get('eta')
        part_order_comments_name = request.POST.get('part_order_comments')
        requested_part = Request_parts.objects.get(id=id)
        
        part_status = Part_status.objects.get(p_status=part_status_name)
        
        data = Ordered_parts(
                    requested_parts_ordered = requested_part,
                    part_status = part_status,
                    eta = eta_name,
                    comments = part_order_comments_name,
                    created_date = datetime.datetime.now(),
                    created_by = request.user
        )
        data.save()
        
        requested_part = Request_parts.objects.filter(id=id).update(part_status=part_status)
        return redirect('all_requested_parts')
        
    return redirect('all_requested_parts')


def ordered_part_detail(request,id):
    ordered_part = Ordered_parts.objects.get(id=id)
    part_status = Part_status.objects.all()
    # context = {'ordered_part_context':ordered_part}  parts_requested_context
    context = {'parts_requested_context':ordered_part,
               'part_status_context':part_status}  
    return render(request,'ordered_part_detail.html',context) 






def ordered_parts_arrived(request,id):
    ordered_part = Ordered_parts.objects.get(id=id)
    part_status = Part_status.objects.all()
    device = Devices.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    device = Devices.objects.all()
    part_name = Part_name.objects.all()
    colour = Part_colour.objects.all()
    supplier = Supplier.objects.all()
    
    if request.method == "POST":
        
        device_name = request.POST.get('device_name')
        make_name = request.POST.get('make_name')
        model_name = request.POST.get('model_name')
        part_name = request.POST.get('part_name')
        part_colour = request.POST.get('color_name')
        supplier_name = request.POST.get('supplier_name')
        quantity_name = request.POST.get('quantity_name')
        cost_name = request.POST.get('cost_name')   
        part_status_name = request.POST.get('part_status_arrived_name')
        
        device_v = Devices.objects.get(devices=device_name)
        make_v = Make.objects.get(make=make_name)
        model_v = Model.objects.get(model=model_name)
        part_name_v = Part_name.objects.get(part_name=part_name)
        part_colour_v = Part_colour.objects.get(colour=part_colour)
        supplier_v = Supplier.objects.get(supplier=supplier_name)
        p_status_v = Part_status.objects.get(p_status=part_status_name)
        
        data = Inventories(     devices = device_v,
                                make = make_v,
                                model = model_v,
                                part_name = part_name_v,
                                part_colour = part_colour_v,
                                supplier = supplier_v,
                                quantity = quantity_name,
                                cost = cost_name,
                                part_status=p_status_v,
                                created_date = datetime.datetime.now(),
                                created_by = request.user
                                )
        data.save()
        order_part = Ordered_parts.objects.filter(id=id).update(part_status=p_status_v)
        # order_part = Ordered_parts.objects.filter(id=id)
        
        return redirect('ordered_parts')
    context ={ 
                'make_context':make,
                'model_context':model,
                'device_context':device,
                'part_name_context':part_name,
                'colour_context':colour,
                'supplier_context':supplier,
                'part_status_context':part_status
               }
    
    
    return render(request,'ordered_part_detail.html',context)
     
    

# def ordered_parts_arrived(request):
#     ordered_part = Ordered_parts.objects.get(id=id)
#     part_status = Part_status.objects.all()
    
#     if request.method == "POST":
#         device_name = request.POST.get('device_name')
#         make_name = request.POST.get('make_name')
#         model_name = request.POST.get('model_name')
#         part_name = request.POST.get('part_name')
#         part_colour = request.POST.get('color_name')
#         supplier_name = request.POST.get('supplier_name')
#         quantity_name = request.POST.get('quantity_name')
#         cost_name = request.POST.get('cost_name')   
#         part_status_name = request.POST.get('part_status_arrived_name')
        
#         device_v = Devices.objects.get(devices=device_name)
#         make_v = Make.objects.get(make=make_name)
#         model_v = Model.objects.get(model=model_name)
#         part_name_v = Part_name.objects.get(part_name=part_name)
#         part_colour_v = Part_colour.objects.get(colour=part_colour)
#         supplier_v = Supplier.objects.get(supplier=supplier_name)
#         p_status_v = Part_status.objects.get(p_status=part_status_name)
        
#         data = Inventories(     devices = device_v,
#                                 make = make_v,
#                                 model = model_v,
#                                 part_name = part_name_v,
#                                 part_colour = part_colour_v,
#                                 supplier = supplier_v,
#                                 quantity = quantity_name,
#                                 cost = cost_name,
#                                 part_status=p_status_v,
#                                 created_date = datetime.datetime.now(),
#                                 created_by = request.user
#                                 )
#         data.save()
        
#         return redirect('part_added',id=data.id)
     
#     context = {'parts_requested_context':ordered_part,
#                'part_status_context':part_status}
    
#     return render(request,'ordered_parts_arrived.html')





def update_part(request,id):
    part_u = Inventories.objects.get(id=id)
    part_device_p = Devices.objects.all()
    part_make_p = Make.objects.all()
    part_model_p = Model.objects.all()
    part_name_p = Part_name.objects.all()
    part_color_p = Part_colour.objects.all()
    part_supplier_p = Supplier.objects.all()
    

    if request.method == "POST":
        
        part_make_name = request.POST.get('part_make_name')
        part_model_name = request.POST.get('part_model_name')
        part_part_name = request.POST.get('part_part_name')
        part_colour_name = request.POST.get('part_colour_name')
        part_supplier_name = request.POST.get('part_supplier_name')
        part_cost_name = request.POST.get('part_cost_name')
            
        #make_v = Inventories.objects.get(make__make=part_make_name)
        data = Inventories(cost=part_cost_name)
        data.save()




    context = {'part_update_context':part_u}
    return render(request,'update_part.html')    



def search_parts(request):
    part_s = Inventories.objects.all()
    context = {'all_parts_context':part_s}
    return render(request,'search_parts.html',context)







# def search_parts(request):
#     if request.method =="POST":
#         searched = request.POST['searched']
#         lookup = (Q(id__icontains=searched))
        
#         result = Inventories.objects.filter(lookup)
    
#         context = {'all_parts_context':result, 'searched':searched}
#         return render(request,'search_parts.html', context )

#     else:
#         return render(request,'search_parts.html',context )






