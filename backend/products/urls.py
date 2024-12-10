from django.urls import path, include
from .views import *

urlpatterns = [
   path('create_product/',create_product,name='create_product'),
    path('product_count/',product_count,name='product_count'),
    path('get_all/',get_all,name='get_all'),
   
]

