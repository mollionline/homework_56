from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.
from product.models import Product, Category
from product.forms import CategoryForm


def category_add_view(request):
    if request.method == 'GET':
        return render(request, 'category/category_add_page.html')
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
            template_name='category/category_add_page.html',
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
                  template_name='category/categories_list.html',
                  context=context)


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category
    }
    return render(request=request,
                  template_name='category/category_detail.html',
                  context=context)


def category_edit_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category.category = form.cleaned_data['category']
            category.save(update_fields=['category'])
            return HttpResponseRedirect('/categories/')
        else:
            return render(request, 'category/category_edit.html', context={
                'category': category,
                'form': form,
                'errors': form.errors
            })
    elif request.method == 'GET':
        form = CategoryForm(initial={
            'category': category.category
        })
        return render(request, 'category/category_edit.html', context={
            'category': category,
            'form': form,
            'errors': form.errors
        })


def category_delete_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return HttpResponseRedirect('/')


def cat_products_view(request, category):
    category_name = Category.objects.get(category=category)
    products = Product.objects.filter(category=category_name.pk).order_by('product')
    return render(request, 'category_products_list.html', context={'products': products, 'category': category_name})
