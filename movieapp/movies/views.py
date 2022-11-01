from xml.sax.handler import all_features
from django.shortcuts import render
from .models import Category, DataSetDeneme, Data, Data2, Data4, Data3, Data6
from django.db.models import Q

def home(request):
    query = request.GET.get('q')

    if query:
        filter = Data6.objects.filter(
        Q(Marka__icontains=query) | Q(Siteİsmi1__icontains=query) 
        | Q(Siteİsmi1__icontains=query) | Q(Siteİsmi2__icontains=query)
        | Q(Siteİsmi3__icontains=query) | Q(Siteİsmi4__icontains=query)
        | Q(ModelAdi__icontains=query) | Q(Modelno__icontains=query)
        | Q(İşletimSistemi__icontains=query) | Q(İslemciTipi__icontains=query)
        | Q(İslemciNesli__icontains=query) | Q(Ram__icontains=query)
        | Q(DiskBoyutu__icontains=query) | Q(DiskTürü__icontains=query)
        ).distinct()
    else:
        filter = Data6.objects.all()
    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": Data6.objects.filter(id=1) | Data6.objects.filter(id=2)
    }
    if query:
        return render(request, "movies.html", data)
    else:
        return render(request, "index.html", data)

def movies(request):
    query = request.GET.get('q')
    fruits = []

    filter = Data6.objects.all()

    if query:
        filter = Data6.objects.filter(
        Q(Marka__icontains=query) | Q(Siteİsmi1__icontains=query) 
        | Q(Siteİsmi1__icontains=query) | Q(Siteİsmi2__icontains=query)
        | Q(Siteİsmi3__icontains=query) | Q(Siteİsmi4__icontains=query)
        | Q(ModelAdi__icontains=query) | Q(Modelno__icontains=query)
        | Q(İşletimSistemi__icontains=query) | Q(İslemciTipi__icontains=query)
        | Q(İslemciNesli__icontains=query) | Q(Ram__icontains=query)
        | Q(DiskBoyutu__icontains=query) | Q(DiskTürü__icontains=query)
        ).distinct()

    
    if request.method == 'POST':
       fruits = request.POST.getlist('fruits')
    
    T = []
    a = 0
    x = ""
    for i in range(len(fruits)):
        T.append(fruits[i])
        x = fruits[i]
    l = len(T)
    for j in range(l, 6):
        T.append(x)
    print(T)
    if fruits:
        a = filter.filter((Q(Marka__icontains=T[0])
                             | Q(Marka__icontains=T[1])
                             | Q(Marka__icontains=T[2])
                             | Q(Marka__icontains=T[3])
                             | Q(Marka__icontains=T[4]))).distinct()
        b = filter.filter((Q(Ram__icontains=T[0])
                             | Q(Ram__icontains=T[1])
                             | Q(Ram__icontains=T[2])
                             | Q(Ram__icontains=T[3])
                             | Q(Ram__icontains=T[4]))).distinct()

        c = filter.filter(Q(İslemciTipi__icontains=T[0])
                             | Q(İslemciTipi__icontains=T[1])
                             | Q(İslemciTipi__icontains=T[2])
                             | Q(İslemciTipi__icontains=T[3])
                             | Q(İslemciTipi__icontains=T[4])).distinct()

        d = filter.filter(Q(DiskBoyutu__icontains=T[0])
                             | Q(DiskBoyutu__icontains=T[1])
                             | Q(DiskBoyutu__icontains=T[2])
                             | Q(DiskBoyutu__icontains=T[3])
                             | Q(DiskBoyutu__icontains=T[4])).distinct()
        
        if(len(a)>0 and len(b)>0 and len(c)>0 and len(d)>0):
            filter = a & b & c & d
        elif(len(a)>0 and len(b)>0 and len(c)>0):
            filter = a & b & c
        elif(len(a)>0 and len(b)>0 and len(d)>0):
            filter = a & b & d
        elif(len(a)>0 and len(c)>0 and len(d)>0):
            filter = a & c & d
        elif(len(a)>0 and len(b)>0):
            filter = a & b
        elif(len(a)>0 and len(c)>0):
            filter = a & c
        elif(len(a)>0 and len(d)>0):
            filter = a & d
        elif(len(b)>0 and len(c)>0 and len(d)>0):
            filter = b & c & d
        elif(len(b)>0 and len(c)>0):
            filter = b & c
        elif(len(b)>0 and len(d)>0):
            filter = b & d
        elif(len(a)>0):
            filter = a
        elif(len(b)>0):
            filter = b
        elif(len(c)>0):
            filter = c
        elif(len(d)>0):
            filter = d

    if "ucuz" in T:
        filter = filter.order_by('Fiyat1')
    if "pahalı" in T:
        filter = filter.order_by('-Fiyat1')
    if "puanlı" in T:
        filter = filter.order_by('-Puanı1')
    if "puansız" in T:
        filter = filter.order_by('Puanı1')

    data = {
        "kategoriler": Category.objects.all(),
        "notebooklar": filter
        }
    return render(request, "movies.html", data)

def moviedetails(request, id):
    data = {
        "laptoplar": Data6.objects.get(id=id),
        
    }
    
    return render(request, "details.html", data)

def magazadetails(request):
    data = {
        "laptoplar": Data6.objects.all(),
    }
    return render(request, "magaza.html", data)
