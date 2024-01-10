from django.shortcuts import render


def cart_view(request):
    return render(request, "cart_view.html", {})
    
def cart_add(request):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass