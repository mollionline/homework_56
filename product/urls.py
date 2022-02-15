from django.urls import path
from product.views.product_views import (ListProductView,
                                         DetailProductView,
                                         CreateProductView,
                                         UpdateProductView,
                                         DeleteProductView,
                                         AddProductToBasketView,
                                         ListBasketOfProductsView,
                                         MinusProductToBasket,
                                         AddOrderView)

from product.views.category_views import (category_add_view,
                                          category_view,
                                          categories_view,
                                          category_edit_view,
                                          category_delete_view,
                                          cat_products_view)

urlpatterns = []

product_urls = [
    path('', ListProductView.as_view(), name='product_list'),
    path('products/?<int:pk>/', DetailProductView.as_view(), name='product_detail'),
    path('products/add/', CreateProductView.as_view(), name='product_add'),
    path('products/?<int:pk>/edit', UpdateProductView.as_view(), name='product_edit'),
    path('products/?<int:pk>/delete', DeleteProductView.as_view(), name='product_delete'),
    path('basket/?<int:pk>/', AddProductToBasketView.as_view(), name='add_to_basket'),
    path('basket/?<int:pk>/minus/', MinusProductToBasket.as_view(), name='minus_to_basket'),
    path('baskets/', ListBasketOfProductsView.as_view(), name='list_basket'),
    path('orders/add/', AddOrderView.as_view(), name='add_order')
]

category_urls = [
    path('categories/add/', category_add_view, name='category_add'),
    path('categories/', categories_view, name='categories_list'),
    path('categories/?<int:pk>/', category_view, name='category_detail'),
    path('categories/?<int:pk>/edit', category_edit_view, name='category_edit'),
    path('categories/?<int:pk>/delete', category_delete_view, name='category_delete'),
    path('products/<str:category>', cat_products_view, name='cat_products_list')
]

urlpatterns += product_urls
urlpatterns += category_urls
