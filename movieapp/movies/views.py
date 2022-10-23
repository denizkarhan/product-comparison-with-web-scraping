from django.shortcuts import render
from .models import Category, DataSetDeneme, Data, Data2

# Create your views here.

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": Data2.objects.all()
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": Data2.objects.all(),
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "laptoplar": Data2.objects.get(id=id)
    }
    return render(request, "details.html", data)