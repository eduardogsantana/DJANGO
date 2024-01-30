from django.shortcuts import render
from .models import AlugarCarro
from django.contrib import messages
from .forms import AlugarCarroForm

def index(request):
    alugar_carros = AlugarCarro.objects.all()
    return  render(request, 'home/index.html', {'alugar_carros': alugar_carros})

def cadastro(request):
    if request.method == 'POST':
        form = AlugarCarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro Realizado com Sucesso.')
            form = AlugarCarroForm()
        else:
            messages.error(request, 'Erro ao Cadastrar Cliente.')
    else:
        form = AlugarCarroForm

    return render(request, 'home/cadastro.html', {'form': form})