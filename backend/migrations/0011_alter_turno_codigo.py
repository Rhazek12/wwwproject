# Generated by Django 4.0 on 2022-02-24 04:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_rename_priodidad_turno_prioridad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='codigo',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
