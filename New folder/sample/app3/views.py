from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home3(request):
    return HttpResponse('<h1>Home page app3</h1>')

def about3(request):
    return HttpResponse('<h1>About page app3</h1>')