from django.db import models
import datetime
from django.contrib.auth.models import User


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    client_type = models.CharField(max_length=250, null=True, blank= True)
    company = models.CharField(max_length=250,null=True, blank= True )
    vat = models.CharField(max_length=250, null=True, blank= True)

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone  = models.IntegerField()
    landline  = models.IntegerField()
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    postcode = models.CharField(max_length=250)
    created_date = models.DateTimeField(null=True, blank= True)#
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

