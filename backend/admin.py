from django.contrib import admin
from backend.models import *

# Register your models here.
admin.site.register(usuario)
admin.site.register(cliente)
admin.site.register(sede)
admin.site.register(caja)
admin.site.register(sede_caja)
admin.site.register(turno)
admin.site.register(atencion)
admin.site.register(usuario_sede_caja)

