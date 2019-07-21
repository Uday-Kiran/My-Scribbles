from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Home</h1>")
    return render(request,"blog/index.html")

def about(request):
    return HttpResponse("<h1>About</h1>")    

def blog(request):
    return render(request, 'blog/blog.html' )        