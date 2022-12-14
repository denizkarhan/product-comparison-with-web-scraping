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

class Data(models.Model):
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
    Puanı1 = models.CharField(max_length=200, null=True)
    Fiyat1 = models.CharField(max_length=200, null=True)
    Siteİsmi1 = models.CharField(max_length=200, null=True)
    SiteLinki1 = models.CharField(max_length=200, null=True)
    Puanı2 = models.CharField(max_length=200, null=True)
    Fiyat2 = models.CharField(max_length=200, null=True)
    Siteİsmi2 = models.CharField(max_length=200, null=True)
    SiteLinki2 = models.CharField(max_length=200, null=True)

class Data2(models.Model):
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
    Puanı1 = models.BigIntegerField(null=True)
    Fiyat1 = models.BigIntegerField(null=True)
    Siteİsmi1 = models.CharField(max_length=200, null=True)
    SiteLinki1 = models.CharField(max_length=200, null=True)
    Puanı2 = models.BigIntegerField(null=True)
    Fiyat2 = models.BigIntegerField(null=True)
    Siteİsmi2 = models.CharField(max_length=200, null=True)
    SiteLinki2 = models.CharField(max_length=200, null=True)

class Data3(models.Model):
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
    Puanı1 = models.BigIntegerField(null=True)
    Fiyat1 = models.BigIntegerField(null=True)
    Siteİsmi1 = models.CharField(max_length=200, null=True)
    SiteLinki1 = models.CharField(max_length=200, null=True)
    Puanı2 = models.BigIntegerField(null=True)
    Fiyat2 = models.BigIntegerField(null=True)
    Siteİsmi2 = models.CharField(max_length=200, null=True)
    SiteLinki2 = models.CharField(max_length=200, null=True)
    Puanı3 = models.BigIntegerField(null=True)
    Fiyat3 = models.BigIntegerField(null=True)
    Siteİsmi3 = models.CharField(max_length=200, null=True)
    SiteLinki3 = models.CharField(max_length=200, null=True)
    Puanı4 = models.BigIntegerField(null=True)
    Fiyat4 = models.BigIntegerField(null=True)
    Siteİsmi4 = models.CharField(max_length=200, null=True)
    SiteLinki4 = models.CharField(max_length=200, null=True)
    Puanı5 = models.BigIntegerField(null=True)
    Fiyat5 = models.BigIntegerField(null=True)
    Siteİsmi5 = models.CharField(max_length=200, null=True)
    SiteLinki5 = models.CharField(max_length=200, null=True)
    İmageLink = models.CharField(max_length=200, null=True)

class Data4(models.Model):
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
    Puanı1 = models.BigIntegerField(null=True)
    Fiyat1 = models.BigIntegerField(null=True)
    Siteİsmi1 = models.CharField(max_length=200, null=True)
    SiteLinki1 = models.CharField(max_length=200, null=True)
    Title1 = models.CharField(max_length=200, null=True)
    Puanı2 = models.BigIntegerField(null=True)
    Fiyat2 = models.BigIntegerField(null=True)
    Siteİsmi2 = models.CharField(max_length=200, null=True)
    SiteLinki2 = models.CharField(max_length=200, null=True)
    Title2 = models.CharField(max_length=200, null=True)
    Puanı3 = models.BigIntegerField(null=True)
    Fiyat3 = models.BigIntegerField(null=True)
    Siteİsmi3 = models.CharField(max_length=200, null=True)
    SiteLinki3 = models.CharField(max_length=200, null=True)
    Title3 = models.CharField(max_length=200, null=True)
    Puanı4 = models.BigIntegerField(null=True)
    Fiyat4 = models.BigIntegerField(null=True)
    Siteİsmi4 = models.CharField(max_length=200, null=True)
    SiteLinki4 = models.CharField(max_length=200, null=True)
    Title4 = models.CharField(max_length=200, null=True)
    Puanı5 = models.BigIntegerField(null=True)
    Fiyat5 = models.BigIntegerField(null=True)
    Siteİsmi5 = models.CharField(max_length=200, null=True)
    SiteLinki5 = models.CharField(max_length=200, null=True)
    Title5 = models.CharField(max_length=200, null=True)
    İmageLink = models.CharField(max_length=200, null=True)
    
class Data6(models.Model):
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
    Puanı1 = models.BigIntegerField(null=True)
    Fiyat1 = models.BigIntegerField(null=True)
    Siteİsmi1 = models.CharField(max_length=200, null=True)
    SiteLinki1 = models.CharField(max_length=200, null=True)
    Title1 = models.CharField(max_length=200, null = True)
    Puanı2 = models.BigIntegerField(null=True)
    Fiyat2 = models.BigIntegerField(null=True)
    Siteİsmi2 = models.CharField(max_length=200, null=True)
    SiteLinki2 = models.CharField(max_length=200, null=True)
    Title2 = models.CharField(max_length=200, null = True)
    Puanı3 = models.BigIntegerField(null=True)
    Fiyat3 = models.BigIntegerField(null=True)
    Siteİsmi3 = models.CharField(max_length=200, null=True)
    SiteLinki3 = models.CharField(max_length=200, null=True)
    Title3 = models.CharField(max_length=200, null = True)
    Puanı4 = models.BigIntegerField(null=True)
    Fiyat4 = models.BigIntegerField(null=True)
    Siteİsmi4 = models.CharField(max_length=200, null=True)
    SiteLinki4 = models.CharField(max_length=200, null=True)
    Title4 = models.CharField(max_length=200, null = True)
    Puanı5 = models.BigIntegerField(null=True)
    Fiyat5 = models.BigIntegerField(null=True)
    Siteİsmi5 = models.CharField(max_length=200, null=True)
    SiteLinki5 = models.CharField(max_length=200, null=True)
    Title5 = models.CharField(max_length=200, null = True)
    İmageLink = models.CharField(max_length=200, null=True)