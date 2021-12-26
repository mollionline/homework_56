from django.shortcuts import render, get_object_or_404

# Create your views here.
from product.models import Product, Category


def products_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request=request,
                  template_name='product_list.html',
                  context=context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request=request,
                  template_name='product_detail.html',
                  context=context)
