from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from backend.models import *
from django.http import JsonResponse
from .forms import *

# Create your views here.

#SOLO PARA HACER PRUEBAS EN EL BACKEND:

def busqueda_test(request):
    return render(request, "pruebas.html")

#------------------------------------------------------------------------------------------

#CRUD DE USUARIO:

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
    return JsonResponse(False, safe=False)

#------------------------------------------------------------------------------------------

#CRUD DE CLIENTE:

def busqueda_cliente (request):

    clientes =""

    if(request.GET["cedula"]):
        cedula_request = request.GET["cedula"]
        clientes = list(cliente.objects.filter(cedula=cedula_request).values())
    else:
        clientes = list(cliente.objects.values())

    return JsonResponse(clientes, safe=False)

def editar_cliente(request):

    if(request.GET["id"]):
        id_cliente = request.GET["id"]
        var_cliente =get_object_or_404(cliente, id = id_cliente)
        datos = cliente_form(request.GET)

        if datos.is_valid():
            var_cliente.cedula = datos.cleaned_data['cedula']

            var_cliente.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_cliente(request):

    if(request.GET["cedula"]):
        cedula_cliente = request.GET["cedula"]
        var_cliente =get_object_or_404(cliente, cedula = cedula_cliente)
        var_cliente.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_cliente(request):

    datos = cliente_form()

    if (request.method == "GET"):
        datos = cliente_form(request.GET)

        if datos.is_valid():
            var_cliente = cliente()
            var_cliente.cedula = datos.cleaned_data['cedula']

            var_cliente.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)

#------------------------------------------------------------------------------------------

#CRUD DE SEDE:

def busqueda_sede (request):

    sedes=""

    if(request.GET["nombre"]):
        nombre_request = request.GET["nombre"]
        sedes = list(sede.objects.filter(nombre=nombre_request).values())
    elif(request.GET["direccion"]):
        direccion_request = request.GET["direccion"]
        sedes = list(sede.objects.filter(direccion=direccion_request).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        sedes = list(sede.objects.filter(id=id_request).values())
    else:
        sedes = list(sede.objects.values())

    return JsonResponse(sedes, safe=False)

def editar_sede(request):

    if(request.GET["id"]):
        id_sede = request.GET["id"]
        var_sede =get_object_or_404(sede, id = id_sede)
        datos = sede_form(request.GET)

        if datos.is_valid():
            var_sede.nombre = datos.cleaned_data['nombre']
            var_sede.direccion = datos.cleaned_data['direccion']
            var_sede.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_sede(request):

    if(request.GET["id"]):
        id_sede = request.GET["id"]
        var_sede =get_object_or_404(sede, id = id_sede)
        var_sede.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_sede(request):

    datos = sede_form()

    if (request.method == "GET"):
        datos = sede_form(request.GET)

        if datos.is_valid():
            var_sede= sede()
            var_sede.nombre = datos.cleaned_data['nombre']
            var_sede.direccion = datos.cleaned_data['direccion']

            var_sede.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------

#CRUD DE CAJA

def busqueda_caja (request):

    cajas=""

    if(request.GET["numero_caja"]):
        numero_caja_request = request.GET["numero_caja"]
        cajas = list(caja.objects.filter(numero_caja=numero_caja_request).values())
    elif(request.GET["tipo"]):
        tipo_request = request.GET["tipo"]
        cajas = list(caja.objects.filter(tipo=tipo_request).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        cajas = list(caja.objects.filter(id=id_request).values())
    else:
        cajas = list(caja.objects.values())

    return JsonResponse(cajas, safe=False)

def editar_caja(request):

    if(request.GET["id"]):
        id_caja = request.GET["id"]
        var_caja =get_object_or_404(caja, id = id_caja)
        datos = caja_form(request.GET)

        if datos.is_valid():
            var_caja.numero_caja = datos.cleaned_data['numero_caja']
            var_caja.tipo = datos.cleaned_data['tipo']
            var_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_caja(request):

    if(request.GET["id"]):
        id_caja = request.GET["id"]
        var_caja =get_object_or_404(caja, id = id_caja)
        var_caja.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_caja(request):

    datos = caja_form()

    if (request.method == "GET"):
        datos = caja_form(request.GET)

        if datos.is_valid():
            var_caja= caja()
            var_caja.numero_caja = datos.cleaned_data['numero_caja']
            var_caja.tipo = datos.cleaned_data['tipo']

            var_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------

#CRUD DE SEDE_CAJA

def busqueda_sede_caja (request):

    sede_cajas=""

    if(request.GET["id_sede"]):
        id_sede_request = request.GET["id_sede"]
        sede_cajas = list(sede_caja.objects.filter(id_sede=id_sede_request).values())
    elif(request.GET["id_caja"]):
        id_caja_request = request.GET["id_caja"]
        sede_cajas = list(sede_caja.objects.filter(id_caja=id_caja_request).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        sede_cajas = list(sede_caja.objects.filter(id=id_request).values())
    else:
        sede_cajas = list(sede_caja.objects.values())

    return JsonResponse(sede_cajas, safe=False)

def editar_sede_caja(request):

    if(request.GET["id"]):
        id_sede_caja = request.GET["id"]
        var_sede_caja =get_object_or_404(sede_caja, id = id_sede_caja)
        datos = sede_caja_form(request.GET)

        if datos.is_valid():
            var_sede_caja.id_sede = datos.cleaned_data['id_sede']
            var_sede_caja.id_caja = datos.cleaned_data['id_caja']
            var_sede_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_sede_caja(request):

    if(request.GET["id"]):
        id_sede_caja = request.GET["id"]
        var_sede_caja =get_object_or_404(sede_caja, id = id_sede_caja)
        var_sede_caja.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_sede_caja(request):

    datos = sede_caja_form()

    if (request.method == "GET"):
        datos = sede_caja_form(request.GET)

        if datos.is_valid():
            var_sede_caja= sede_caja()
            var_sede_caja.id_sede= datos.cleaned_data['id_sede']
            var_sede_caja.id_caja = datos.cleaned_data['id_caja']

            var_sede_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------

#CRUD DE ATENCION

def busqueda_atencion(request):

    atenciones=""

    if(request.GET["id_turno"]):
        id_turno_request = request.GET["id_turno"]
        atenciones = list(atencion.objects.filter(id_turno=id_turno_request).values())
    elif(request.GET["id_sede_caja"]):
        id_sede_caja_request = request.GET["id_sede_caja"]
        atenciones = list(atencion.objects.filter(id_sede_caja=id_sede_caja_request).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        atenciones = list(atencion.objects.filter(id=id_request).values())
    else:
        atenciones = list(atencion.objects.values())

    return JsonResponse(atenciones, safe=False)

def editar_atencion(request):

    if(request.GET["id"]):
        id_atencion = request.GET["id"]
        var_atencion =get_object_or_404(atencion, id = id_atencion)
        datos = atencion_form(request.GET)

        if datos.is_valid():
            var_atencion.id_turno = datos.cleaned_data['id_turno']
            var_atencion.id_sede_caja = datos.cleaned_data['id_sede_caja']
            var_atencion.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_atencion(request):

    if(request.GET["id"]):
        id_atencion = request.GET["id"]
        var_atencion =get_object_or_404(atencion, id = id_atencion)
        var_atencion.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_atencion(request):

    datos = atencion_form()

    if (request.method == "GET"):
        datos = atencion_form(request.GET)

        if datos.is_valid():
            var_atencion= atencion()
            var_atencion.id_turno= datos.cleaned_data['id_turno']
            var_atencion.id_sede_caja = datos.cleaned_data['id_sede_caja']

            var_atencion.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------

#CRUD DE USUARIO_SEDE_CAJA

def busqueda_usuario_sede_caja(request):

    usuario_sede_cajas=""

    if(request.GET["id_usuario"]):
        id_usuario_request = request.GET["id_usuario"]
        usuario_sede_cajas = list(usuario_sede_caja.objects.filter(id_usuario=id_usuario_request).values())
    elif(request.GET["id_sede_caja"]):
        id_sede_caja_request = request.GET["id_sede_caja"]
        usuario_sede_cajas = list(usuario_sede_caja.objects.filter(id_sede_caja=id_sede_caja_request).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        usuario_sede_cajas = list(usuario_sede_caja.objects.filter(id=id_request).values())
    else:
        usuario_sede_cajas = list(usuario_sede_caja.objects.values())

    return JsonResponse(usuario_sede_cajas, safe=False)

def editar_usuario_sede_caja(request):

    if(request.GET["id"]):
        id_usuario_sede_caja = request.GET["id"]
        var_usuario_sede_caja =get_object_or_404(usuario_sede_caja, id = id_usuario_sede_caja)
        datos = usuario_sede_caja_form(request.GET)

        if datos.is_valid():
            var_usuario_sede_caja.id_usuario = datos.cleaned_data['id_usuario']
            var_usuario_sede_caja.id_sede_caja = datos.cleaned_data['id_sede_caja']
            var_usuario_sede_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_usuario_sede_caja(request):

    if(request.GET["id"]):
        id_usuario_sede_caja = request.GET["id"]
        var_usuario_sede_caja =get_object_or_404(usuario_sede_caja, id = id_usuario_sede_caja)
        var_usuario_sede_caja.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_usuario_sede_caja(request):

    datos = usuario_sede_caja_form()

    if (request.method == "GET"):
        datos = usuario_sede_caja_form(request.GET)

        if datos.is_valid():
            var_usuario_sede_caja= usuario_sede_caja()
            var_usuario_sede_caja.id_usuario= datos.cleaned_data['id_usuario']
            var_usuario_sede_caja.id_sede_caja = datos.cleaned_data['id_sede_caja']

            var_usuario_sede_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------