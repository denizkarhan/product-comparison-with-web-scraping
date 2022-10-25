from importlib.resources import path
from unicodedata import name


from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="magazahome"),
    path("magazahome", views.home, name="magazahome"),
    path("magaza", views.items, name="magaza"),
    path("magaza/<int:id>", views.itemdetails, name="details1")
]