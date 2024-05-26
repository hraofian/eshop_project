from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Avg , Min , Max
from django.views.generic.base import TemplateView
from django.views.generic import ListView





class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


# class ProductListView(TemplateView):
#     template_name = 'product_module/product_list.html'

#     def get_context_data(self, **kwargs: Any):
#         products = Product.objects.all().order_by('price')[:5]
#         context = super(ProductListView, self).get_context_data()
#         context['products'] = products
#         return context


# def product_list(request):
#     products = Product.objects.all().order_by("-price")[:5]
#     return render(request , 'product_module/product_list.html', {
#         'products': products,
#     })

 

# def product_detail(request , slug):
#     product = get_object_or_404(Product , slug=slug)
#     return render(request, 'product_module/product_detail.html', {
#         'product': product,
#     })

class ProductDetailView(TemplateView):
    template_name = 'product_module/product_detail.html'

    def get_context_data(self, **kwargs):
        context =  super(ProductDetailView , self).get_context_data()
        slug = kwargs['slug']
        product = get_object_or_404(Product , slug=slug)
        context['product'] = product
        return context

