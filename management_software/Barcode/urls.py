from django.urls import path , include
from .import views
from django.urls import path

urlpatterns = [
    path('', views.barcode, name='barcode'),
    

]