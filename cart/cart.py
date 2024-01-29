from django.conf import settings
from product.models import Product
from decimal import Decimal


class Cart(object):
    def __init__(self,request):
        # Initialize Cart

        self.session = request.session
        
        self.cart = self.session.setdefault(settings.CART_SESSION_ID, {})



    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)

        price = '{:.2f}'.format(float(product.price))

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price}

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            if product.category == 'unit':
                self.cart[product_id]['quantity'] += quantity
            elif product.category == 'weight' and self.cart[product_id]['quantity'] == 0:
                # Only add the weight-based product if it hasn't been added before
                self.cart[product_id]['quantity'] += quantity

        self.save()


    
    

    
    def save(self):
        self.session.modified = True
    

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for prod in products:
            product_id= str(prod.id)
            if prod is None:
                raise ValueError("Product object is None")
            cart[str(prod.id)]['product'] = prod
        #     print(f"Product {product_id} added to cart with name {prod.name}")
            cart[product_id]['category'] = prod.category 


        # print("Cart dictionary:", cart)  # Debug: Print cart dictionary to console

        for item in cart.values():
            item['price']=Decimal(item['price'])
            #Calculate total price for an item 
            item['total_price'] = item['price'] * item['quantity']
            item['category'] = item['category']  # Use get method to avoid KeyError

            yield item


    #Returns the total of items in cart 
    def __len__(self):
        return sum(item['quantity']for item in self.cart.values())
    
    #Calculate total price for the cart
    def get_total_price(self):
        return sum(Decimal(item['price'] *item['quantity'])for item in self.cart.values())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def update_quantity(self, product_id, quantity_change):
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity_change


            if self.cart[product_id]['quantity'] <= 0:
                # Remove the product if the quantity becomes zero or negative
                del self.cart[product_id]

            self.save()