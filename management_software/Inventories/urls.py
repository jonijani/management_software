
from django.urls import path
from .import views

urlpatterns = [
    path('inventories_dashboard/', views.inventories_dashboard, name='inventories_dashboard'),
    path('Add_new_part/', views.Add_new_part, name='Add_new_part'),
    path('part_added/<str:id>', views.part_added, name='part_added'),
    path('part_detail/<str:id>', views.part_detail, name='part_detail'),
    path('update_part/<str:id>', views.update_part, name='update_part'),
    path('search_parts/', views.search_parts, name='search_parts'),
    path('request_part/<str:id>', views.request_part, name='request_part'),
    path('all_requested_parts/', views.all_requested_parts, name='all_requested_parts'),
    path('requested_part_detail/<str:id>', views.requested_part_detail, name='requested_part_detail'),
    path('ordered_parts/', views.ordered_parts, name='ordered_parts'),  
    path('update_requested_part/<str:id>', views.update_requested_part, name='update_requested_part'),
    path('ordered_part_detail/<str:id>', views.ordered_part_detail, name='ordered_part_detail'),
    path('ordered_parts_arrived/<str:id>', views.ordered_parts_arrived, name='ordered_parts_arrived'),

]









