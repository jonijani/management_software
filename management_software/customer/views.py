from django.shortcuts import render, redirect
from .models import Customer
from Jobs.models import  Jobs
import datetime
from django.http import HttpResponse
from django.db.models import Q





def home(request):
    return render(request,'login.html')

def add_customer(request):

    if request.method == "POST":
        client_type = request.POST.get('inlineRadioOptions')
        company_name = request.POST.get('company_name')
        vat_name = request.POST.get('vat_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        landline = request.POST.get('landline')
        email = request.POST.get('email')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        created_date = datetime.datetime.now()
        created_by = request.user#created_by new variable to bring authrosed user in request.user
        data = Customer(
                        client_type = client_type,
                        company = company_name,
                        vat = vat_name,
                        first_name=first_name,
                        last_name=last_name,
                        phone=phone, 
                        landline=landline,
                        email=email,
                        address=address, 
                        postcode=postcode , 
                        created_date=created_date ,
                        created_by=created_by  )#first parameter is column name(database) 2nd paarmeter is variable which will take data to database.
        #line 23 data is object for customer class which will call inbuilt function.save and save data to Customer table
        
        data.save()
        
        customer = Customer.objects.get(id=data.id)#first id compares newly created client id from database
        context = {'message':"New client has been created successfuly  ", 'customer_context':customer}
        return render(request, 'New_client_created.html',context)
        # return redirect('/')#/ is deafult page diverts to default home page
    else:
        return render(request, 'add_client_form.html')




def Client_little_info(request):
    find_client = Customer.objects.all()
    context = {'search_clients_context':find_client}
    return render(request, 'Client_little_info.html',context )

def Client_detail_info(request,id):
    customer = Customer.objects.get(id=id)
    jobs = Jobs.objects.filter(customer=customer)#first cusomer is field/column from job models and 2 customer is variable from  line 46
    context = {'customer_context':customer, 'jobs_context':jobs}
    return render(request, 'Client_detail_info.html',context)





    
def update_client_details(request,id):
    customer_update = Customer.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        landline = request.POST.get('landline')
        email = request.POST.get('email')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        created_date = datetime.datetime.now()
        #created_by = request.user#created_by new variable to bring authrosed user in request.user
        customer_update_data = Customer.objects.filter(id=id).update(first_name=first_name,
                                                                    last_name=last_name,
                                                                    phone=phone,
                                                                    landline=landline,
                                                                    email=email,
                                                                    address=address,
                                                                    postcode=postcode ,
                                                                    created_date=created_date  )
    context = {'customer_context':customer_update}# customer_update comes from line 56
    
    return render(request,'update_client_details.html',context)





def search_client(request):
    if request.method =="POST":
        searched = request.POST['searched']
        lookup = (Q(id__icontains=searched)
        |Q(first_name__icontains=searched)
        |Q(last_name__icontains=searched)
        |Q(phone__icontains=searched)
        |Q(landline__icontains=searched)
        |Q(email__icontains=searched)
        |Q(address__icontains=searched)
        |Q(postcode__icontains=searched))
        
        result = Customer.objects.filter(lookup)
    
        context = {'all_clients_context':result, 'searched':searched}
        return render(request,'search_client.html', context )

    else:
        return render(request,'search_client.html' )




