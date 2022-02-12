from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from backend.models import *
from django.http import JsonResponse
from .forms import *

# Create your views here.

def busqueda_test(request):
    return render(request, "pruebas.html")

def busqueda_usuario (request):

    usuarios=""

    if(request.GET["nombre"] and request.GET["contrasena"]):
        nombre_request = request.GET["nombre"]
        contrsena_request = request.GET["contrasena"]
        usuarios = list(usuario.objects.filter(nombre=nombre_request,contrasena=contrsena_request ).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        usuarios = list(usuario.objects.filter(id=id_request).values())

    elif(request.GET["nombre"]):
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

def editar_usuario(request):

    if(request.GET["id"]):
        id_usuario = request.GET["id"]
        var_usuario =get_object_or_404(usuario, id = id_usuario)
        datos = usuario_form(request.GET)

        if datos.is_valid():
            var_usuario.rol = datos.cleaned_data['rol']
            var_usuario.nombre = datos.cleaned_data['nombre']
            var_usuario.contrasena = datos.cleaned_data['contrasena']

            var_usuario.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_usuario(request):

    if(request.GET["id"]):
        id_usuario = request.GET["id"]
        var_usuario =get_object_or_404(usuario, id = id_usuario)
        var_usuario.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_usuario(request):

    datos = usuario_form()

    if (request.method == "GET"):
        datos = usuario_form(request.GET)

        if datos.is_valid():
            var_usuario = usuario()
            var_usuario.rol = datos.cleaned_data['rol']
            var_usuario.nombre = datos.cleaned_data['nombre']
            var_usuario.contrasena = datos.cleaned_data['contrasena']

            var_usuario.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)



