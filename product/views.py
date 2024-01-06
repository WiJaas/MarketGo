from django.shortcuts import render
from . models import Product







def home_view(request):
    # Retrieve products from both concrete model tables
    products = Product.objects.all()
    context = {'products': products}
    # return render(request, 'home.html', context)
    return render(request, 'home.html',context)


