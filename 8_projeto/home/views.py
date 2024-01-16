from django.shortcuts import render
from django.http import HttpResponse
from .models import Livros

def home(request):
    meus_livros = Livros.objects.all()
    context = {
        'livros': meus_livros,
    }
    return render(request, 'home/index.html', context)