from django.shortcuts import render
from immobilerproducs.models import immobiler_Products
from blogs.models import Blog_table

# Create your views here.

pageTitle = 'Accueil'
immobilerProducts = immobiler_Products.objects.all()
blogs_table = Blog_table.objects.all()
Context = {
    'pageTitle':pageTitle,
    'immobiler_Products':immobilerProducts,
    'products_types': immobiler_Products.products_type,
    'products_location':immobiler_Products.products_location,
    'blogsInfo':blogs_table,
    }   
   

def Home(request):

    return render(request , 'index.html',Context)


   


