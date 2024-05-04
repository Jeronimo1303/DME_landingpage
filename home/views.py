from django.http import HttpResponse
from django.shortcuts import render
from .forms import new_search

# Create your views here.
def index(request):
    title = 'Django webpage'
    return render(request, 'index.html')

def hello(request):
    return HttpResponse("<h1>hello world</h1>")

def about(request):
    return render(request, 'about.html')

def search(request):
    print(request.GET)
    return render(request, 'search.html',{
        'form' : new_search()
    })

