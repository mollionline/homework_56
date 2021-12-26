from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.category)


class Product(models.Model):
    product = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    price = models.DecimalField(max_digits=19, decimal_places=3, null=False, blank=False)
    image = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return '{}. {}'.format(self.pk, self.product)
