from django.contrib import admin
from product.models import Category, Product, Order, ProductOrder, Basket


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    list_filter = ['category']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'description', 'created_at', 'price', 'remains']
    list_filter = ['product']
    search_fields = ['product', 'created_at']
    fields = ['product', 'category', 'description', 'created_at', 'price', 'remains']
    readonly_fields = ['created_at']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'created_at']
    ordering = ['-created_at']


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'products', 'order', 'qty']
    ordering = ['order']


class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']
    ordering = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductOrder, ProductOrderAdmin)
admin.site.register(Basket, BasketAdmin)
