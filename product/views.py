

# views.py
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

def search_product(request):
    product = None

    if 'barcode' in request.GET:
        barcode = request.GET['barcode']
        try:
            # Attempt to find the product by barcode
            product = Product.objects.get(barcode=barcode)
        except Product.DoesNotExist:
            # Product not found
            pass

    return render(request, 'home.html', {'product': product})








# from django.shortcuts import render
# from . models import Product

# def home_view(request):
#     # Retrieve products from both concrete model tables
#     products = Product.objects.all()
#     context = {'products': products}
#     # return render(request, 'home.html', context)
#     return render(request, 'home.html',context)