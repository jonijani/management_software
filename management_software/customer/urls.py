"""fonedoctors_junaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path , include
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add_customer', views.add_customer, name='add_customer'),
    #path('New_client_created', views.New_client_created, name='New_client_created'),
    path('Client_little_info', views.Client_little_info, name='Client_little_info'),
    path('search_client', views.search_client, name='search_client'),
    path('Client_detail_info/<str:id>', views.Client_detail_info, name='Client_detail_info'),
    path('update_client_details/<str:id>', views.update_client_details, name='update_client_details'),
    

]