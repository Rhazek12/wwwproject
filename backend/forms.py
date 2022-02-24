import django
from django import forms

from backend.models import caja, sede

class usuario_form(forms.Form):
    rol = forms.CharField(max_length=20, required=True)
    nombre = forms.CharField(max_length=30, required=True)
    contrasena = forms.CharField(max_length=30, required=True)

class cliente_form(forms.Form):
    cedula = forms.IntegerField(max_value=10000000000000, required=True)

class sede_form(forms.Form):
    nombre =  forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=50, required=True)

class caja_form(forms.Form):
    numero_caja =  forms.IntegerField(max_value=100, required=True)
    tipo = forms.CharField(max_length=20, required=True)

class sede_caja_form(forms.Form):
    id_sede =  forms.IntegerField(required=True)
    id_caja = forms.IntegerField(required=True)

class turno_form (forms.Form):

    prioridad = forms.BooleanField(required=False)
    tipo = forms.CharField(max_length=20,required=True)
    cedula_cliente = forms.IntegerField(required=True)

class atencion_form (forms.Form):
    
    id_turno = forms.IntegerField(required=True)
    id_sede_caja = forms.IntegerField(required=True)

class usuario_sede_caja_form (forms.Form):
    id_usuario = forms.IntegerField(required=True)
    id_sede_caja = forms.IntegerField(required=True)