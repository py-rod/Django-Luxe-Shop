from django.shortcuts import render
from .models import SubCategories
from categories.models import Categories
# Create your views here.


def products_of_the_sucategory(request, slug_category, slug_subcategory):
    title_window = SubCategories.objects.get(
        series__slug=slug_category, slug=slug_subcategory, is_active=True)
    return render(request, 'content_products.html', {
        'title_window': title_window
    })
