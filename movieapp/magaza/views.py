from dataclasses import dataclass
from django.shortcuts import render
from .models import Category, Data3, Data

# Create your views here.

def home(request):
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": Data.objects.all()
    }
    return render(request, "magazahome.html", data)

def items(request):
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": Data.objects.all(),
    }
    return render(request, "magaza.html", data)

def itemdetails(request, id):
    data = {
        "laptoplar": Data.objects.get(id=id)
    }
    return render(request, "magazadetails.html", data)
