from django.shortcuts import render
from .models import Category, DataSetDeneme, Data, Data2, Data3

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
        "notebooklar": Data3.objects.all(),
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "laptoplar": Data3.objects.get(id=id)
    }
    return render(request, "details.html", data)

def magazadetails(request):
    data = {
        "laptoplar": Data3.objects.all(),
    }
    return render(request, "magaza.html", data)
