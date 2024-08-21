from django.db import models
import os
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
# Create your models here.


class ImagesSlider(models.Model):

    def image_upload_to(self, instance):
        if instance:
            return os.path.join('Slider_images', instance)
        return None

    def validate_image_count(self):
        image_count = ImagesSlider.objects.all().count()
        if image_count >= 3:
            raise ValidationError(
                "Only three images can be selected. If you need to change select image, you need to delete one select image and select the new image ")

    title = models.CharField(max_length=100, unique=True, blank=False)
    image = models.ImageField(
        upload_to=image_upload_to, default='', blank=False)
    date_upload = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
