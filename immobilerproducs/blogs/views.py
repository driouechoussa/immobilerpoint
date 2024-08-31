from django.shortcuts import render
from .models import Blog_table
# Create your views here.

pageTitle = 'Blogs'

def blogslayout(request):
    return render(request , 'layouts/blogs.html')