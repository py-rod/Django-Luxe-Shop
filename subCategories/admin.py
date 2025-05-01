from django.contrib import admin
from .models import SubCategories
# Register your models here.


@admin.register(SubCategories)
class SubCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug_sub': ('title',)}
    list_display = ['id', 'title', 'slug_sub',
                    'series', 'is_active', 'created']
    list_display_links = ['id', 'title', 'slug_sub']
    list_filter = ['is_active', ]
    list_per_page = 50
    search_fields = ['id', 'title']
