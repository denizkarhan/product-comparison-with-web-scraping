from xml.sax.handler import all_features
from django.shortcuts import render
from .models import Category, DataSetDeneme, Data, Data2, Data4, Data3
from django.db.models import Q


def home(request):
    query = request.GET.get('q')
    if query:
        filter = Data3.objects.filter(
        Q(Marka__icontains=query) | Q(Siteİsmi1__icontains=query) 
        | Q(Siteİsmi1__icontains=query) | Q(Siteİsmi2__icontains=query)
        | Q(Siteİsmi3__icontains=query) | Q(Siteİsmi4__icontains=query)
        | Q(ModelAdi__icontains=query) | Q(Modelno__icontains=query)
        | Q(İşletimSistemi__icontains=query) | Q(İslemciTipi__icontains=query)
        | Q(İslemciNesli__icontains=query) | Q(Ram__icontains=query)
        | Q(DiskBoyutu__icontains=query) | Q(DiskTürü__icontains=query)
        ).distinct()
    else:
        filter = Data3.objects.all()
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": filter
    }
    if query:
        return render(request, "movies.html", data)
    else:
        return render(request, "index.html", data)

def movies(request):

    context = dict()

    queryy = request.GET.get('q')
    query = ["MSI", "16 GB",]
    filter = Data3.objects.all()
    if query:   
        for i in query:       
           filter = filter.filter(
           Q(Marka__icontains=i) | Q(Siteİsmi1__icontains=i) 
           | Q(Siteİsmi1__icontains=i) | Q(Siteİsmi2__icontains=i)
           | Q(Siteİsmi3__icontains=i) | Q(Siteİsmi4__icontains=i)
           | Q(ModelAdi__icontains=i) | Q(Modelno__icontains=i)
           | Q(İşletimSistemi__icontains=i) | Q(İslemciTipi__icontains=i)
           | Q(İslemciNesli__icontains=i) | Q(Ram__icontains=i)
           | Q(DiskBoyutu__icontains=i) | Q(DiskTürü__icontains=i)
        ).distinct()
    else:
        filter = Data3.objects.all()
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": filter,    
    }
    data2 = {
        
    }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "laptoplar": Data3.objects.get(id=id),
        
    }
    
    return render(request, "details.html", data)

def magazadetails(request):
    data = {
        "laptoplar": Data3.objects.all(),
    }
    return render(request, "magaza.html", data)
