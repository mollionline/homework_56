from django.urls import path
from product.views import products_view, product_view, category_add_view, product_add_view, categories_view, \
    category_view, category_edit_view, category_delete_view, product_edit_view, product_delete_view, cat_products_view, SearchResultView

urlpatterns = [
    path('', products_view, name='product_list'),
    path('products/?<int:pk>/', product_view, name='product_detail'),
    path('categories/add/', category_add_view, name='category_add'),
    path('products/add/', product_add_view, name='product_add'),
    path('categories/', categories_view, name='categories_list'),
    path('categories/?<int:pk>/', category_view, name='category_detail'),
    path('categories/?<int:pk>/edit', category_edit_view, name='category_edit'),
    path('categories/?<int:pk>/delete', category_delete_view, name='category_delete'),
    path('products/?<int:pk>/edit', product_edit_view, name='product_edit'),
    path('products/?<int:pk>/delete', product_delete_view, name='product_delete'),
    path('products/<str:category>', cat_products_view, name='cat_products_list'),
    path('search/', SearchResultView.as_view(), name='search_result')
]
