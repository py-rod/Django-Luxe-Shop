from django.db import models
from categories.models import Categories
from django.urls import reverse
# Create your models here.


class SubCategories(models.Model):
    title = models.CharField(max_length=100, blank=False, unique=True)
    series = models.ForeignKey(
        Categories, default='', blank=False, on_delete=models.CASCADE)
    slug_sub = models.SlugField(default='', unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sub Categories'

    def __str__(self):
        return self.title

    def get_products_of_the_subcategory(self):
        return reverse('products_of_the_subcategory', args=[self.series.slug_cate, self.slug_sub])
