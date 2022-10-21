from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog, Deneme12, Category
import pymongo



# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True)
        #"categories": Category.objects.all()
    }
    return render(request, "index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.all
    }
    return render(request, "blogs.html", context)

def blogdetails(request,id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/blogdetails.html", {
    "blog": blog
    }
    )



"""
def blogs_by_category(request, slug):
    context = {
        "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all()
    }
    return render(request, "blogs.html", context)
"""