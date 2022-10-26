from xml.sax.handler import all_features
from django.shortcuts import render
from .models import Category, DataSetDeneme, Data, Data2, Data4, Data
from django.db.models import Q


def home(request):
    query = request.GET.get('q')
    if query:
        filter = Data4.objects.filter(
        Q(Marka__icontains=query) | Q(Siteİsmi1__icontains=query) 
        | Q(Siteİsmi1__icontains=query) | Q(Siteİsmi2__icontains=query)
        | Q(Siteİsmi3__icontains=query) | Q(Siteİsmi4__icontains=query)
        | Q(ModelAdi__icontains=query) | Q(Modelno__icontains=query)
        | Q(İşletimSistemi__icontains=query) | Q(İslemciTipi__icontains=query)
        | Q(İslemciNesli__icontains=query) | Q(Ram__icontains=query)
        | Q(DiskBoyutu__icontains=query) | Q(DiskTürü__icontains=query)
        ).distinct()
    else:
        filter = Data4.objects.all()
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": filter
    }
    return render(request, "index.html", data)

def movies(request):

    context = dict()

    query = request.GET.get('q')
    if query:
           filter = Data4.objects.filter(
           Q(Marka__icontains=query) | Q(Siteİsmi1__icontains=query) 
           | Q(Siteİsmi1__icontains=query) | Q(Siteİsmi2__icontains=query)
           | Q(Siteİsmi3__icontains=query) | Q(Siteİsmi4__icontains=query)
           | Q(ModelAdi__icontains=query) | Q(Modelno__icontains=query)
           | Q(İşletimSistemi__icontains=query) | Q(İslemciTipi__icontains=query)
           | Q(İslemciNesli__icontains=query) | Q(Ram__icontains=query)
           | Q(DiskBoyutu__icontains=query) | Q(DiskTürü__icontains=query)
        ).distinct()
    else:
        filter = Data4.objects.all()
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": filter,
        "laptoplarram": Data4.objects.filter(Ram="8 GB")     
    }
    data2 = {
        
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "laptoplar": Data4.objects.get(id=id),
        
    }
    
    return render(request, "details.html", data)

def magazadetails(request):
    data = {
        "laptoplar": Data4.objects.all(),
    }
    return render(request, "magaza.html", data)
