from django.db import models
from subCategories.models import SubCategories
import os
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.


class Products(models.Model):
    def image_upload_to(self, instance):
        if instance:
            return os.path.join('Products_images', slugify(self.name), instance)
        return None

    name = models.CharField(max_length=100, default='',
                            blank=False, unique=True)
    slug_prod = models.SlugField(default='', blank=False, unique=True)
    series = models.ForeignKey(
        SubCategories, default='', blank=False, on_delete=models.CASCADE)

    price = models.IntegerField()
    stock = models.IntegerField()
    brand = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=200, default='')
    image = models.ImageField(
        default='./default/placeholder.webp', upload_to=image_upload_to, max_length=5000)
    is_active = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_detail', args=[self.series.series.slug_cate, self.series.slug_sub, self.slug_prod])

    class Meta:
        verbose_name_plural = 'Products'
