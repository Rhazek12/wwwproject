from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from backend.models import *
from django.http import JsonResponse
from .forms import *
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
#Variables globales
lista_turnos = []
lista_g = []
lista_ie = []
lista_s = []
lista_d = []
lista_vip = []

#View de Home:

def home(request):
    return render(request, "index.html")

#SOLO PARA HACER PRUEBAS EN EL BACKEND:

def busqueda_test(request):
    return render(request, "pruebas.html")

#------------------------------------------------------------------------------------------

#CRUD DE USUARIO:

def busqueda_usuario (request):

    usuarios=""

    if(request.GET["nombre"] and request.GET["contrasena"]):
        nombre_request = request.GET["nombre"]
        var_usuario =get_object_or_404(usuario, nombre = nombre_request)
        contrsena_request =check_password( request.GET["contrasena"],var_usuario.contrasena)
        if (contrsena_request == True):
            usuarios = list(usuario.objects.filter(nombre=nombre_request).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        usuarios = list(usuario.objects.filter(id=id_request).values())

    elif(request.GET["nombre"]):
        nombre_request = request.GET["nombre"]
        usuarios = list(usuario.objects.filter(nombre=nombre_request).values())
        
    elif(request.GET["rol"]):
        rol_request = request.GET["rol"]
        usuarios = list(usuario.objects.filter(rol=rol_request).values())
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
            var_usuario.contrasena = make_password(datos.cleaned_data['contrasena'])

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
            var_usuario.contrasena = make_password(datos.cleaned_data['contrasena'])

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
        

def crear_cliente(cedula):


    if (cedula):


        var_cliente = cliente()
        var_cliente.cedula = cedula

        var_cliente.save()

        return JsonResponse(True, safe=False)
    else:
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
            id_sede= request.GET["id_sede"]
            id_caja= request.GET["id_caja"]
            var_sede =get_object_or_404(sede, id = id_sede)
            var_caja =get_object_or_404(caja, id = id_caja)
            var_sede_caja= sede_caja()
            var_sede_caja.id_sede= var_sede
            var_sede_caja.id_caja = var_caja

            var_sede_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------

#CRUD DE ATENCION

def busqueda_atencion(request):

    atenciones=""

    if(request.GET["id_turno"] and request.GET["id_sede_caja"]):
        id_turno_request = request.GET["id_turno"]
        id_sede_caja_request = request.GET["id_sede_caja"]
        atenciones = list(atencion.objects.filter(id_turno=id_turno_request,id_sede_caja=id_sede_caja_request).values())
    elif(request.GET["id_turno"]):
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
        

def crear_atencion(turno_atendido,sede_caja_que_atiende):

    if (turno_atendido and sede_caja_que_atiende):
        datos = True

        if (datos == True):

            var_turno= get_object_or_404(turno, id = turno_atendido)
            var_sede_caja =get_object_or_404(sede_caja, id = sede_caja_que_atiende)
            var_atencion= atencion()
            var_atencion.id_turno= var_turno
            var_atencion.id_sede_caja = var_sede_caja

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
            id_sede_caja= request.GET["id_sede_caja"]
            id_usuario= request.GET["id_usuario"]
            var_sede_caja =get_object_or_404(sede_caja, id = id_sede_caja)
            var_usuario =get_object_or_404(usuario, id = id_usuario)
            var_usuario_sede_caja= usuario_sede_caja()
            var_usuario_sede_caja.id_usuario= var_usuario
            var_usuario_sede_caja.id_sede_caja = var_sede_caja

            var_usuario_sede_caja.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)

    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------

#CRUD DE TURNO

def busqueda_turno(request):

    turnos=""

    if(request.GET["codigo"]):
        codigo_request = request.GET["codigo"]
        turnos = list(turno.objects.filter(codigo=codigo_request).values())
    elif(request.GET["prioridad"]):
        prioridad_request = request.GET["prioridad"]
        turnos = list(turno.objects.filter(prioridad=prioridad_request).values())
    elif(request.GET["tipo"]):
        tipo_request = request.GET["tipo"]
        turnos = list(turno.objects.filter(tipo=tipo_request).values())
    elif(request.GET["cedula_cliente"]):
        cedula_cliente_request = request.GET["cedula_cliente"]
        var_cliente =get_object_or_404(cliente, cedula = cedula_cliente_request)
        id_cliente_request = var_cliente.id
        turnos = list(turno.objects.filter(id_cliente=id_cliente_request).values())
    elif(request.GET["id"]):
        id_request = request.GET["id"]
        turnos = list(turno.objects.filter(id=id_request).values())
    else:
        turnos = list(turno.objects.values())

    return JsonResponse(turnos, safe=False)

def editar_turno(request):

    if(request.GET["id"]):
        id_turno = request.GET["id"]
        var_turno =get_object_or_404(turno, id = id_turno)
        datos = turno_form(request.GET)

        if datos.is_valid():
            var_turno.codigo = datos.cleaned_data['codigo']
            var_turno.prioridad = datos.cleaned_data['prioridad']
            var_turno.tipo = datos.cleaned_data['tipo']
            var_turno.id_cliente = datos.cleaned_data['id_cliente']
            var_turno.save()

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def eliminar_turno(request):

    if(request.GET["id"]):
        id_turno = request.GET["id"]
        var_turno =get_object_or_404(turno, id = id_turno)
        var_turno.delete()
        return JsonResponse(True, safe=False)
    else:
        return JsonResponse(False, safe=False)
        

def crear_turno(request):

    datos = turno_form()

    if (request.method == "GET"):
        datos = turno_form(request.GET)
        fecha_actual=datetime.today().strftime('%Y-%m-%d')
        ultimo_regsitro = turno.objects.filter().last()
        ultima_fecha= ultimo_regsitro.fecha
        ultima_fecha = ultima_fecha.strftime('%Y-%m-%d')
        ultimo_codigo = ultimo_regsitro.codigo
        if(request.GET["prioridad"]):
            prioridad_dada = True
        else:
            prioridad_dada = False
        cedula_cliente= request.GET["cedula_cliente"]
        clientes = list(cliente.objects.filter(cedula=cedula_cliente).values())
        if (clientes == []):
            crear_cliente(int(cedula_cliente))
            var_cliente =get_object_or_404(cliente, cedula = cedula_cliente)
        else:
            var_cliente =get_object_or_404(cliente, cedula = cedula_cliente)
             
        if datos.is_valid():
            if (fecha_actual == ultima_fecha):
                codigo_generado = ultimo_codigo + 1
                var_turno= turno()
                var_turno.prioridad = prioridad_dada
                var_turno.tipo = datos.cleaned_data['tipo']
                var_turno.id_cliente = var_cliente
                var_turno.codigo = codigo_generado
                var_turno.save()
                #Aquí se almacena el turno en la lista
                turno_lista = {codigo_generado : datos.cleaned_data['tipo']}
                almacenar_turno(turno_lista, prioridad_dada)
            else:
                codigo_generado = 1
                var_turno= turno()
                var_turno.prioridad = prioridad_dada
                var_turno.tipo = datos.cleaned_data['tipo']
                var_turno.id_cliente = var_cliente
                var_turno.codigo = codigo_generado
                var_turno.save()
                #Aquí se almacena el turno en la lista
                turno_lista = {codigo_generado : datos.cleaned_data['tipo']}
                limpiar_listas()
                almacenar_turno(turno_lista,prioridad_dada)

            return JsonResponse(True, safe=False)
        else:
            return JsonResponse(False, safe=False)
    
    return JsonResponse(False, safe=False)
#------------------------------------------------------------------------------------------

#PRIORIDAD DE TURNO

def almacenar_turno(turno_nuevo, prioridad):

    global lista_turnos
    global lista_g
    global lista_ie
    global lista_s
    global lista_d
    global lista_vip
    lista_turnos.append(turno_nuevo)
    elementos = [*turno_nuevo.values() ]
    if(elementos[0] == "G"):
        lista_g.append(turno_nuevo)
        print ("es de tipo g")
    elif(elementos[0] == "IE"):
        lista_ie.append(turno_nuevo)
        print ("es de tipo ie")
    elif(elementos[0] == "S"):
        lista_s.append(turno_nuevo)
        print ("es de tipo s")
    elif(elementos[0] == "D"):
        lista_d.append(turno_nuevo)
        print ("es de tipo d")
    else:
        print ("tipo no valido")
    
    if(prioridad == True):
        lista_vip.append(turno_nuevo)
        print ("es vip el cabron")

    print("lista:" + str(lista_turnos))
    print("lista g:" + str(lista_g))
    print("lista ie:" + str(lista_ie))
    print("lista s:" + str(lista_s))
    print("lista d:" + str(lista_d))
    print("lista vip:" + str(lista_vip))
    return lista_turnos

def pedir_turno(request):

    siguiente_turno = {}
    global lista_turnos
    global lista_g
    global lista_ie
    global lista_s
    global lista_d
    global lista_vip
    tipo_de_caja = request.GET["tipo"]
    if(tipo_de_caja == 'G'):
        if(len(lista_g)>0):
            siguiente_turno= lista_g.pop(0)
            lista_turnos.remove(siguiente_turno)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
        elif(len(lista_turnos)>0):
            siguiente_turno = lista_turnos.pop(0)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
            if (lista_ie.count(siguiente_turno)>0):
                lista_ie.remove(siguiente_turno)
            if (lista_s.count(siguiente_turno)>0):
                lista_s.remove(siguiente_turno)
            if (lista_d.count(siguiente_turno)>0):
                lista_d.remove(siguiente_turno)
        else:
            print("no hay turnos por atender")
    elif(tipo_de_caja == 'IE'):
        if(len(lista_ie)>0):
            siguiente_turno = lista_ie.pop(0)
            lista_turnos.remove(siguiente_turno)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
        elif(len(lista_turnos)>0):
            siguiente_turno = lista_turnos.pop(0)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
            if (lista_g.count(siguiente_turno)>0):
                lista_g.remove(siguiente_turno)
            if (lista_s.count(siguiente_turno)>0):
                lista_s.remove(siguiente_turno)
            if (lista_d.count(siguiente_turno)>0):
                lista_d.remove(siguiente_turno)
        else:
            print("no hay turnos por atender")
    elif(tipo_de_caja == 'S'):
        if(len(lista_s)>0):
            siguiente_turno = lista_s.pop(0)
            lista_turnos.remove(siguiente_turno)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
        elif(len(lista_turnos)>0):
            siguiente_turno = lista_turnos.pop(0)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
            if (lista_ie.count(siguiente_turno)>0):
                lista_ie.remove(siguiente_turno)
            if (lista_g.count(siguiente_turno)>0):
                lista_g.remove(siguiente_turno)
            if (lista_d.count(siguiente_turno)>0):
                lista_d.remove(siguiente_turno)
        else:
            print("no hay turnos por atender")
    elif(tipo_de_caja == 'D'):
        if(len(lista_d)>0):
            siguiente_turno = lista_d.pop(0)
            lista_turnos.remove(siguiente_turno)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
        elif(len(lista_turnos)>0):
            siguiente_turno = lista_turnos.pop(0)
            if (lista_vip.count(siguiente_turno)>0):
                lista_vip.remove(siguiente_turno)
            if (lista_ie.count(siguiente_turno)>0):
                lista_ie.remove(siguiente_turno)
            if (lista_s.count(siguiente_turno)>0):
                lista_s.remove(siguiente_turno)
            if (lista_g.count(siguiente_turno)>0):
                lista_g.remove(siguiente_turno)
        else:
            print("no hay turnos por atender")
    elif(tipo_de_caja == 'VIP'):
        if(len(lista_vip)>0):
            siguiente_turno = lista_vip.pop(0)
            lista_turnos.remove(siguiente_turno)
            if (lista_g.count(siguiente_turno)>0):
                lista_g.remove(siguiente_turno)
            if (lista_ie.count(siguiente_turno)>0):
                lista_ie.remove(siguiente_turno)
            if (lista_s.count(siguiente_turno)>0):
                lista_s.remove(siguiente_turno)
            if (lista_d.count(siguiente_turno)>0):
                lista_d.remove(siguiente_turno)
        elif(len(lista_turnos)>0):
            siguiente_turno = lista_turnos.pop(0)
            if (lista_g.count(siguiente_turno)>0):
                lista_g.remove(siguiente_turno)
            if (lista_ie.count(siguiente_turno)>0):
                lista_ie.remove(siguiente_turno)
            if (lista_s.count(siguiente_turno)>0):
                lista_s.remove(siguiente_turno)
            if (lista_d.count(siguiente_turno)>0):
                lista_d.remove(siguiente_turno)
        else:
            print("no hay turnos por atender")
    else:
        print("tipo incorrecto")
    print(siguiente_turno)
    siguiente_turno_tipo = [*siguiente_turno.values()]
    siguiente_turno_codigo =[*siguiente_turno.keys() ]
    turno_json = {"tipo":str(siguiente_turno_tipo[0]),"codigo":int(siguiente_turno_codigo[0])}

    #creando registro de atención
    turnos = list(turno.objects.filter(codigo=int(siguiente_turno_codigo[0]), tipo=str(siguiente_turno_tipo[0])).values())
    elemento_turnos = turnos[0]
    turno_id =elemento_turnos["id"]
    print(turno_id)
    id_de_sede_caja = request.GET["id_sede_caja"]
    crear_atencion(turno_id,id_de_sede_caja)

    return JsonResponse(turno_json, safe=False)

def limpiar_listas():
    global lista_turnos
    lista_turnos.clear()
    global lista_g
    lista_g.clear()
    global lista_ie
    lista_ie.clear()
    global lista_s
    lista_s.clear()
    global lista_d
    lista_d.clear()
    global lista_vip
    lista_vip.clear()
    return True

#------------------------------------------------------------------------------------------

#ESTADISTICAS

def estadistica_turnos_por_sede(request):
    lista_json = []
    if(request.GET["id_sede"]):
        id_sede_request = request.GET["id_sede"]
        sede_cajas = list(sede_caja.objects.filter(id_sede=id_sede_request).values('id', 'id_caja'))
        i=0
        while i < len(sede_cajas):
            elemento_id = sede_cajas[i]
            sede_caja_id =elemento_id["id"]
            caja_id =elemento_id["id_caja"]
            nombre_dic = list(caja.objects.filter(id=caja_id).values("tipo"))
            atenciones = len(list(atencion.objects.filter(id_sede_caja=sede_caja_id).values()))
            prenombre = nombre_dic[0]
            nombre = prenombre["tipo"]
            print (nombre_dic)
            dic ={nombre:atenciones}
            lista_json.append(dic)
            i=i+1
    return JsonResponse(lista_json, safe=False)

def estadistica_turnos_vip(request):

    turnos_totales = len(list(turno.objects.values()))
    turnos_true = len(list(turno.objects.filter(prioridad=True).values()))
    turnos_false = turnos_totales - turnos_true
    porcentaje_true = int ((turnos_true/turnos_totales)*100)
    porcentaje_false =100 - porcentaje_true

    estadisticas_json = {"vipdato":turnos_true,
                        "novipdato":turnos_false,
                        "vipporc":porcentaje_true,
                        "novipporc":porcentaje_false}
    
    return JsonResponse(estadisticas_json, safe=False)

def estadistica_turnos_por_tipo(request):
    turnos_totales = len(list(turno.objects.values()))
    turnos_g = len(list(turno.objects.filter(tipo="G").values()))
    porcentaje_g = int ((turnos_g/turnos_totales)*100)
    turnos_ie = len(list(turno.objects.filter(tipo="IE").values()))
    porcentaje_ie = int ((turnos_ie/turnos_totales)*100)
    turnos_s = len(list(turno.objects.filter(tipo="S").values()))
    porcentaje_s = int ((turnos_s/turnos_totales)*100)
    turnos_d = len(list(turno.objects.filter(tipo="D").values()))
    porcentaje_d = 100 - (porcentaje_s + porcentaje_ie + porcentaje_g)
    estadisticas_json = {"turnosg":turnos_g,
                        "turnosie":turnos_ie,
                        "turnoss":turnos_s,
                        "turnosd":turnos_d,
                        "porcg":porcentaje_g,
                        "procie":porcentaje_ie,
                        "porcs":porcentaje_s,
                        "porcd":porcentaje_d}
    
    return JsonResponse(estadisticas_json, safe=False)