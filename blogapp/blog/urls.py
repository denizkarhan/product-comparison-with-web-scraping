from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index, name="home"),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<int:id>", views.blogdetails, name="blog_details"),
]