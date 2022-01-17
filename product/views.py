from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db import IntegrityError

# Create your views here.
from product.models import Product, Category
from product.forms import ProductForm, CategoryForm


def products_view(request):
    products = Product.objects.filter(remains__gt=0).order_by('category').order_by('product')
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
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.product = form.cleaned_data['product']
            product.description = form.cleaned_data['description']
            product.category = Category.objects.get(pk=request.POST.get('category'))
            product.price = form.cleaned_data['price']
            product.remains = form.cleaned_data['remains']
            product.save(update_fields=['product', 'description', 'category', 'price', 'remains'])
            return HttpResponseRedirect('/')
        else:
            return render(request, 'product_edit.html', context={
                'product': product,
                'form': form,
                'errors': form.errors,
                'categories': Category.objects.all()
            })
    elif request.method == 'GET':
        form = ProductForm(initial={
            'product': product.product,
            'description': product.description,
            'category': product.category,
            'price': product.price,
            'remains': product.remains
        })
        return render(request, 'product_edit.html', context={
            'product': product,
            'form': form,
            'errors': form.errors,
            'categories': categories
        })


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return HttpResponseRedirect('/')


def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'category_add_page.html')
    elif request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category, is_not_new = Category.objects.get_or_create(
                category=form.cleaned_data.get('category'),
            )
            url = reverse('category_detail', kwargs={
                'pk': category.pk
            })
            return HttpResponseRedirect(url)
        return render(
            request=request,
            template_name='category_add_page.html',
            context={
                'errors': form.errors,
                'form': form
            }
        )


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
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category.category = form.cleaned_data['category']
            category.save(update_fields=['category'])
            return HttpResponseRedirect('/')
        else:
            return render(request, 'category_edit.html', context={
                'category': category,
                'form': form,
                'errors': form.errors
            })
    elif request.method == 'GET':
        form = CategoryForm(initial={
            'category': category.category
        })
        return render(request, 'category_edit.html', context={
            'category': category,
            'form': form,
            'errors': form.errors
        })


def category_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return HttpResponseRedirect('/')


def product_add_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    if request.method == 'GET':
        return render(request=request, template_name='product_add_page.html', context=context)
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product, is_not_new = Product.objects.get_or_create(
                product=form.cleaned_data.get('product'),
                description=form.cleaned_data.get('description'),
                category=Category.objects.get(pk=request.POST.get('category')),
                price=form.cleaned_data.get('price'),
                remains=form.cleaned_data.get('remains')
            )
            url = reverse('product_detail', kwargs={
                'pk': product.pk
            })
            return HttpResponseRedirect(url)
        return render(
            request=request,
            template_name='product_add_page.html',
            context={
                'categories': Category.objects.all(),
                'errors': form.errors,
                'form': form
            }
        )
