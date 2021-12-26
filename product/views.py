from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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


def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'category_add_page.html')
    elif request.method == 'POST':
        try:
            category = request.POST.get('category')
            description = request.POST.get('description')
            added_cat = Category.objects.create(
                category=category,
                description=description
            )
            return HttpResponseRedirect('/')
        except BaseException:
            return HttpResponseRedirect("<h2>Категория существует/h2>")


def product_add_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    if request.method == 'GET':
        return render(request=request, template_name='product_add_page.html', context=context)
    elif request.method == 'POST':
        product = request.POST.get('product')
        description = request.POST.get('description')
        category = request.POST.get('category')
        created_at = request.POST.get('created_at')
        price = request.POST.get('price')
        image = request.POST.get('image')
        added_product = Product.objects.create(
            product=product,
            description=description,
            category=Category.objects.get(pk=category),
            created_at=created_at,
            price=price,
            image=image
        )
        url = reverse('product_detail', kwargs={'pk': added_product.pk})
        return HttpResponseRedirect(url)
