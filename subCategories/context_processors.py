from categories.models import Categories
from .models import SubCategories
import json


def menu_link(request):
    categories = Categories.objects.filter(is_active=True).order_by('id')

    sub = {}

    for category in categories:
        subcategory = SubCategories.objects.filter(
            series__title=category, is_active=True).order_by('id')
        sub[category] = subcategory

    return dict(subcategories=sub, categories=categories)
