from django.urls import path
from .views import *

urlpatterns = [
    path('Products/',Products,name='Products'),
    path('Products/<int:pk>/',Products,name='Products_crud'),
    path('product_count/',product_count,name='product_count'),
    path('all_products/',all_products,name='all_products'),
    path('all_active_product/',all_active_product,name="all_active_product"),

    path('categories/',category_list,name='category_list'),
    path('categories/<int:pk>/',categories,name='catogory_crud'),
    path('category_count',category_count,name='category_count'),
]

