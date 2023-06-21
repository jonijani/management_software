from django.db import models
from Jobs.models import *
from Inventories.models import *
from Retail.models import *
from django.contrib.auth.models import User
from Retail.models import *

class Acceesories_name(models.Model):
    acce_name = models.CharField(max_length=250)


    def __str__(self):
        return self.acce_name


# class Acceesories_colour(models.Model):
#     colour = models.CharField(max_length=250)


#     def __str__(self):
#         return self.colour




class Acceesories_status(models.Model):
    acce_status = models.CharField(max_length=250)


    def __str__(self):
        return self.acce_status


class Retail_Accessories(models.Model):
    devices = models.ForeignKey(Devices,on_delete=models.CASCADE, related_name = 'acceessories_device')
    make = models.ForeignKey(Make,on_delete=models.CASCADE, related_name = 'acceessories_make')
    model = models.ForeignKey(Model,on_delete=models.CASCADE, related_name = 'acceessories_model')
    acce_name = models.ForeignKey(Acceesories_name,on_delete=models.CASCADE, related_name = 'acceessories_part_name')
    acce_colour = models.ForeignKey(Part_colour,on_delete=models.CASCADE, related_name = 'acceessories_colour')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name = 'accessories_supplier')
    quantity = models.IntegerField()
    cost = models.IntegerField()
    retail_price = models.IntegerField(null=True, blank=True)

    acce_status = models.ForeignKey(Acceesories_status,on_delete=models.CASCADE, related_name = 'accessories_status',null=True, blank=True)
    # barcode = models.ImageField(upload_to='barcodes/', blank=True)
    date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    alocated = models.BooleanField(default=False)
    
    
    




