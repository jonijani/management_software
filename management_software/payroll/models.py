from time import strftime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, time
import datetime as dt

from datetime import timedelta

class staff_info(models.Model):
    U_name = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True )
    first_name =  models.CharField(max_length=250,null=True, blank=True )
    last_name = models.CharField(max_length=250,null=True, blank=True )
    home_number = models.CharField(max_length=250,null=True, blank=True )
    mobile = models.CharField(max_length=250,null=True, blank=True )
    nationility = models.CharField(max_length=250,null=True, blank=True )
    passport_no = models.CharField(max_length=250,null=True, blank=True )
    adress = models.CharField(max_length=250,null=True, blank=True )
    postcode = models.CharField(max_length=250,null=True, blank=True )
    bank_details = models.CharField(max_length=250,null=True, blank=True )
    
    def __str__(self):
        return self.U_name.username




    

class Staff_salary_package(models.Model):
    staff =  models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True ,related_name='staff')
    total_yearly_salary =  models.CharField(max_length=250)
    date = models.DateTimeField(null=True, blank=True)
    
    
    
    def weekly_salary(self):
        return int(self.total_yearly_salary) / int(52)
    
    def daily_salary(self):
        return int(self.total_yearly_salary) / int(52) / int(5)
    
    def Hour_salary(self):
        return (int(self.total_yearly_salary) / int(52) / int(5) / int(8))
    
    def minutes_salary(self):
        return (int(self.total_yearly_salary) / int(52) / int(5) / int(8) /int(60))
    
    
    
    def __str__(self):
        return self.staff.username
    
    
    # def worked_hours_wages(self):
    #     return int(self.staff_hours_worked.Hours_worked) * int(self.Hour_salary)







class Staff_times(models.Model):
    name =  models.ForeignKey(Staff_salary_package, on_delete = models.CASCADE,blank=True, null=True)
    d_date =  models.DateField(null=True, blank=True)
    start_time =  models.TimeField(null=True, blank=True)
    end_time =  models.TimeField(null=True, blank=True)
    hours_worked_field =  models.CharField(max_length=250,null=True, blank=True)
    hourly_wages = models.CharField(max_length=250,null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
   
    
    
    
    
    
       
        









    
 



    
    
    








