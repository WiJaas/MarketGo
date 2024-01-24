
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CartAddProductForm
from .cart import Cart
from product.models import Product


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)

        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
           
            cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
       
        return redirect('cart:cart_detail')


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart_detail.html', {'cart': cart})




class CartRemoveView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')


























