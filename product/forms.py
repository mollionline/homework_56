from django import forms
from django.core.validators import MinValueValidator

from product.models import Product, Category


class ProductForm(forms.Form):
    product = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=2000, required=True)
    price = forms.DecimalField(max_digits=7, decimal_places=2, required=True)
    remains = forms.IntegerField(validators=[MinValueValidator(0)], required=True)


class CategoryForm(forms.Form):
    category = forms.CharField(max_length=30, required=True)