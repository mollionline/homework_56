from django.urls import path
from product.views import products_view

urlpatterns = [
    path('', products_view, name='product_list')
]