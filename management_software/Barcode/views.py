from django.shortcuts import render, redirect
#from .models import Customer
import datetime
from django.http import HttpResponse
from Inventories.models import  *
from Jobs.models import *


def barcode(request):
    return render(request,'barcode.html')
