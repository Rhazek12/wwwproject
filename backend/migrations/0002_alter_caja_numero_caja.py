# Generated by Django 4.0 on 2022-02-12 20:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='numero_caja',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]