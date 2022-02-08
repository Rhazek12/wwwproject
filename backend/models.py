from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class usuario (models.Model):

    rol= models.CharField(max_length=20)
    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=30)

class cliente (models.Model):

    cedula = models.IntegerField(validators=[MaxValueValidator(10000000000000)])

class sede (models.Model):

    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)

class caja (models.Model):

    numero_caja = models.IntegerField(validators=[MaxValueValidator(100)])
    tipo = models.CharField(max_length=20)

class sede_caja (models.Model):

    id_sede = models.ForeignKey(sede,on_delete=models.CASCADE)
    id_caja = models.ForeignKey(caja,on_delete=models.CASCADE)

class turno (models.Model):

    codigo= models.CharField(max_length=5)
    priodidad = models.BooleanField()
    tipo = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    id_sede_caja = models.ForeignKey(sede_caja,on_delete=models.CASCADE)

class atencion (models.Model):

    id_cliente = models.ForeignKey(cliente,on_delete=models.CASCADE)
    id_turno = models.ForeignKey(turno,on_delete=models.CASCADE)
    id_sede_caja = models.ForeignKey(sede_caja,on_delete=models.CASCADE)

class usuario_sede_caja (models.Model):
    id_usuario = models.ForeignKey(usuario,on_delete=models.CASCADE)
    id_sede_caja = models.ForeignKey(sede_caja,on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)




