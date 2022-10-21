from django.contrib import admin
from .models import Blog, Category, Customer, Deneme12

class N11Admin(admin.ModelAdmin):
    list_display = ("Fiyat","Marka",)
    

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home",)
    list_filter = ("is_active","is_home","category",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Deneme12)