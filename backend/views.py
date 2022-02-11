from django.http import HttpResponse
from django.shortcuts import render
from backend.models import *
from django.http import JsonResponse

# Create your views here.

def busqueda_test(request):
    return render(request, "pruebas.html")

def busqueda_clientes (request):

    usuarios=""

    if(request.GET["nombre"]):
        nombre_request = request.GET["nombre"]
        usuarios = list(usuario.objects.filter(nombre=nombre_request).values())
        
    elif(request.GET["rol"]):
        rol_request = request.GET["rol"]
        usuarios = list(usuario.objects.filter(rol=rol_request).values())
    elif(request.GET["contrasena"]):
        contrsena_request = request.GET["contrasena"]
        usuarios = list(usuario.objects.filter(contrasena=contrsena_request).values())
    else:
        usuarios = list(usuario.objects.values())

    return JsonResponse(usuarios, safe=False)
    
