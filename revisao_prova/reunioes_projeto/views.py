from django.shortcuts import render, redirect
from.models import Reuniao
from django.contrib import messages
from .forms import ReuniaoForm

def index(request):
    reunioes = Reuniao.objects.all()
    return render(request, 'reunioes_projeto/index.html', {'reuioes': reunioes})

def register(request):
    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reunião Marcada com Sucesso')
            form = ReuniaoForm()
        else:
            messages.error(request, 'Erro ao marcar reunião')
    else:
        form = ReuniaoForm()
    
    return render(request, 'reunioes_projeto/register.html', {'form': form})

def delete_reuniao(request, id):
    comida_consumida = Reuniao.objects.get(id=id)
    if request.method == 'POST':
        comida_consumida.delete()
        return redirect('/')
    return render(request, 'reunioes_projeto/delete.html')