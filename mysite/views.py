from django.shortcuts import render
from .models import Categories, Products
# Create your views here.
def homepage(request):
    
    categories = Categories.objects.all()
    products = Products.objects.all()
    data = {
        'categories': categories,
        'products': products
    }
    return render(request, 'index.html', data)