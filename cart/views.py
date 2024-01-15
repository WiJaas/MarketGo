
# views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from .models import Cart, CartItem
from product.models import Product
from django.contrib.auth import authenticate, login



class CartHomeView(LoginRequiredMixin, View):
    # def get(self, request):
    #     return render(request, "cart_home.html", {})

    template_name = 'cart_home.html'
    login_url = '/core/login/'

    def get(self, request, *args, **kwargs):
        user_cart = Cart.objects.get_or_create(user=request.user)[0]
        cart_items = CartItem.objects.filter(cart=user_cart)

        context = {
            'cart': user_cart,
            'cart_items': cart_items,
        }

        return render(request, self.template_name, context)



class AddToCartView(LoginRequiredMixin, View):
    
    login_url = '/core/login/'

    def post(self, request, barcode):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            quantity = int(request.POST.get('quantity', 1))
            product = get_object_or_404(Product, barcode=barcode)
            print(product)


            # Access the customer instance from the logged-in user
            customer_instance = request.user
            print(customer_instance)


            # Get or create the cart associated with the customer
            cart, created = Cart.objects.get_or_create(user=request.user)
            

            # Check if the product is already in the cart
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})

            if not created:
                # If the item is already in the cart, update the quantity
                cart_item.quantity += quantity
                cart_item.save()

            return redirect('cart:cart_home')  # Replace with the actual cart home URL
        else:
            # Redirect to the login page if the user is not authenticated
            return redirect('core:login')  # Replace with the actual login URL






