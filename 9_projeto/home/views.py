from django.shortcuts import render
from .forms import ContatoForm

def index(request):
    return render(request, 'home/index.html')

def contato(request):
    form = ContatoForm()
    context = {
        'form':form 
    }
    return render(request, 'home/contato.html', context)

def produto(request):
    return render(request, 'home/produto.html')