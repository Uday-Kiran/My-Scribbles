from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home2),
    path('about_app2', views.about2),
]