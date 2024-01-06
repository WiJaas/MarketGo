
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pro/',include('store.urls')),
    path('',include('product.urls')),
]
