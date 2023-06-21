from django.urls import path, include
from .import views

urlpatterns = [
    path('retail_sale_page/<str:id>', views.retail_sale_page, name='retail_sale_page'),
    path('customer_cart/<str:id>', views.customer_cart, name='customer_cart'),
    path('daily_sale_report/', views.daily_sale_report, name='daily_sale_report'),
    path('add_sale/', views.add_sale, name='add_sale'),
    path('acce_cart/<str:id>', views.acce_cart, name='acce_cart'),
    path('get_job/', views.get_job, name='get_job'),
    path('sold_accessories/', views.sold_accessories, name='sold_accessories'),
    path('End_of_day_sale/', views.End_of_day_sale, name='End_of_day_sale'),
    #path('daily_sale_report_dashboard/', views.daily_sale_report_dashboard, name='daily_sale_report_dashboard'),
    
    #path('get_phone/', views.get_job, name='get_job')
    
]







