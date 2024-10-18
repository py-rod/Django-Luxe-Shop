from django.shortcuts import render
from .models import SubCategories
from categories.models import Categories
from products.models import Products
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
# Create your views here.


def products_of_the_sucategory(request, slug_category, slug_subcategory):
    title_window = SubCategories.objects.get(
        series__slug_cate=slug_category, slug_sub=slug_subcategory, is_active=True)

    category = SubCategories.objects.filter(
        series__slug_cate=slug_category, is_active=True).first()

    products = Products.objects.filter(
        series__series__slug_cate=slug_category, series__slug_sub=slug_subcategory)

    brands = Products.objects.values('brand').annotate(
        count=Count('brand')).order_by('brand')

    today = timezone.now() - timedelta(days=7)
    print(today)

    return render(request, 'content_products.html', {
        'title_window': title_window,
        'products': products,
        'category': category.series,
        'brands': brands,
        'today': today
    })
