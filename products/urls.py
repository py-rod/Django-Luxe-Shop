from django.urls import path
from . import views


urlpatterns = [
    path('<slug:cate_slug>/<slug:sub_slug>/<slug:prod_slug>',
         views.product_detail, name='product_detail')
]
