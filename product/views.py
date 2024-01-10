import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.urls import reverse
from .models import Product  # Assuming your Product model is in the same app

def home_view(request):

    return render(request, 'home.html')

def scan_view(request):
    return render(request,'scan_logic.html')


def search_product(request):
    product = None
    if request.method == "POST":
        try: #for getting barcode from the post request
            data = json.loads(request.body.decode('utf-8'))
            barcode = data.get('barcode') 
            # Store the barcode in the session
            request.session['barcode'] = barcode
            product = Product.objects.get(barcode=barcode)
            # Attempt to return the product if he exist 
            if product: 
                product_data = serialize('json', [product])
                return JsonResponse({'success': True, 'product': product_data})
        except Product.DoesNotExist:
            print("the problem is here")
            return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)


        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)

    elif request.method == "GET":
        barcode = request.session.get('barcode', None)

        if barcode is not None:
            try:
                # Attempt to find the product by barcode
                product = Product.objects.get(barcode=barcode)

                # Render search.html with product details
                context = {'product': product}
                return render(request, 'search.html', context)

            except Product.DoesNotExist:
                   # Handle the case when the product is not found, redirect to search.html with a parameter indicating the absence of the product
                    answer= {'product_not_found': True}
                    return render(request, 'search.html', answer)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)




















# # Redirect function (assuming you want to redirect after some other operation)
# def redirect_to_search(request, barcode):
#     try:
#         product = Product.objects.get(barcode=barcode)
#         return redirect('search_product', {'product': product})
#     except Product.DoesNotExist:
#         return render(request, 'search.html', {'error': 'Product not found'})







        




# # def search_product(request):
# #     product = None

# #     if 'barcode' in request.GET:
# #         barcode = request.GET['barcode']
# #         try:
# #             # Attempt to find the product by barcode
# #             product = Product.objects.get(barcode=barcode)
# #         except Product.DoesNotExist:
# #             # Product not found
# #             pass

# #     return render(request, 'home.html', {'product': product})


