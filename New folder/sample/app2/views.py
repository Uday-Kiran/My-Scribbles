from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home2(request):
    return HttpResponse('<h1>Home page app2</h1>')

def about2(request):
    return HttpResponse('<h1>About page app2</h1>')
