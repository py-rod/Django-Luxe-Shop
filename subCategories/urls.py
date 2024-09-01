from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug_category>/<slug:slug_subcategory>',
         views.products_of_the_sucategory, name='products_of_the_subcategory')
]
