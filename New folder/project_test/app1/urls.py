from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name = 'home-1'),
    path('about/',views.about_page,name = 'about-1')
]