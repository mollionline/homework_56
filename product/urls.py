from django.urls import path
from product.views import products_view, product_view

urlpatterns = [
    path('', products_view, name='product_list'),
    path('products/?<int:pk>/', product_view, name='product_detail')
]