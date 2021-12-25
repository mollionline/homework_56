from django.shortcuts import render

# Create your views here.
from product.models import Product, Category

def product_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request=request,
                  template_name='product_list.html',
                  context=context)
