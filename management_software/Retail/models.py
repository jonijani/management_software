from django.db import models
from Jobs.models import *
from Accessories.models import *

class Payment_type(models.Model):
    payment = models.CharField(max_length=250, null = True, blank=True)

    def __str__(self):
        return self.payment
    


class Customer_cart(models.Model):
    c_cart = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)
    deliver_cost = models.CharField(max_length=250, null = True, blank=True)
    payment_type = models.ForeignKey(Payment_type,  on_delete=models.CASCADE, null = True, blank=True)
    reciept = models.ForeignKey(Reciepts,  on_delete=models.CASCADE, null = True, blank=True)
    delivery_comments = models.CharField(max_length=250, null = True, blank=True)
    sale_person = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    

    def get_make(self):
        return self.c_cart.make

    def get_imei(self):
        return self.c_cart.imei

    def get_model(self):
        return self.c_cart.model

    def get_job_id(self):
        return self.c_cart.id


# class Daily_sale(models.Model):
#     d_sale = models.ForeignKey(Customer_cart, on_delete = models.CASCADE, null=True, blank=True)

#     #payment_reciept = models.ForeignKey(Reciepts,  on_delete=models.CASCADE, null = True, blank=True)
#     sale_person = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
#     date = models.DateTimeField(null=True, blank=True)



#     def __str__(self):
#         return str(self.d_sale.id)


class Daily_sale(models.Model):
    
    job_deliver = models.ForeignKey(Jobs,on_delete = models.CASCADE, related_name = 'job_daily_sale' , null = True, blank=True)
    device_deliver =  models.ForeignKey(Devices,on_delete = models.CASCADE, related_name = 'device_daily_sale', null = True, blank=True)
    make_deliver = models.ForeignKey(Make,on_delete = models.CASCADE, related_name = 'make_daily_sale', null = True, blank=True)
    model_deliver = models.ForeignKey(Model,on_delete = models.CASCADE, related_name = 'model_daily_sale', null = True, blank=True)
    fault_deliver =  models.ForeignKey(Fault,on_delete = models.CASCADE, related_name = 'fault_daily_sale', null = True, blank=True)
    description_deliver = models.TextField(null = True, blank=True)
    imei_deliver = models.CharField(max_length=250, null = True, blank=True)
    passcode_deliver = models.CharField(max_length=250, null = True, blank=True)
    cost_deliver = models.IntegerField(null = True, blank=True)
    job_status_deliver = models.ForeignKey(Job_status,on_delete = models.CASCADE, related_name = 'job_status_daily_sale', null = True, blank=True)
    payment_status_deliver = models.CharField(choices= PAYMENT_STATUS, max_length=250, null = True, blank=True)
    delivery_comments = models.CharField(max_length=250, null = True, blank=True)
    payment_type_daily_sale = models.ForeignKey(Payment_type,on_delete = models.CASCADE, related_name = 'payment_type_daily', null = True, blank=True)
    reciept_daily_sale = models.ForeignKey(Reciepts,on_delete = models.CASCADE, related_name = 'reciept_daily_sale', null = True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    sale_person = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    delivered = models.BooleanField(default= False)
    
    # def __str__(self):
    #     return str(self.job_deliver.id)

class Daily_totals(models.Model):
    total = models.CharField(max_length=250, null = True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
 


class Acce_Cart(models.Model):
    cart = models.ForeignKey(Retail_Accessories, on_delete = models.CASCADE, null=True, blank=True)
    
    
    
    
    


class Sold_acc(models.Model):
    retail_acc = models.ForeignKey(Retail_Accessories, on_delete = models.CASCADE, null=True, blank=True)
    retail_price = models.CharField(max_length=250,null=True, blank=True)
    payment_type = models.ForeignKey(Payment_type,  on_delete=models.CASCADE, null = True, blank=True)
    delivery_comments = models.CharField(max_length=250, null = True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)  
    
    # def __str__(self):
        
    #     # return f"{self.id} {self.cart.acce_name}"
    #     return self.retail_acc.acce_name
    

class Email_admin_list(models.Model):
    email = models.CharField(max_length=250, null = True, blank=True)
      

    
    
    
    
    