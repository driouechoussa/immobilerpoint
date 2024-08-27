from django.shortcuts import render

# Create your views here.

def Immobilerproducts(request):
    return render(request , 'layouts/products.html')