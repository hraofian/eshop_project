from django.shortcuts import render , get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Avg , Min , Max

def product_list(request):
    products = Product.objects.all().order_by("title")
    number_of_product = products.count()
    # avg_rating = products.aggregate(Avg("rating") , Min("price"), Max("id"))
    return render(request , 'product_module/product_list.html', {
        'products': products,
        'total_number_of_product':number_of_product,
        # 'avaeage_rating':avg_rating,
    })



def product_detail(request , slug):
    product = get_object_or_404(Product , slug=slug)
    return render(request, 'product_module/product_detail.html', {
        'product': product,

    })