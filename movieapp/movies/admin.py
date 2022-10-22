from django.contrib import admin
from .models import Category, DataSetDeneme

# Register your models here.

admin.site.register(DataSetDeneme)
admin.site.register(Category)