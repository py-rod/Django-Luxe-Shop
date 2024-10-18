from django.contrib import admin
from .models import Products
# Register your models here.


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_prod': ('name',)}
    list_display = ['id', 'name', 'is_active', 'series', 'price', 'stock']
    list_display_links = ['id', 'name']
    list_editable = ['is_active', 'series']
    list_filter = ['series']
    search_fields = ['id', 'name']
