from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home3),
    path('about_app3', views.about3),
]