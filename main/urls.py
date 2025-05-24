from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('contacts', views.contacts, name='contacts'),
]