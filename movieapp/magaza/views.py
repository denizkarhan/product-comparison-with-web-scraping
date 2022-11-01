from dataclasses import dataclass
from django.shortcuts import render
from .models import Category, Data3, Data, magaza
from django.db.models import Q

# Create your views here.

def home(request):
    query = request.GET.get('q')
    if query:
        filter = magaza.objects.filter(
        Q(Marka__icontains=query) | Q(Siteİsmi1__icontains=query) 
        | Q(Siteİsmi1__icontains=query) | Q(Siteİsmi2__icontains=query)
        | Q(Siteİsmi3__icontains=query) | Q(Siteİsmi4__icontains=query)
        | Q(ModelAdi__icontains=query) | Q(Modelno__icontains=query)
        | Q(İşletimSistemi__icontains=query) | Q(İslemciTipi__icontains=query)
        | Q(İslemciNesli__icontains=query) | Q(Ram__icontains=query)
        | Q(DiskBoyutu__icontains=query) | Q(DiskTürü__icontains=query)
        ).distinct()
    else:
        filter = magaza.objects.all()
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": filter
    }
    if query:
        return render(request, "magaza.html", data)
    else:
        return render(request, "magazahome.html", data)

def items(request):

    query = request.GET.get('q')
    if query:
           filter = magaza.objects.filter(
           Q(Marka__icontains=query) | Q(Siteİsmi1__icontains=query) 
           | Q(Siteİsmi1__icontains=query) | Q(Siteİsmi2__icontains=query)
           | Q(Siteİsmi3__icontains=query) | Q(Siteİsmi4__icontains=query)
           | Q(ModelAdi__icontains=query) | Q(Modelno__icontains=query)
           | Q(İşletimSistemi__icontains=query) | Q(İslemciTipi__icontains=query)
           | Q(İslemciNesli__icontains=query) | Q(Ram__icontains=query)
           | Q(DiskBoyutu__icontains=query) | Q(DiskTürü__icontains=query)
        ).distinct()
    else:
        filter = magaza.objects.all()
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": filter,    
    }
    data2 = {
        
    }
    return render(request, "magaza.html", data)

def itemdetails(request, id):
    data = {
        "laptoplar": magaza.objects.get(id=id)
    }
    return render(request, "magazadetails.html", data)
