from django.shortcuts import render
from .models import Category, DataSetDeneme

# Create your views here.

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": DataSetDeneme.objects.all()
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
        "kategoriler": Category.objects.all(),
        "filmler": DataSetDeneme.objects.all()
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "laptoplar": DataSetDeneme.objects.get(id=id)
    }
    return render(request, "details.html", data)