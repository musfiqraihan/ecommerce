from django.shortcuts import render
from .models import *


def home_page(request):
    return render(request, 'home-page.html')


def product_page(request):
    return render(request, 'product-page.html')


def checkout_page(request):
    return render(request, 'checkout-page.html')
