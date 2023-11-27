from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import product, category


# Create your views here.

def allproducts(request, slug_c=None):
    page_c = None
    products = None
    if slug_c != None:
        page_c = get_object_or_404(category, slug=slug_c)

        products = product.objects.all().filter(category=page_c, available=True)
    else:

        products = product.objects.all().filter(available=True)

    return render(request, 'tem1.html', {'category': page_c, 'products': products})


def pro_duct(request, slug_c, slug_p):
    try:
        Product = product.objects.get(category__slug=slug_c, slug=slug_p)
    except Exception as e:
        raise e
    return render(request, 'products.html', {'product': Product})
