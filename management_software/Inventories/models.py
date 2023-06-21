from django.db import models
from Jobs.models import *
from django.contrib.auth.models import User
import barcode             
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File




class Part_name(models.Model):
    part_name = models.CharField(max_length=250)


    def __str__(self):
        return self.part_name


class Part_colour(models.Model):
    colour = models.CharField(max_length=250)


    def __str__(self):
        return self.colour



class Supplier(models.Model):
    supplier = models.CharField(max_length=250)


    def __str__(self):
        return self.supplier


class Part_status(models.Model):
    p_status = models.CharField(max_length=250)


    def __str__(self):
        return self.p_status


class Inventories(models.Model):
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE, related_name = 'job_inventory',null=True, blank=True)
    devices = models.ForeignKey(Devices,on_delete=models.CASCADE, related_name = 'inventory_device')
    make = models.ForeignKey(Make,on_delete=models.CASCADE, related_name = 'inventory_make')
    model = models.ForeignKey(Model,on_delete=models.CASCADE, related_name = 'inventory_model')
    part_name = models.ForeignKey(Part_name,on_delete=models.CASCADE, related_name = 'inventory_part_name')
    part_colour = models.ForeignKey(Part_colour,on_delete=models.CASCADE, related_name = 'inventory_Part_colour')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name = 'inventory_supplier')
    quantity = models.IntegerField()
    cost = models.IntegerField()
    part_status = models.ForeignKey(Part_status,on_delete=models.CASCADE, related_name = 'i_part_status',null=True, blank=True)
    
    barcode = models.ImageField(upload_to='barcodes/', blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    alocated = models.BooleanField(default=False)
    
    def part_no(self):

        return self.id

    # def __str__(self):
    #     return f"{self.id } {self.devices.devices} {self.make.make} {self.model.model} {self.part_name} {self.part_colour} {self.quantity} {self.cost}"


    # def save(self, *args, **kwargs):          # overriding save() 
    #     Code128 = barcode.get_barcode_class('Code128')
    #     rv = BytesIO()
    #     code = Code128(f'{self.part_no}', writer=ImageWriter()).write(rv)
    #     self.barcode.save(f'{self.part_no}.png', File(rv), save=False)
    #     return super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):          # overriding save() 
    #     Code39 = barcode.get_barcode_class('Code39')
    #     rv = BytesIO()
    #     code = Code39(self.id, writer=ImageWriter()).write(rv)
    #     self.barcode.save(f'{self.id}.png', File(rv), save=False)
    #     return super().save(*args, **kwargs)

#class Order_parts(models.Model):
class Request_parts(models.Model):    
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE, related_name = 'job_order_part',null=True, blank=True)
    devices = models.ForeignKey(Devices,on_delete=models.CASCADE, related_name = 'order_device')
    make = models.ForeignKey(Make,on_delete=models.CASCADE, related_name = 'order_make')
    model = models.ForeignKey(Model,on_delete=models.CASCADE, related_name = 'order_model')
    part_name = models.ForeignKey(Part_name,on_delete=models.CASCADE, related_name = 'order_part_name')
    part_colour = models.ForeignKey(Part_colour,on_delete=models.CASCADE, related_name = 'order_Part_colour')
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name = 'order_supplier')
    quantity = models.IntegerField()
    buying_cost = models.IntegerField()
    part_description = models.CharField(max_length=20000, null=True, blank=True)
    part_status = models.ForeignKey(Part_status,on_delete=models.CASCADE, related_name = 'order_part_status',null=True, blank=True)
    #barcode = models.ImageField(upload_to='barcodes/', blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    

class Ordered_parts(models.Model):    
    #job = models.ForeignKey(Jobs,on_delete=models.CASCADE, related_name = 'job_ordered_part',null=True, blank=True)
    requested_parts_ordered = models.ForeignKey(Request_parts,on_delete=models.CASCADE, related_name = 'requested_parts_ordered',null=True, blank=True)
    #devices = models.ForeignKey(Devices,on_delete=models.CASCADE, related_name = 'ordered_device')
    make = models.ForeignKey(Make,on_delete=models.CASCADE, related_name = 'ordered_make', null=True, blank=True)
    #model = models.ForeignKey(Model,on_delete=models.CASCADE, related_name = 'ordered_model')
    #part_name = models.ForeignKey(Part_name,on_delete=models.CASCADE, related_name = 'ordered_part_name')
    #part_colour = models.ForeignKey(Part_colour,on_delete=models.CASCADE, related_name = 'ordered_Part_colour')
    #supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name = 'ordered_supplier')
    #quantity = models.IntegerField(null=True, blank=True)
    #buying_cost = models.IntegerField(null=True, blank=True)
    #part_description = models.CharField(max_length=20000, null=True, blank=True)
    part_status = models.ForeignKey(Part_status,on_delete=models.CASCADE, related_name = 'ordered_part_status',null=True, blank=True)
    eta = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    
    def requested_parts_ID(self):
    
        return self.requested_parts_ordered.id
    


