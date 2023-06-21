from django.shortcuts import render, redirect
from customer.models import *
from .models import *
from django.http import HttpResponse
import random
import datetime
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q
from Retail.models import  *
from Inventories.models import  *



# function
# function
def add_job(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        device = Devices.objects.all()
        make = Make.objects.all()
        model = Model.objects.all()
        fault = Fault.objects.all()
        accessories = Accessories.objects.all()
        sale_item = Sale_item.objects.all()
        network = Network.objects.all()
        job_status = Job_status.objects.all()
        img = Pictures.objects.all()
        #payment = payment_status.objects.all()  'payment_status_context':payment,  
        context = {'customers':customers,
                    'device_context':device, 
                    'make_context':make, 
                    'model_context':model,
                    'fault_context':fault ,
                    'accessories_context':accessories, 
                    'sale_item_context':sale_item , 
                    'network_context':network,
                    'job_status_context': job_status

                    }
        return render(request,'add_job.html',context)
    
    if request.method == "POST":
    
        #bring all front end inputs to view so we can connect them with models.
        customer1 = request.POST.get('customer')#customer in brackets comes from html Name = customer
        device = request.POST.get('device_mobile')
        make = request.POST.get('make')
        model = request.POST.get('model')
        imei = request.POST.get('imei')
        fault = request.POST.get('faults')
        description = request.POST.get('description')
        accessories = request.POST.get('accessories')
        sale_item = request.POST.get('sale_item')
        passcode = request.POST.get('passcode')
        network = request.POST.get('network')
        cost = request.POST.get('cost')
        job_status = request.POST.get('job_status')
        eta = request.POST.get('eta')
        payment = request.POST.get('payment_status')
        try:
            img_name = request.FILES['image_name']
        except Exception:
            img_name = ""

        customer_id = Customer.objects.get(id=customer1)# customer_id is new variable than Customer class and in brackets id comes from html value="id" and customer is variable in line 35.
        device_id = Devices.objects.get(devices=device)
        make_id = Make.objects.get(make=make)
        model_id = Model.objects.get(model=model)
        fault_id = Fault.objects.get(fault=fault)
        acessories_id = Accessories.objects.get(accessories=accessories)
        sale_item_id = Sale_item.objects.get(sale_item=sale_item)
        network_id = Network.objects.get(network=network)
        job_status_id = Job_status.objects.get(job_status=job_status)

        # vat = cost * 20 /100
        # total_cost = vat +  cost

        data = Jobs(customer=customer_id,#customer is column or field from classes and customer_id from line 51.
                    device=device_id,
                    make=make_id,
                    model=model_id,
                    fault=fault_id,
                    description=description,
                    imei=imei,
                    accessories=acessories_id,
                    sale_item=sale_item_id,
                    passcode=passcode,
                    network=network_id,
                    cost=cost,
                    # vat = vat,
                    # Total_cost = total_cost,
                    job_status=job_status_id,
                    collection_time=eta,
                    payment_status=payment,
                    created_by = request.user,
                    created_date = datetime.datetime.now() )

        data.save() 
        job_data =  Jobs.objects.get(id=data.id)          
        img_v = Pictures(device_images=job_data,
                         image=img_name,
                         captured_at = datetime.datetime.now(),
                         captured_by = request.user
                         )
        img_v.save()
        
        reciept = Reciepts(reciept=job_data)
        reciept.save()

        return redirect('reciept',data.id) 



def add_direct_job(request,id):
    if request.method == "GET":
        customers = Customer.objects.get(id=id)
        device = Devices.objects.all()
        make = Make.objects.all()
        model = Model.objects.all()
        fault = Fault.objects.all()
        accessories = Accessories.objects.all()
        sale_item = Sale_item.objects.all()
        network = Network.objects.all()
        job_status = Job_status.objects.all()
        #payment = payment_status.objects.all()  'payment_status_context':payment,  
        context = {'customers':customers,
                    'device_context':device, 
                    'make_context':make, 
                    'model_context':model,
                    'fault_context':fault ,
                    'accessories_context':accessories, 
                    'sale_item_context':sale_item , 
                    'network_context':network,
                    'job_status_context': job_status
                    }
        return render(request,'add_direct_job.html',context)
    
    if request.method == "POST":
    
        #bring all front end inputs to view so we can connect them with models.
        customer1 = request.POST.get('customer')#customer in brackets comes from html Name = customer
        device = request.POST.get('device_mobile')
        make = request.POST.get('make')
        model = request.POST.get('model')
        imei = request.POST.get('imei')
        fault = request.POST.get('faults')
        description = request.POST.get('description')
        accessories = request.POST.get('accessories')
        sale_item = request.POST.get('sale_item')
        passcode = request.POST.get('passcode')
        network = request.POST.get('network')
        cost = request.POST.get('cost')
        job_status = request.POST.get('job_status')
        eta = request.POST.get('eta')
        payment = request.POST.get('payment_status')

        customer_id = Customer.objects.get(id=customer1)# customer_id is new variable than Customer class and in brackets id comes from html value="id" and customer is variable in line 108.
        device_id = Devices.objects.get(devices=device)
        make_id = Make.objects.get(make=make)
        model_id = Model.objects.get(model=model)
        fault_id = Fault.objects.get(fault=fault)
        acessories_id = Accessories.objects.get(accessories=accessories)
        sale_item_id = Sale_item.objects.get(sale_item=sale_item)
        network_id = Network.objects.get(network=network)
        job_status_id = Job_status.objects.get(job_status=job_status)
        job_created_date = datetime.datetime.now() #craeted new variable to store current time ( datetime.datetime.now())
        job_created_by = request.user

        # vat = (int(cost * 20 /100))
        # total_cost = (int(vat +  cost))
        # vat = ((cost) * (20) / 100)
        # total_cost = ((cost) + (vat))

        data = Jobs(customer=customer_id,#customer is column or field from classes and customer_id from line 51.
                    device=device_id,
                    make=make_id,
                    model=model_id,
                    fault=fault_id,
                    description=description,
                    imei=imei,
                    accessories=acessories_id,
                    sale_item=sale_item_id,
                    passcode=passcode,
                    network=network_id,
                    
                    cost=cost,
                    # vat = vat,
                    # Total_cost = total_cost,
                    job_status=job_status_id,
                    collection_time=eta,
                    payment_status=payment,
                    created_date= job_created_date,
                    created_by=job_created_by )
        
               
        data.save() 
        job_data =  Jobs.objects.get(id=data.id)          
        reciept = Reciepts(reciept=job_data)
        reciept.save()           
        job = Jobs.objects.get(id=data.id)#here we fetch last job added and show to user
        context = {'job_created_context':job}            
        return render(request, 'job_created.html', context)
    
            
             
    

def dashboard(request):
    retail = Customer.objects.filter(client_type = 'retail').count()
    corporate = Customer.objects.filter(client_type = 'corporate').count()
    context = {'retail_count_context': retail,
               'corporate_count_context':corporate}
    return render(request,'dashboard.html', context)



def search_job(request):
    return render(request,'search_job.html')
    

def search_job(request):
    
    if request.method =="POST":
        
        searched = request.POST['searched']
        lookup = (Q(id__contains=searched)
        |Q(make__make__icontains=searched)
        |Q(model__model__icontains=searched)
        |Q(imei__icontains=searched)
        |Q(created_date__icontains=searched)
        |Q(job_status__job_status__icontains=searched))
        
        result = Jobs.objects.filter(lookup)
        context = {'result_context':result, 'searched':searched}
        return render(request,'search_job.html',context)
    else:
        return render(request,'search_job.html' )






# def job_detail_page(request,id):
#     detail_page = Jobs.objects.get(id=id)
#     c_cart = Customer_cart.objects.filter(c_cart=detail_page).first()#when we mentione first or last with filter and dont add for loop it wont give error as only one parameter called.
    
#     job_update_table = Job_update.objects.filter(job_update=id)
#     now = datetime.datetime.now()
#     Fprint = Fingerprints.objects.filter(job_fprint=id)# job_fprint comes from models as its related to that specific job
#     update_finger_print= Fingerprints(user_fprint=request.user, date_time_fprint=now.strftime("%m/%d/%Y, %H:%M:%S"), job_fprint=detail_page)
#     update_finger_print.save()

#     job_complete_v =  Complete_job.objects.filter(c_job=id).last()
#     context = {'detail_page_context':detail_page, 'job_update_table_context':job_update_table,
#                  'Fprint_context':Fprint , 
#                  'job_complete_v_context':job_complete_v, 
#                  'c_cart_context':c_cart}
#     return render(request,'job_detail_page.html',context)


def job_detail_page(request,id):
    detail_page = Jobs.objects.get(id=id)
    part_requested = Request_parts.objects.filter(job=detail_page)
    part_ordered = Ordered_parts.objects.filter(requested_parts_ordered=id)
    #c_cart = Customer_cart.objects.filter(c_cart=detail_page).first()#when we mentione first or last with filter and dont add for loop it wont give error as only one parameter called.
    job_d = Delivered.objects.filter(job_deliver=detail_page).first()
    job_update_table = Job_update.objects.filter(job_update=id)
    now = datetime.datetime.now()
    Fprint = Fingerprints.objects.filter(job_fprint=id)# job_fprint comes from models as its related to that specific job
    update_finger_print= Fingerprints(user_fprint=request.user, date_time_fprint=now.strftime("%m/%d/%Y, %H:%M:%S"), job_fprint=detail_page)
    update_finger_print.save()

    job_complete_v =  Complete_job.objects.filter(c_job=id).last()
    context = {'detail_page_context':detail_page, 
               'job_update_table_context':job_update_table,
                 'Fprint_context':Fprint , 
                 'job_complete_v_context':job_complete_v, 
                 'job_d_context':job_d,
                 'part_requested_context':part_requested,
                 'part_ordered_context':part_ordered
                }
    return render(request,'job_detail_page.html',context)



def job_update_page(request,id):
    job_update = Jobs.objects.get(id=id)
    customers = Customer.objects.filter(id=id)
    device = Devices.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    fault = Fault.objects.all()
    accessories = Accessories.objects.all()
    sale_item = Sale_item.objects.all()
    network = Network.objects.all()
    job_status = Job_status.objects.all()
    #payment = payment_status.objects.all()  'payment_status_context':payment,  
        
    if request.method == "POST":
        #customer1 = request.POST.get('customer')#customer in brackets comes from html Name = customer
        #device = request.POST.get('device_mobile')
        #make = request.POST.get('make')
        #model = request.POST.get('model')
        imei = request.POST.get('imei_update')
        fault = request.POST.get('fault_update')
        description = request.POST.get('description_update')
        accessories = request.POST.get('accessories_update')
        sale_item = request.POST.get('sale_item_update')
        passcode = request.POST.get('passcode_update')
        network = request.POST.get('network_update')
        cost = request.POST.get('cost_update')
        job_status = request.POST.get('job_status_update')
        eta = request.POST.get('eta_update')
        payment = request.POST.get('payment_status_update')

        #customer_id = Customer.objects.get(id=customer1)# customer_id is new variable than Customer class and in brackets id comes from html value="id" and customer is variable in line 108.
        #device_id = Devices.objects.get(devices=device)
        #make_id = Make.objects.get(make=make)
        #model_id = Model.objects.get(model=model)
        fault_id = Fault.objects.get(fault=fault)
        acessories_id = Accessories.objects.get(accessories=accessories)
        sale_item_id = Sale_item.objects.get(sale_item=sale_item)
        network_id = Network.objects.get(network=network)
        job_status_id = Job_status.objects.get(job_status=job_status)
        job_created_date = datetime.datetime.now() #craeted new variable to store current time ( datetime.datetime.now())
        job_created_by = request.user
        job_update_data = Jobs.objects.get(id=id)

        data = Job_update(
                    job_update = job_update_data,
                    fault_update=fault_id,
                    description_update=description,
                    imei_update=imei,
                    accessories_update=acessories_id,
                    sale_item_update=sale_item_id,
                    passcode_update=passcode,
                    network_update=network_id,
                    cost_update=cost,
                    job_status_update=job_status_id,
                    collection_time_update=eta,
                    payment_status_update=payment,
                    updated_on= job_created_date,
                    updated_by=job_created_by )
        
               
        data.save()
        # job_cost = Jobs.objects.filter(id=id).update(cost=cost,
        #                                              payment_status= payment,
        #                                              job_status= job_status_id)
        return redirect('job_detail_page',id=id)
    context = {'customers':customers,
                    'device_context':device, 
                    'make_context':make, 
                    'model_context':model,
                    'fault_context':fault ,
                    'accessories_context':accessories, 
                    'sale_item_context':sale_item , 
                    'network_context':network,
                    'job_status_context': job_status,
                    'job_update_context':job_update,
                    
                    
                    }
    
    return render(request,'job_update_page.html', context)





def reciept(request,id):
    reciept = Reciepts.objects.filter(reciept=id).last()
    context = {'reciept':reciept}
    return render(request,'reciept.html',context)


def send_email_page(request,id, reciept_id):
    customer = Customer.objects.get(id=id)
    reciept = Reciepts.objects.filter(id=reciept_id)
    context = {'reciept':reciept}
    

    subject = 'Please find Reciept for your device...'
    html_message = render_to_string('reciept_email.html', context)
    plain_message = strip_tags(html_message)
    from_email = 'learningdjango1@gmail.com'
    to = customer.email

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    return render(request,'send_email_page.html')




def contact_by_email(request,id,job_id):
    e = Jobs.objects.filter(customer=id)
    j_id = Jobs.objects.get(id=job_id)
    if request.method == "POST":
        subject = request.POST.get("email_subject_name")
        message = request.POST.get("email_area_name")
        send_mail(
            subject,
            message,
            'learningdjango1@gmail.com',
            [j_id.customer.email],
            fail_silently=False,
)



    context = {'e_context':e, 'j_id_context':j_id, }
    return render(request,'contact_by_email.html', context )



def complete(request,id):
    complete_job = Jobs.objects.get(id=id)
    parts = Inventories.objects.filter(alocated=False)
    if request.method == "POST":
        complete_job_name = request.POST.get('Complete_area_name')
        cost_com = request.POST.get('cost_com_name')
        payment_status_com_name = request.POST.get('payment_status_com_name')  
        select_part_name = request.POST.get('select_part_name')

        job_status = Job_status.objects.get(id=3)
        inventories = Inventories.objects.filter(id=select_part_name).update(alocated=True,job=complete_job )
        data = Complete_job(c_job=complete_job,
                             complete_update = complete_job_name,
                             checked=True, 
                             completed_by=request.user,
                             cost_com=cost_com,
                             payment_status_com = payment_status_com_name,
                             completed_on=datetime.datetime.now())
        data.save()
        job_cost = Jobs.objects.filter(id=id).update(cost=cost_com, job_status = job_status ,completed=True )
        
        return redirect('job_detail_page',id)
    context = {'complete_job_context':complete_job, 'parts_context':parts}
    return render(request,'complete.html',context)









def job_deliver(request):
    return render(request,'job_deliver.html')



def job_rebook(request,id):
    j_rebook = Jobs.objects.get(id=id)
    faults = Fault.objects.all()
    job_status_v = Job_status.objects.all()
    if request.method == "POST":
        imei_r = request.POST.get("imei")
        fault_r = request.POST.get("faults")
        description_r = request.POST.get("description")
        passcode_r = request.POST.get("passcode")
        cost_r = request.POST.get("cost")
        eta_r = request.POST.get("eta")
        job_status_r = request.POST.get("job_status")
        payment_r = request.POST.get("payment_status")
        

        fault_c = Fault.objects.get(fault=fault_r)
        job_status_c = Job_status.objects.get(job_status=job_status_r)

        data = Job_rebook(j_rebook=j_rebook,
                            cost_r= cost_r,
                            eta_r =  eta_r,
                            fault_r=  fault_c,
                            description_r = description_r,
                            imei_r =  imei_r,

                            rebooked_on = datetime.datetime.now(),
                            rebooked_by = request.user   )
                                            
        data.save()

        job_data = Jobs(customer = j_rebook.customer,
                            device = j_rebook.device,
                            make =  j_rebook.make,
                            model = j_rebook.model,
                            cost= cost_r,
                            collection_time =  eta_r,
                            fault=  fault_c,
                            description = description_r,
                            imei =  imei_r,
                            payment_status = j_rebook.payment_status,
                            job_status = job_status_c,
                            created_date = datetime.datetime.now(),
                            created_by = request.user )
        job_data.save()
        data_v = Jobs.objects.get(id=job_data.id)
        reciept = Reciepts(reciept=data_v)
        reciept.save()
        return redirect ('reciept',data_v)
        


    context = {'j_rebook_context':j_rebook,"fault_context":faults }
    return render(request,'job_rebook.html',context)



def send_text_page(request):
    return render(request,'send_text_page.html') 


def images(request,id):
    img = Pictures.objects.filter(device_images=id)
    if request.method == "POST":
        img_name = request.FILES['image_name']  
        comments_name = request.POST.get("comments_name")

    
        img_data =  Jobs.objects.get(id=id)          
        img_v = Pictures(device_images=img_data, 
                            image=img_name, 
                            captured_at = datetime.datetime.now(),
                            captured_by = request.user,
                            comments = comments_name
                            )
        img_v.save()
        return redirect('images',id=id)
        


    context = {'img_context':img}
    return render(request,'images.html',context)













def pending_jobs(request):
    today = datetime.datetime.now()
    pending_jobs = Jobs.objects.filter(device__devices='Mobile').filter(job_status__job_status='pending')
    laptop_pending_jobs = Jobs.objects.filter(device__devices='Laptop').filter(job_status__job_status='pending')
    tablets_pending_jobs = Jobs.objects.filter(device__devices='Tablet').filter(job_status__job_status='pending')
    other_pending_jobs = Jobs.objects.filter(device__devices='Others').filter(job_status__job_status='pending')
    
    context = {
        'pending_jobs_context':pending_jobs,
        'laptop_pending_jobs_context':laptop_pending_jobs,
        'tablets_pending_jobs':tablets_pending_jobs,
        'other_pending_jobs':other_pending_jobs
        
    }
    return render(request,'pending_jobs.html',context)














def waiting_for_parts_jobs(request):
    
    waiting_for_parts_jobs = Jobs.objects.filter(device__devices='Mobile').filter(job_status__job_status='waiting for parts')
    laptop_waiting_for_parts_jobs = Jobs.objects.filter(device__devices='Laptop').filter(job_status__job_status='waiting for parts')
    tablet_waiting_for_parts_jobs = Jobs.objects.filter(device__devices='Tablet').filter(job_status__job_status='waiting for parts')
    other_waiting_for_parts_jobs = Jobs.objects.filter(device__devices='Others').filter(job_status__job_status='waiting for parts')
    context = { 
                'waiting_for_parts_jobs_context':waiting_for_parts_jobs,
                'laptop_waiting_for_parts_jobs':laptop_waiting_for_parts_jobs,
                'tablet_waiting_for_parts_jobs':tablet_waiting_for_parts_jobs,
                'other_waiting_for_parts_jobs':other_waiting_for_parts_jobs
                }
    return render(request,'waiting_for_parts_jobs.html',context)
    
    

def waiting_approval_jobs(request):
    
    
    waiting_approval_jobs = Jobs.objects.filter(device__devices='Mobile').filter(job_status__job_status='Waiting for approval')
    laptop_waiting_approval_jobs = Jobs.objects.filter(device__devices='Laptop').filter(job_status__job_status='Waiting for approval')
    tablet_waiting_approval_jobs = Jobs.objects.filter(device__devices='Tablet').filter(job_status__job_status='Waiting for approval')
    other_waiting_for_approval_jobs = Jobs.objects.filter(device__devices='Others').filter(job_status__job_status='Waiting for approval')
    
    context = { 
                'waiting_approval_jobs_context':waiting_approval_jobs,
                'laptop_waiting_approval_jobs':laptop_waiting_approval_jobs ,
                'tablet_waiting_approval_jobs': tablet_waiting_approval_jobs,
                'other_waiting_for_approval_jobs':other_waiting_for_approval_jobs
                }
    return render(request,'waiting_approval_jobs.html',context)



def completed_jobs(request):
    
    completed_jobs = Jobs.objects.filter(device__devices='Mobile').filter(job_status__job_status='Completed')
    laptop_completed_jobs = Jobs.objects.filter(device__devices='Laptop').filter(job_status__job_status='Completed')
    tablet_completed_jobs = Jobs.objects.filter(device__devices='Tablet').filter(job_status__job_status='Completed')
    other_completed_jobs = Jobs.objects.filter(device__devices='Others').filter(job_status__job_status='Completed')
    
    
    context = { 
                'completed_jobs_context':completed_jobs,
                'laptop_completed_jobs': laptop_completed_jobs,
                'tablet_completed_jobs': tablet_completed_jobs,
                'other_completed_jobs':other_completed_jobs
                }
    return render(request,'completed_jobs.html',context)

    
     
        
    





