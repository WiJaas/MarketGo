
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
            product.update_stock(quantity_change=cd['quantity'])
       
        return redirect('cart:cart_detail')


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        print(cart.cart)
        return render(request, 'cart_detail.html', {'cart': cart})



class CartRemoveView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')
    


class CartUpdateQuantityView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        action = request.POST.get('action')

        if action == 'increase':
            cart.update_quantity(product_id, 1)
            quantity_change= 1
        elif action == 'decrease':
            cart.update_quantity(product_id, -1)
            quantity_change= -1
            # Update stock_quantity in the Product model

        product = Product.objects.get(id=product_id)

        product.update_stock(quantity_change)

        return redirect('cart:cart_detail') 



















