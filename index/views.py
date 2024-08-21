from django.shortcuts import render, redirect
from .models import ImagesSlider
# Create your views here.


def index(request):
    slider_imgs = ImagesSlider.objects.filter(active=True)

    return render(request, 'index.html', {
        'images': slider_imgs
    })
