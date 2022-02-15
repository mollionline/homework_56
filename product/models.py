from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.TextField(max_length=100, null=False, blank=False, unique=True, default='Разное')

    def __str__(self):
        return '{}'.format(self.category)


class Product(models.Model):
    product = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    remains = models.IntegerField(validators=[MinValueValidator(0)], null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.product)


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)], null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.pk)


class Order(models.Model):
    products = models.ManyToManyField(
        'product.Product',
        related_name='order',
        through='product.ProductOrder',
        through_fields=('order', 'products'),
        blank=True
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return '{}'.format(self.name)


class ProductOrder(models.Model):
    products = models.ForeignKey(
        'product.Product', related_name='products_order', on_delete=models.CASCADE, verbose_name='Продукты'
    )
    order = models.ForeignKey(
        'product.Order', related_name='order_products', on_delete=models.CASCADE, verbose_name='Заказ'
    )
    qty = models.IntegerField(validators=[MinValueValidator(0)], null=False, blank=False)

    def __str__(self):
        return '{}. {}'.format(self.products, self.order)
