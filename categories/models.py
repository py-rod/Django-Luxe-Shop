from django.db import models

# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    slug_cate = models.SlugField(default='', blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
