from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
post = [{
    'name':'random',
    'age':'infinity',
    'interest':'nothing',
    'address':'unknown',
    'schooling':'boring school'
},{
    'name1':'random12',
    'age':'infinity',
    'interest':'nothing',
    'address':'unknown',
    'schooling':'boring school'
}]

# title = {"abt"
def home(request):

    context = {
        'post' : post,
    }
    # return HttpResponse('<h1>Home page</h1>')
    return render(request,"sampleapp/home.html", context)


def about(request):
    context = {
        'post' : post,
    }
    # return HttpResponse('<h1>About page</h1>')
    return render(request,"sampleapp/about.html", {'title' : 'Abt'})