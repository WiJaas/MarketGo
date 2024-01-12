import json
from django.http import JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Product

class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        barcode = request.GET.get('barcode')
        product = None

        if barcode:
            try:
                product = Product.objects.get(barcode=barcode)
            except Product.DoesNotExist:
                pass

        context = {'product': product}
        return render(request, self.template_name, context)

class ScanView(View):
    template_name = 'scan_logic.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SearchProductView(View):
    template_name = 'search.html'

    @csrf_exempt
    def post(self, request, *args, **kwargs):
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
            return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)

    def get(self, request, *args, **kwargs):
        barcode = request.session.get('barcode')

        if barcode is not None:
            try:
                # Attempt to find the product by barcode
                product = Product.objects.get(barcode=barcode)
                context = {'product': product}
            except Product.DoesNotExist:
                # Handle the case when the product is not found, redirect to search.html with a parameter indicating the absence of the product
                context = {'product_not_found': True}

            return render(request, self.template_name, context)

        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)
