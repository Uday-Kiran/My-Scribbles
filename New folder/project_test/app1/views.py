from django.shortcuts import render
from django.http import HttpResponse

a = {'titles': ['1','2','3','4'] }
# Create your views here.
def home_page(request):
    # return HttpResponse('<h1>Project home page 1</h1>')
    return render(request,"app1/home.html", {'titles': ['1','2','3','4'] })

def about_page(request):
    # return HttpResponse('<h1>Project home page 1</h1>')
    return render(request,"app1/about.html", a)

