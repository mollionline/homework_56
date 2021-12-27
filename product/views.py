from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
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


def product_edit_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        categories = Category.objects.all()
        if request.method == 'POST':
            product.product = request.POST.get('product')
            product.description = request.POST.get('description')
            product.category = Category.objects.get(pk=request.POST.get('category'))
            product.price = request.POST.get('price')
            product.image = request.POST.get('image')
            product.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'product_edit.html', {'product': product, 'categories': categories})
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def product_delete_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return HttpResponseRedirect('/')
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


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
            return HttpResponseRedirect('/categories/')
        except BaseException:
            return HttpResponseRedirect("<h2>Категория существует/h2>")


def categories_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request=request,
                  template_name='categories_list.html',
                  context=context)


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category
    }
    return render(request=request,
                  template_name='category_detail.html',
                  context=context)


def category_edit_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        if request.method == 'POST':
            category.category = request.POST.get('category')
            category.description = request.POST.get('description')
            category.save()
            return HttpResponseRedirect('/categories/')
        else:
            return render(request, 'category_edit.html', {'category': category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")


def category_delete_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        return HttpResponseRedirect('/categories/')
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")


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
        price = request.POST.get('price')
        image = request.POST.get('image')
        added_product = Product.objects.create(
            product=product,
            description=description,
            category=Category.objects.get(pk=category),
            price=price,
            image=image
        )
        url = reverse('product_detail', kwargs={'pk': added_product.pk})
        return HttpResponseRedirect(url)
