"""proyecto_www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_usuario/', views.busqueda_usuario),
    path('crear_usuario/', views.crear_usuario),
    path('eliminar_usuario/', views.eliminar_usuario),
    path('editar_usuario/', views.editar_usuario),
    path('busqueda_cliente/', views.busqueda_cliente),
    path('crear_cliente/', views.crear_cliente),
    path('eliminar_cliente/', views.eliminar_cliente),
    path('editar_cliente/', views.editar_cliente),
    path('busqueda_sede/', views.busqueda_sede),
    path('crear_sede/', views.crear_sede),
    path('eliminar_sede/', views.eliminar_sede),
    path('editar_sede/', views.editar_sede),
    path('busqueda_caja/', views.busqueda_caja),
    path('crear_caja/', views.crear_caja),
    path('eliminar_caja/', views.eliminar_caja),
    path('editar_caja/', views.editar_caja),
    path('busqueda_sede_caja/', views.busqueda_sede_caja),
    path('crear_sede_caja/', views.crear_sede_caja),
    path('eliminar_sede_caja/', views.eliminar_sede_caja),
    path('editar_sede_caja/', views.editar_sede_caja),
    path('busqueda_atencion/', views.busqueda_atencion),
    path('crear_atencion/', views.crear_atencion),
    path('eliminar_atencion/', views.eliminar_atencion),
    path('editar_atencion/', views.editar_atencion),
    path('busqueda_usuario_sede_caja/', views.busqueda_usuario_sede_caja),
    path('crear_usuario_sede_caja/', views.crear_usuario_sede_caja),
    path('eliminar_usuario_sede_caja/', views.eliminar_usuario_sede_caja),
    path('editar_usuario_sede_caja/', views.editar_usuario_sede_caja),
    path('busqueda_turno/', views.busqueda_turno),
    path('crear_turno/', views.crear_turno),
    path('eliminar_turno/', views.eliminar_turno),
    path('editar_turno/', views.editar_turno),
    path('pedir_turno/', views.pedir_turno),
    path('estadistica_turnos_vip/', views.estadistica_turnos_vip),
    path('estadistica_turnos_por_sede/', views.estadistica_turnos_por_sede),
    path('estadistica_turnos_por_tipo/', views.estadistica_turnos_por_tipo),
    path('',views.home),
]
