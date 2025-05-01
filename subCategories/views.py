from django.shortcuts import render
from .models import SubCategories
from categories.models import Categories
from products.models import Products
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def products_of_the_sucategory(request, slug_category, slug_subcategory):
    title_window = SubCategories.objects.get(
        series__slug_cate=slug_category, slug_sub=slug_subcategory, is_active=True)

    category = SubCategories.objects.filter(
        series__slug_cate=slug_category, is_active=True).first()

    products = Products.objects.filter(
        series__series__slug_cate=slug_category, series__slug_sub=slug_subcategory)

    brands = products.values('brand').distinct().annotate(
        count=Count('brand'))

    today = timezone.now() - timedelta(days=7)

    # Filter form
    selected_brands = request.GET.getlist('brand')
    price_order = request.GET.get('price_order')

    if selected_brands:
        products = products.filter(brand__in=selected_brands)

    if price_order == 'asc':
        products = products.order_by('price')
    elif price_order == 'desc':
        products = products.order_by('-price')

    # Paginator

    return render(request, 'content_products.html', {
        'title_window': title_window,
        'products': products,
        'category': category.series,
        'subcategory': title_window,
        'brands': brands,
        'today': today,
        'selected_brands': selected_brands,
        'price_order': price_order,
    })
