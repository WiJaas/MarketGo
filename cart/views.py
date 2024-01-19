
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
            print(f"Adding product {product_id} to cart with quantity {cd['quantity']}, override: {cd['override']}")
            cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        print("Heyy###############",cart.cart)
        return redirect('cart:cart_detail')


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        print("Cart data in view:", cart.cart)  # Debug: Print cart data to console
        return render(request, 'cart_detail.html', {'cart': cart})




class CartRemoveView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')































# from .forms import CartAddProductForm
# from .cart import Cart

# from django.shortcuts import redirect, render, get_object_or_404
# from product.models import Product
# from django.views.decorators.http import require_POST


# @require_POST
# def cart_add(request , product_id):
#     cart = Cart(request)
#     print(product_id)
#     product =  get_object_or_404(Product,id=product_id)
#     print(product)
#     form = CartAddProductForm(request.POST)
#     print(form)
#     if form.is_valid():
#         cd= form.cleaned_data
#         cart.add(product=product , quantity=cd['quantity'], override_qunatity=cd['override'])
#     return redirect('cart:cart_detail')

# def cart_remove(request,product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart:cart_detail')

# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'cart_detail.html' , {'cart':cart})