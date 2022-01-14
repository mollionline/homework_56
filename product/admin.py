from django.contrib import admin
from product.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'description']
    list_filter = ['category']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'description', 'created_at', 'price', 'image', 'remains']
    list_filter = ['product']
    search_fields = ['product', 'created_at']
    fields = ['product', 'category', 'description', 'created_at', 'price', 'image', 'remains']
    readonly_fields = ['created_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
