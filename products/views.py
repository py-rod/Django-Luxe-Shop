from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Products

# Create your views here.


def product_detail(request, cate_slug, sub_slug, prod_slug):
    single_product = Products.objects.get(
        series__series__slug_cate=cate_slug, series__slug_sub=sub_slug, slug_prod=prod_slug)

    print(single_product.name)

    return render(request, 'product_detail.html', {
        'product': single_product
    })
