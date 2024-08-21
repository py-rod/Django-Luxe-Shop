from django.contrib import admin
from .models import ImagesSlider

# Register your models here.


@admin.register(ImagesSlider)
class ImagesSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_upload', 'active']
    list_display_links = ['id', 'title']
    list_editable = ['active',]
    list_per_page = 20
    list_filter = ['active']
    search_fields = ['id', 'title']
