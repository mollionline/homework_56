from django.template.defaultfilters import urlencode
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView
from product.models import Product
from product.forms import ProductForm, SearchForm
from product.views.helpers import SearchView


# Create your views here.
class ListProductView(SearchView):
    template_name = 'product/product_list.html'
    model = Product
    ordering = ('product',)
    paginate_by = 5
    context_object_name = 'products'
    search_form = SearchForm
    search_fields = {
        'product': 'icontains'
    }

    def get_queryset(self):
        return super().get_queryset().filter(remains__gt=0).order_by('product')


class DetailProductView(DetailView):
    context_object_name = 'product'
    model = Product
    template_name = 'product/product_detail.html'


class UpdateProductView(UpdateView):
    template_name = 'product/product_edit.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.get_object().pk})


class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class CreateProductView(CreateView):
    model = Product
    template_name = 'product/product_add_page.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})
