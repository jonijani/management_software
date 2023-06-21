from django.shortcuts import render, redirect
from .models import *
from Jobs.models import  *
from Inventories.models import  *

def Add_new_accessories(request):
    device = Devices.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    acceesories_name = Acceesories_name.objects.all()
    acceesories_colour = Part_colour.objects.all()
    acc_supplier = Supplier.objects.all()
    acceesories_status = Acceesories_status.objects.all()

    if request.method == "POST":
        device = request.POST.get('device_mobile')
        make = request.POST.get('make_name')
        model = request.POST.get('model_name')
        acce_name = request.POST.get('acce_name')
        colour_name = request.POST.get('colour_name')
        supplier_name = request.POST.get('supplier_name')
        quantity_name = request.POST.get('quantity_name')  
        cost_name = request.POST.get('cost_name')
        retail_price_name = request.POST.get('retail_price_name')
        acce_status = request.POST.get('acce_status')

        
        device_v = Devices.objects.get(devices=device)
        make_v = Make.objects.get(make=make)
        model_v = Model.objects.get(model=model)
        acce_name_v = Acceesories_name.objects.get(acce_name=acce_name)
        colour_name_v = Part_colour.objects.get(colour=colour_name)
        supplier_name_v = Supplier.objects.get(supplier=supplier_name)
        acce_status_v = Acceesories_status.objects.get(acce_status=acce_status)
        
        for i in range(int(quantity_name)):

            data = Retail_Accessories(
                                    devices=  device_v,
                                    make = make_v,
                                    model = model_v,
                                    acce_name = acce_name_v,
                                    acce_colour = colour_name_v,
                                    supplier = supplier_name_v,
                                    cost = cost_name,
                                    retail_price = retail_price_name,
                                    acce_status = acce_status_v,
                                    quantity = quantity_name,
                                    date = datetime.datetime.now(),
                                    user = request.user,
                                 )
            data.save()
        return redirect('Accessories')



    context = {'device_context': device,
                'make_context':make,
                'model_context':model,
                'acceesories_name_context':acceesories_name,
                'acceesories_colour_context':acceesories_colour,
                'supplier_context':acc_supplier,
                'acceesories_status_context':acceesories_status

                }

    return render(request,'Add_new_accessories.html',context)

def Accessories(request):
    acc = Retail_Accessories.objects.all()
    context = {'acc_context':acc}
    return render(request,'Accessories.html',context )






















