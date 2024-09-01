from django.contrib import admin
from .models import Categories
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'slug', 'is_active']
    list_display_links = ['id', 'title', 'slug']
    list_filter = ['is_active', ]
    list_per_page = 50
    search_fields = ['id', 'title']
