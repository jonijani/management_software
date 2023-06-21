from django.shortcuts import render ,redirect
from Jobs.models import *
from Retail.models import *
from Jobs.models import *
from .models import *
from Accessories.models import *
from django.db.models import Q


# def add_sale(request):
#     return render(request,'add_sale.html')


def add_sale(request):
    
    if request.method =="POST":
        
        searched = request.POST['searched']

        lookup =    (Q(id__contains=searched)
                    
                    )
       
    
        result_acce = Retail_Accessories.objects.filter(lookup)

        context = {'result_acce_context':result_acce}
        return render(request,'add_sale.html',context)
    else:
        return render(request,'add_sale.html')





def get_job(request):
    
    if request.method =="POST":
        
        searched = request.POST['searched']
        

        lookup_job =    (Q(id__contains=searched)
                    
                    )
        
        
        result_job = Jobs.objects.filter(lookup_job)

        context = { 'result_job_context':result_job}
        return render(request,'add_sale.html',context)
    else:
        return render(request,'add_sale.html')








def retail_sale_page(request,id):
    j_deliver = Jobs.objects.get(id=id)
    

        

    if request.method == 'POST':
        cost_name = request.POST.get("cost_name")
        data = Customer_cart(c_cart=j_deliver, deliver_cost=cost_name, sale_person=request.user, date=datetime.datetime.now())
        data.save()
        
        customer_cart = Customer_cart.objects.filter(id=data.id).first()
        
        return redirect('customer_cart',customer_cart.id)
    
    context = {'j_deliver_context':j_deliver,
               
               }

    return render(request,'retail_sale_page.html',context)










def customer_cart(request,id):
    cart = Customer_cart.objects.filter(id=id)
    payment_type = Payment_type.objects.all()
    if request.method == "POST":
        updated_cost_name = request.POST.get("updated_cost_name")
        
        payment_type_name = request.POST.get("payment_type_name")
        delivery_comments_name_v = request.POST.get("delivery_comments_name")

        payment_tpye_v = Payment_type.objects.get(id=payment_type_name)#fetch payment type and id = front end ( whats selecetd from user)
        
        temp = Customer_cart.objects.get(id=id)
         
        # temp.c_cart.job_status= Job_status.objects.get(job_status='Delivered')
        job = temp.c_cart.id# ??
        jobs = Jobs.objects.filter(id=job).update(job_status= Job_status.objects.get(job_status='Delivered'))
        job = temp.c_cart# ??
        f_reciept = Reciepts(reciept=job)
        f_reciept.save()
        reciept_filter = Reciepts.objects.get(id=f_reciept.id)
        cart_save = Customer_cart.objects.filter(id=id).update(payment_type=payment_tpye_v,
                                                            reciept=f_reciept, 
                                                            deliver_cost=updated_cost_name,
                                                            delivery_comments = delivery_comments_name_v,
                                                            
                                                     )
        job_save = Delivered(job_deliver=job, 
                                delivered_on=datetime.datetime.now(),
                                delivered_by=request.user,
                                device_deliver=temp.c_cart.device,
                                make_deliver =  temp.c_cart.make,
                                model_deliver =  temp.c_cart.model,
                                fault_deliver =  temp.c_cart.fault,
                                imei_deliver =  temp.c_cart.imei,
                                cost_deliver =  temp.c_cart.cost,
                                # payment_status_deliver=cart_save.payment_type,
                                delivery_comments = delivery_comments_name_v,
                                delivered=True
                            )
        job_save.save() 

        save_to_daily_sale = Daily_sale(job_deliver=job, 
                                date=datetime.datetime.now(),
                                sale_person=request.user,
                                device_deliver=temp.c_cart.device,
                                make_deliver =  temp.c_cart.make,
                                model_deliver =  temp.c_cart.model,
                                fault_deliver =  temp.c_cart.fault,
                                imei_deliver =  temp.c_cart.imei,
                                cost_deliver =  temp.c_cart.cost,
                                payment_type_daily_sale=payment_tpye_v,
                                reciept_daily_sale=reciept_filter,
                                delivery_comments = delivery_comments_name_v,
                                delivered=True
                            )
        save_to_daily_sale.save() 


        return redirect('reciept',job)

    context = {'cart_context':cart,"payment_type_context": payment_type}
    return render(request,'customer_cart.html',context)



######################################

# def daily_sale_report(request):
#     d_jobs = Daily_sale.objects.all()
    
#     if request.method == "POST":
#         date = request.POST.get('date_name')
#         d_jobs = Daily_sale.objects.filter(date__date=date)
        
#     context = {'d_jobs_context':d_jobs}


#     return render(request,'daily_sale_report.html',context) 't_context':t
######################################

from django.db.models import Sum

def daily_sale_report(request):
    # date = datetime.date.today()
    date = datetime.datetime.now()
    
    jobs_list_total = []
    acc_list_total = []
    d_jobs_payment_type_list = []
    d_jobs_payment_type_card_list = []
    d_jobs_payment_type_amax_list = []
    d_jobs_payment_type_amax_izettle_revive_list = []
    d_jobs_payment_type_amax_izettle_star_list = []
    total_jobs_acc_amax_list = []
    d_jobs_payment_cash_acc_list = []
    d_jobs_payment_type_card_acc_list = []
    sold_acc_irevive_list = []
    sold_acc_istar_list = []
    
    
    if request.method == "POST":
        date = request.POST.get('date_name')
        d_jobs = Daily_sale.objects.filter(date__date=date)
        python_date = date
        
        sold_acc_daily_sale = Sold_acc.objects.filter(date__date=date)
        # sold_acc_count = Sold_acc.objects.filter(date__date=date, payment_type='Cash').count()
        #t = Daily_sale.objects.filter(date__date=date).aggregate(Sum('cost_deliver'))   
        d_jobs_cash_count = Daily_sale.objects.filter(date__date=date, payment_type_daily_sale__payment = 'Cash').count()
        d_jobs_payment_type = Daily_sale.objects.filter(date__date=date,payment_type_daily_sale__payment = 'Cash')
        d_jobs_payment_cash_acc = Sold_acc.objects.filter(date__date=date,payment_type__payment = 'Cash')
        
        d_jobs_payment_type_card = Daily_sale.objects.filter(date__date=date,payment_type_daily_sale__payment = 'Card')
        d_jobs_payment_type_card_acc = Sold_acc.objects.filter(date__date=date,payment_type__payment =  'Card')
        
        d_jobs_payment_type_amax = Daily_sale.objects.filter(date__date=date,payment_type_daily_sale__payment = 'Amax')
        d_jobs_payment_type_amax_acc = Sold_acc.objects.filter(date__date=date,payment_type__payment = 'Amax')
        
        d_jobs_payment_type_irevive = Daily_sale.objects.filter(date__date=date,payment_type_daily_sale__payment = 'izettle Revive')
        sold_acc_irevive = Sold_acc.objects.filter(date__date=date,payment_type__payment= 'izettle Revive')
        
        d_jobs_payment_type_istar = Daily_sale.objects.filter(date__date=date,payment_type_daily_sale__payment = 'izettle (star)')
        sold_acc_istar = Sold_acc.objects.filter(date__date=date,payment_type__payment = 'izettle (star)')
        sold_acc_daily_salepayment_type = Sold_acc.objects.filter()
        
        
        for i in d_jobs:
            jobs_list_total.append(i.cost_deliver)
            current_date = i.date
        total_job = sum(jobs_list_total) 
        
        for accessories in sold_acc_daily_sale:
            acc_list_total.append(int(accessories.retail_price))
        total_accessories = sum(acc_list_total) 
        
        
        
         
        
        for cash_total in d_jobs_payment_type:
              d_jobs_payment_type_list.append(cash_total.cost_deliver)
        total_jobs_cash = sum(d_jobs_payment_type_list)
        
        for acc_cash in d_jobs_payment_cash_acc:
            d_jobs_payment_cash_acc_list.append(int(acc_cash.retail_price))
        total_acc_cash = sum(d_jobs_payment_cash_acc_list)
        
        total_jobs_cash = total_jobs_cash + total_acc_cash
        
        
        
        
    
        
        for card_total in d_jobs_payment_type_card:
            d_jobs_payment_type_card_list.append(card_total.cost_deliver)
        total_jobs_card = sum(d_jobs_payment_type_card_list)
        
        for acc_car in d_jobs_payment_type_card_acc:
            d_jobs_payment_type_card_acc_list.append(int(acc_car.retail_price))
        total_acc_card = sum(d_jobs_payment_type_card_acc_list)
            
        total_jobs_card = total_jobs_card + total_acc_card
        
        
        
        
        
        for amax_total in d_jobs_payment_type_amax:
            d_jobs_payment_type_amax_list.append(amax_total.cost_deliver)
        total_jobs_amax = sum(d_jobs_payment_type_amax_list)
        
        for total_jobs_acc_amax in d_jobs_payment_type_amax_acc:
            total_jobs_acc_amax_list.append(int(total_jobs_acc_amax.retail_price))
        total_jobs_acc = sum(total_jobs_acc_amax_list)
        
        total_jobs_amax = total_jobs_amax + int(total_jobs_acc)
            
        
        
        
        
        
        
        
        
        for irevive in d_jobs_payment_type_irevive:
            d_jobs_payment_type_amax_izettle_revive_list.append(irevive.cost_deliver)
        total_irevive = sum(d_jobs_payment_type_amax_izettle_revive_list)
        
        for i in sold_acc_irevive:
            sold_acc_irevive_list.append(int(i.retail_price))
        total_sold_acc_irevive = sum(sold_acc_irevive_list)
        
        total_irevive = total_irevive + total_sold_acc_irevive
        
        
        
        
        
        
        
        
        for istar in d_jobs_payment_type_istar:
             d_jobs_payment_type_amax_izettle_star_list.append(istar.cost_deliver)
        total_istar = sum(d_jobs_payment_type_amax_izettle_star_list)
        
        for i in sold_acc_istar:
            sold_acc_istar_list.append(int(i.retail_price))
        total_sold_acc_istar = sum(sold_acc_istar_list)
        
        total_istar = total_istar + total_sold_acc_istar
        
        
        
        
        Net_totals = total_job + total_accessories
        
        
        
        
        # data_total = Daily_totals(
        #     total = Net_totals,
        #     date = date
        # )
        # data_total.save()
        
        
             
            
            
    else:
        python_date = datetime.datetime.now()
        today = datetime.date.today()
        d_jobs = Daily_sale.objects.filter(date__date=today)
        sold_acc_daily_sale = Sold_acc.objects.filter(date__date=today)
        # sold_acc_count = Sold_acc.objects.filter(date__date=date, payment_type='Cash').count()
        d_jobs_payment_type = Daily_sale.objects.filter(date__date=today,payment_type_daily_sale__payment = 'Cash')
        d_jobs_payment_type_card = Daily_sale.objects.filter(date__date=today,payment_type_daily_sale__payment = 'Card')
        d_jobs_payment_type_amax = Daily_sale.objects.filter(date__date=today,payment_type_daily_sale__payment = 'Amax')
        d_jobs_payment_type_irevive = Daily_sale.objects.filter(date__date=today,payment_type_daily_sale__payment = 'izettle Revive')
        d_jobs_payment_type_istar = Daily_sale.objects.filter(date__date=today,payment_type_daily_sale__payment = 'izettle (star)')
        d_jobs_cash_count = Daily_sale.objects.filter(date__date=today, payment_type_daily_sale__payment = 'Cash').count()
        
        for i in d_jobs:
            jobs_list_total.append(i.cost_deliver)
            current_date = i.date
        total_job = sum(jobs_list_total)
        
        for accessories in sold_acc_daily_sale:
            acc_list_total.append(int(accessories.retail_price))
        total_accessories = sum(acc_list_total) 
        
        
        for cash_total in d_jobs_payment_type:
              d_jobs_payment_type_list.append(cash_total.cost_deliver)
        total_jobs_cash = sum(d_jobs_payment_type_list)
        
        for card_total in d_jobs_payment_type_card:
            d_jobs_payment_type_card_list.append(card_total.cost_deliver)
        total_jobs_card = sum(d_jobs_payment_type_card_list)
        
        for amax_total in d_jobs_payment_type_amax:
            d_jobs_payment_type_amax_list.append(amax_total.cost_deliver)
        total_jobs_amax = sum(d_jobs_payment_type_amax_list)
        
        
        
        for irevive in d_jobs_payment_type_irevive:
            d_jobs_payment_type_amax_izettle_revive_list.append(irevive.cost_deliver)
        total_irevive = sum(d_jobs_payment_type_amax_izettle_revive_list)
        
        for istar in d_jobs_payment_type_istar:
             d_jobs_payment_type_amax_izettle_star_list.append(istar.cost_deliver)
        total_istar = sum(d_jobs_payment_type_amax_izettle_star_list)
        
        Net_totals = total_job + total_accessories
        
        Net_totals = total_job + total_accessories
        
        
        
        # data_total = Daily_totals(
        #     total = Net_totals,
        #     date = date
        # )
        # data_total.save()
          
         
        
    context = {'d_jobs_context':d_jobs,
               'total_context':total_job,
               'date_context':date ,
            #    'python_date':python_date,
               'sold_acc_daily_sale_context':sold_acc_daily_sale,
               'total_accessories_context':total_accessories,
               'd_jobs_payment_type_context':d_jobs_payment_type,
               'total_jobs_cash_context':total_jobs_cash,
               'total_jobs_card_context':total_jobs_card,
               'total_jobs_amax_context':total_jobs_amax,
               'total_irevive_context':total_irevive,
               'total_istar_context':total_istar,
               'd_jobs_cash_count_context':d_jobs_cash_count,
               'Net_totals_context':Net_totals
               
               }


    return render(request,'daily_sale_report.html',context)

def End_of_day_sale(request):
    if request.method == "POST":
        date = request.POST.get("date")
        total = request.POST.get("total")
        
        # date = datetime.datetime.strftime(date, '%b %d %Y %I:%M%p')
        # date = date.replace(',','')
        # date = datetime.datetime.strptime(date ,'%b %d %Y').date()
        # date = datetime.datetime.strptime(date, '%Y/%d/%m %H:%M:%S')
        # date = datetime.datetime.date(date).strftime("%Y-%d-%m")
       
        
        
        data = Daily_totals(
            total = total,
            date = date
        )
        data.save()
    return render(request,'daily_sale_report.html')









def cart(request):
    payment = Payment_type.objects.all()
    context = {'payment_con':payment}
    
    return render(request,'add_sale.html',context)



def sold_accessories(request):
    sold_acc = Sold_acc.objects.all()
   
    context = {'sold_acc_context':sold_acc}
    
    return render(request,'sold_accessories.html',context)








def acce_cart(request,id):
    acce = Retail_Accessories.objects.get(id=id)
    payment_type = Payment_type.objects.all()
    
    
    if request.method == "POST":
        payment_type_name = request.POST.get("payment_type_name")
        delivery_comments_name = request.POST.get("delivery_comments_name")  
        cost_name = request.POST.get("cost_name")
        
        payment_type_v = Payment_type.objects.get(id=payment_type_name)
        
        data = Sold_acc(
                        # devices=  device_v,
                        # make = make_v,
                        # model = model_v,
                        # acce_name = acce_name_v,
                        # acce_colour = colour_name_v,
                        # supplier = supplier_name_v,
                        # cost = cost_name,
                        # acce_status = acce_status_v,
                        # quantity = quantity_name,
                        retail_acc = acce,
                        delivery_comments = delivery_comments_name,
                        payment_type = payment_type_v,
                        retail_price = cost_name,
                        date = datetime.datetime.now(),
                        user = request.user
                        )
        data.save()
        
        update_acc = Retail_Accessories.objects.filter(id=data.retail_acc.id).update(alocated=True)

    data1 = Acce_Cart(cart = acce)
    
    data1.save()    
        
        
        
    context = {"acce_context":acce, 'payment_type_context':payment_type}
    
    
    return render(request,'acce_cart.html',context)





