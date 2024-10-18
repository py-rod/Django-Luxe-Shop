from django.contrib import admin
from .models import Categories
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_cate': ('title',)}
    list_display = ['id', 'title', 'slug_cate', 'is_active']
    list_display_links = ['id', 'title', 'slug_cate']
    list_filter = ['is_active', ]
    list_per_page = 50
    search_fields = ['id', 'title']
