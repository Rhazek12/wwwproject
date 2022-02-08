from django.http import HttpResponse
from django.shortcuts import render
from backend.models import *
from django.http import JsonResponse

# Create your views here.

def busqueda_clientes (request):
    usuarios = list(usuario.objects.values())
    return JsonResponse(usuarios, safe=False)