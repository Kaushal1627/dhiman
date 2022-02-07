
from unicodedata import name
from django import views
from django.urls import path
from .import views

urlpatterns = [

    path('', views.index,name='index'),
    path('contact', views.contact,name='contact'),
    path('product', views.product,name='product'),
    path('blog', views.blog,name="blog"),
    
]
