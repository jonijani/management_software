from django.urls import path , include
from .import views
from django.urls import path

urlpatterns = [
    path('client_dashboard', views.client_dashboard, name='client_dashboard'),
    path('jobs_dashboard', views.jobs_dashboard, name='jobs_dashboard'),
    path('Accessories_dashboard', views.Accessories_dashboard, name='Accessories_dashboard'),
    path('parts_dashboard', views.parts_dashboard, name='parts_dashboard'),
    # path('jobs_dashboard', views.jobs_dashboard, name='jobs_dashboard'),
    # path('jobs_dashboard', views.jobs_dashboard, name='jobs_dashboard'),
    
    path('daily_sale_report_dashboard', views.daily_sale_report_dashboard, name='daily_sale_report_dashboard'),
    
    

]