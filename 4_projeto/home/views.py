from django.shortcuts import render
from django.http import HttpResponse

def meu_home(request):
    return HttpResponse('MEU PRIMEIRO WEB APP')

