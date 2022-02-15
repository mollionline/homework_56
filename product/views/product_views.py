from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, ListView, TemplateView
from product.models import Product, Basket, Order, ProductOrder
from product.forms import ProductForm, SearchForm, OrderForm
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


class AddProductToBasketView(TemplateView):
    model = Basket

    def post(self, request, *args, **kwargs):
        product_pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)
        if not self.model.objects.filter(product_id=product_pk) and product.remains > 0:
            Basket.objects.create(quantity=1, product_id=product_pk)
        elif self.model.objects.filter(quantity__lt=product.remains, product_id=product_pk):
            basket_prod = get_object_or_404(Basket, product_id=product_pk)
            basket_prod.quantity += 1
            basket_prod.save()
        return redirect('/baskets/')


class MinusProductToBasket(TemplateView):
    model = Basket

    def post(self, request, *args, **kwargs):
        product_pk = kwargs.get('pk')
        product = get_object_or_404(Product, pk=product_pk)
        if self.model.objects.filter(quantity__gt=1, product_id=product_pk):
            basket_prod = get_object_or_404(Basket, product_id=product_pk)
            basket_prod.quantity -= 1
            basket_prod.save()
        elif self.model.objects.filter(quantity=1, product_id=product_pk):
            prod = self.model.objects.filter(quantity=1, product_id=product_pk)
            prod.delete()
        return redirect('/baskets/')


class ListBasketOfProductsView(ListView):
    model = Basket
    context_object_name = 'baskets'
    template_name = 'basket/basket_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        total = 0
        for tot in self.model.objects.all():
            total += (tot.product.price * tot.quantity)
        context['total'] = total
        return context


class AddOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/basket_list.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        baskets = Basket.objects.all()
        if form.is_valid():
            order = self.model.objects.create(
                name=form.cleaned_data.get('name'),
                phone=form.cleaned_data.get('phone'),
                address=form.cleaned_data.get('address')
            )
            order.save()
            for basket in Basket.objects.all():
                ProductOrder.objects.create(qty=basket.quantity, order_id=order.pk, products_id=basket.product_id)
            Basket.objects.all().delete()
            return redirect('/baskets/')
        return render(request, self.template_name, context={'form': form, 'baskets': baskets})
