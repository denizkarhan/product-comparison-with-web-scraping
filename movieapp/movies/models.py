from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
     
class DataSet(models.Model):
    id = models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID')
    Marka = models.CharField(max_length=200, null=True)
    ModelAdi = models.CharField(max_length=200, null=True)
    Modelno = models.CharField(max_length=200, null=True)
    İşletimSistemi = models.CharField(max_length=200, null=True)
    İslemciTipi = models.CharField(max_length=200, null=True)
    İslemciNesli = models.CharField(max_length=200, null=True)
    Ram = models.CharField(max_length=200, null=True)
    DiskBoyutu = models.CharField(max_length=200, null=True)
    DiskTürü = models.CharField(max_length=200, null=True)
    EkranBoyutu = models.CharField(max_length=200, null=True)
    Puanı = models.CharField(max_length=200, null=True)
    Fiyat = models.CharField(max_length=200, null=True)
    Siteİsmi = models.CharField(max_length=200, null=True)
    SiteLinki = models.CharField(max_length=200, null=True)

class DataSetDeneme(models.Model):
    id = models.BigIntegerField(primary_key=True, serialize=False, verbose_name='ID')
    Marka = models.CharField(max_length=200, null=True)
    ModelAdi = models.CharField(max_length=200, null=True)
    Modelno = models.CharField(max_length=200, null=True)
    İşletimSistemi = models.CharField(max_length=200, null=True)
    İslemciTipi = models.CharField(max_length=200, null=True)
    İslemciNesli = models.CharField(max_length=200, null=True)
    Ram = models.CharField(max_length=200, null=True)
    DiskBoyutu = models.CharField(max_length=200, null=True)
    DiskTürü = models.CharField(max_length=200, null=True)
    EkranBoyutu = models.CharField(max_length=200, null=True)
    Puanı = models.CharField(max_length=200, null=True)
    Fiyat = models.CharField(max_length=200, null=True)
    Siteİsmi = models.CharField(max_length=200, null=True)
    SiteLinki = models.CharField(max_length=200, null=True)


