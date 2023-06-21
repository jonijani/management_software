from django.db import models
from customer.models import *
from django.contrib.auth.models import User



class Devices(models.Model):
    
    devices = models.CharField(max_length=250)

    def __str__(self):
        return self.devices

    def get_id(self):
        return self.id # with this function we can call specific ID for devices column

class Make(models.Model):
    device = models.ForeignKey(Devices,on_delete=models.CASCADE, related_name='make_device')
    make = models.CharField(max_length=250)

    def __str__(self):
        return self.make

    def get_make_id(self):
        return self.id # with this functuon we can call specific ID for Make column

class Model(models.Model):
    make = models.ForeignKey(Make,on_delete=models.CASCADE) 
    model = models.CharField(max_length=250)


    def __str__(self):
        return self.model

PAYMENT_STATUS = (
    ('PAID', 'PAID'),
    ('UNPAID', 'UNPAID'),
    ('CREDIT NOTE', 'CREDIT NOTE'),
    ('REFUND', 'REFUND')
    
)

TEST_ALL_FUNCTIONS = (
    ('MIC', 'MIC'),
    ('SCREEN', 'SCREEN'),
    ('HEARING SPEAKER', 'HEARING SPEAKER'),
    ('LOUD SPEAKER', 'LOUD SPEAKER'),
    ('WIFI', 'WIFI')
    
)


class Fault(models.Model):
    fault =  models.CharField(max_length=250)

    def __str__(self):
        return self.fault



class Accessories(models.Model):
    accessories =  models.CharField(max_length=250)

    def __str__(self):
        return self.accessories

class Sale_item(models.Model):
    sale_item =  models.CharField(max_length=250)

    def __str__(self):
        return self.sale_item

class Network(models.Model):
    network =  models.CharField(max_length=250)

    def __str__(self):
        return self.network


class Job_status(models.Model):
    job_status =  models.CharField(max_length=250)

    def __str__(self):
        return self.job_status

# class Payment_status(models.Model):
#     payment_status =  models.CharField(max_length=250)

#     def __str__(self):
#         return self.payment_status




class Jobs(models.Model):
    
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = 'job_customer')
    device =  models.ForeignKey(Devices,on_delete = models.CASCADE, related_name = 'job_device', null = True, blank=True)
    make = models.ForeignKey(Make,on_delete = models.CASCADE, related_name = 'job_make', null=True, blank=True)
    model = models.ForeignKey(Model,on_delete = models.CASCADE, related_name = 'job_model', null=True, blank=True)
    fault =  models.ForeignKey(Fault,on_delete = models.CASCADE, related_name = 'job_faults', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    imei = models.CharField(max_length=250, null=True, blank=True)
    accessories = models.ForeignKey(Accessories,on_delete = models.CASCADE, related_name = 'job_acessories', null=True, blank=True)
    sale_item = models.ForeignKey(Sale_item,on_delete = models.CASCADE, related_name = 'sale_acessories', null=True, blank=True)
    passcode = models.CharField(max_length=250, null=True, blank=True)
    network = models.ForeignKey(Network,on_delete = models.CASCADE, related_name = 'job_network', null=True, blank=True)
    cost = models.IntegerField(null=True, blank=True)
    vat = models.IntegerField(null=True, blank=True)
    Total_cost = models.IntegerField(null=True, blank=True)
    job_status = models.ForeignKey(Job_status,on_delete = models.CASCADE, related_name = 'job_job_status', null=True, blank=True)
    collection_time = models.DateTimeField(null=True, blank=True)
    payment_status = models.CharField(choices= PAYMENT_STATUS, max_length=250, null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    
    completed = models.BooleanField(default=False)



    def __str__(self):
        return str(self.id)

    def get_vat(self):
        return self.cost * 20 / 100
    v = get_vat

    def get_total_cost(self):
        return self.cost * 20 / 100 + self.cost
        
        
        


    



class Job_update(models.Model):

    job_update = models.ForeignKey(Jobs,on_delete = models.CASCADE, related_name = 'job_update' , null = True, blank=True)
    customer_update = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = 'customer_update', null = True, blank=True)
    device_update =  models.ForeignKey(Devices,on_delete = models.CASCADE, related_name = 'device_update', null = True, blank=True)
    make_update = models.ForeignKey(Make,on_delete = models.CASCADE, related_name = 'make_update', null = True, blank=True)
    model_update = models.ForeignKey(Model,on_delete = models.CASCADE, related_name = 'model_update', null = True, blank=True)
    fault_update =  models.ForeignKey(Fault,on_delete = models.CASCADE, related_name = 'fault_update', null = True, blank=True)
    description_update = models.TextField(null = True, blank=True)
    imei_update = models.CharField(max_length=250, null = True, blank=True)
    accessories_update = models.ForeignKey(Accessories,on_delete = models.CASCADE, related_name = 'accessories_update', null = True, blank=True)
    sale_item_update = models.ForeignKey(Sale_item,on_delete = models.CASCADE, related_name = 'update_sale_item', null = True, blank=True)
    passcode_update = models.CharField(max_length=250, null = True, blank=True)
    network_update = models.ForeignKey(Network,on_delete = models.CASCADE, related_name = 'network_update', null = True, blank=True)
    cost_update = models.IntegerField(null = True, blank=True)
    job_status_update = models.ForeignKey(Job_status,on_delete = models.CASCADE, related_name = 'job_status_update', null = True, blank=True)
    collection_time_update = models.DateTimeField(null = True, blank=True)
    payment_status_update = models.CharField(choices= PAYMENT_STATUS, max_length=250, null = True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.job_update.id)


class Fingerprints(models.Model):
    user_fprint = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date_time_fprint = models.CharField(max_length=250, null=True, blank=True)
    job_fprint = models.ForeignKey(Jobs,on_delete = models.CASCADE , null = True, blank=True)
    def __str__(self):
        return str(self.date_time_fprint)
    




class Reciepts(models.Model):
    reciept = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    


# class Contact_by_email(models.Model):
#     email = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f'{self.email.id} {self.email.customer.first_name} {self.email.customer.email}'



TEST_ALL_FUNCTIONS = (
    ('MIC', 'MIC'),
    ('SCREEN', 'SCREEN'),
    ('HEARING SPEAKER', 'HEARING SPEAKER'),
    ('LOUD SPEAKER', 'LOUD SPEAKER'),
    ('WIFI', 'WIFI')
    
)

class Complete_job(models.Model):
    c_job = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)
    complete_update = models.TextField(null = True, blank=True)
    checked = models.BooleanField(default=False)# its to show complete button as long as job is not completed.
    
    completed_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    #job_status_com = models.ForeignKey(Job_status,on_delete = models.CASCADE, related_name = 'job_status_update', null = True, blank=True)
    payment_status_com = models.CharField(choices= PAYMENT_STATUS, max_length=250, null = True, blank=True)
    cost_com = models.CharField(max_length=250, null = True, blank=True)
    completed_on = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        #return f'{self.c_job.id} {self.c_job.make} {self.c_job.make} '
        return self.complete_update

class Job_rebook(models.Model):
    j_rebook = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)
    
    cost_r = models.CharField(max_length=250, null = True, blank=True)
    rebooked_on = models.DateTimeField(null=True, blank=True)
    rebooked_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    eta_r = models.DateTimeField(null = True, blank=True)
    fault_r =  models.ForeignKey(Fault,on_delete = models.CASCADE, related_name = 'fault_r', null = True, blank=True)
    description_r = models.TextField(null = True, blank=True)
    imei_r = models.CharField(max_length=250, null = True, blank=True)

    def __str__(self):
        return str(self.j_rebook.id)


class Delivered(models.Model):
    
    job_deliver = models.ForeignKey(Jobs,on_delete = models.CASCADE, related_name = 'job_deliver' , null = True, blank=True)
    device_deliver =  models.ForeignKey(Devices,on_delete = models.CASCADE, related_name = 'device_deliver', null = True, blank=True)
    make_deliver = models.ForeignKey(Make,on_delete = models.CASCADE, related_name = 'make_deliver', null = True, blank=True)
    model_deliver = models.ForeignKey(Model,on_delete = models.CASCADE, related_name = 'model_deliver', null = True, blank=True)
    fault_deliver =  models.ForeignKey(Fault,on_delete = models.CASCADE, related_name = 'fault_deliver', null = True, blank=True)
    description_deliver = models.TextField(null = True, blank=True)
    imei_deliver = models.CharField(max_length=250, null = True, blank=True)
    #accessories_deliver = models.ForeignKey(Accessories,on_delete = models.CASCADE, related_name = 'accessories_deliver', null = True, blank=True)
    #sale_item_deliver = models.ForeignKey(Sale_item,on_delete = models.CASCADE, related_name = 'sale_item_deliver', null = True, blank=True)
    passcode_deliver = models.CharField(max_length=250, null = True, blank=True)
    #network_deliver = models.ForeignKey(Network,on_delete = models.CASCADE, related_name = 'network_deliver', null = True, blank=True)
    cost_deliver = models.IntegerField(null = True, blank=True)
    job_status_deliver = models.ForeignKey(Job_status,on_delete = models.CASCADE, related_name = 'job_status_deliver', null = True, blank=True)
    #collection_time_deliver = models.DateTimeField(null = True, blank=True)
    payment_status_deliver = models.CharField(choices= PAYMENT_STATUS, max_length=250, null = True, blank=True)
    delivery_comments = models.CharField(max_length=250, null = True, blank=True)
    delivered_on = models.DateTimeField(null=True, blank=True)
    delivered_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    delivered = models.BooleanField(default= False)
    
    def __str__(self):
        return str(self.job_deliver.id) 


class Pictures(models.Model):
    device_images = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    captured_at = models.DateTimeField(null=True, blank=True)
    captured_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    comments = models.CharField(max_length=250, null = True, blank=True)



    # def __str__(self):
    #     return str(self.device_images.id)























