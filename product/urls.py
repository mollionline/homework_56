from django.urls import path
from product.views import products_view, product_view, category_add_view

urlpatterns = [
    path('', products_view, name='product_list'),
    path('products/?<int:pk>/', product_view, name='product_detail'),
    path('categories/add/', category_add_view, name='category_add')
]