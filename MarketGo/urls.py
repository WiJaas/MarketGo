
from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('product.urls')),
    path('core/',include('core.urls')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('checkout/',include('checkout.urls')),
    path('paypal/',include('paypal.standard.ipn.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

