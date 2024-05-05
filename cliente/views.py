from django.shortcuts import render
from cliente.models import empresa

# Create your views here.

def cliente(request):
    products_queryset = empresa.objects.all()
    context = {
        'Empresas': products_queryset
    }
    print(context)
    return render(request,'cliente.html',context)