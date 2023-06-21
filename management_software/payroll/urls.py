from django.urls import path , include
from .import views
from django.urls import path

urlpatterns = [
    path('staff/', views.staff, name='staff'),
    # path('staff/', views.time_and_wages, name='time_and_wages'),
    path('staff_salary_package', views.staff_salary_package, name='staff_salary_package'),
    

]