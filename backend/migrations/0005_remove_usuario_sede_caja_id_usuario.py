# Generated by Django 4.0 on 2022-02-19 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_atencion_id_cliente_turno_id_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario_sede_caja',
            name='id_usuario',
        ),
    ]
