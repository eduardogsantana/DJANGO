from django.shortcuts import render, redirect
from .models import Food, Consumed

def index(request):
    if request.method == 'POST':
        comida_consumida = request.POST['comida_consumida']
        consumo_food = Food.objects.get(name=comida_consumida)
        user = request.user
        consumo = Consumed(user=user, comida_consumida=consumo_food)
        consumo.save()

        foods = Food.objects.all()
    else:
        foods = Food.objects.all()

    food_consumed = Consumed.objects.filter(user=request.user)

    return render(request, 'nutrion/index.html', {'foods': foods, 'food_consumed': food_consumed})

def delete_comida(request, id):
    comida_consumida = Consumed.objects.get(id=id)
    if request.method == 'POST':
        comida_consumida.delete()
        return redirect('/')
    return render(request, 'nutrion/delete.html')

