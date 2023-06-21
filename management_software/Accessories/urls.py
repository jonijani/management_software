
from django.urls import path
from .import views

urlpatterns = [
    path('Accessories/', views.Accessories, name='Accessories'),
    path('Add_new_accessories/', views.Add_new_accessories, name='Add_new_accessories'),
    #path('acce_cart/<str:id>', views.acce_cart, name='acce_cart'),
    
]