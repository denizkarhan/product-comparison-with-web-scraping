from email.mime import image
from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField()
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Deneme12(models.Model):
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
    