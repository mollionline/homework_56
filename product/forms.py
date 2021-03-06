from django import forms
from product.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'description', 'category', 'price', 'remains']


class CategoryForm(forms.Form):
    category = forms.CharField(max_length=30, required=True)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, required=False)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']
