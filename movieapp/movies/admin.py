from django.contrib import admin
from .models import Category, DataSetDeneme, Data, Data2, Data3

# Register your models here.

admin.site.register(DataSetDeneme)
admin.site.register(Category)
admin.site.register(Data)
admin.site.register(Data2)
admin.site.register(Data3)