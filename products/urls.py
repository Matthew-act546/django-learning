from django.contrib import admin
from django.urls import path

from products.views import (
    product_delete_view,
    product_create_view, 
    product_detail_view, 
    dynamic_lookup_view, 
    product_list_view,
)


app_name = 'product'
urlpatterns = [
    path('<int:my_id>/', dynamic_lookup_view, name='product'),
    path('<int:my_id>/delete/', product_delete_view, name='delete'),
    path('all-list/', product_list_view, name='product_list'),
    path('', product_detail_view, name='detail'),
    path('create/', product_create_view, name='create'),
]