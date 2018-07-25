# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo',
            options={'verbose_name': 'grupo', 'verbose_name_plural': 'grupos'},
        ),
        migrations.AlterField(
            model_name='grupo',
            name='endereco',
            field=models.CharField(max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='grupo',
            field=models.CharField(choices=[('Grupo 1', 'Grupo1'), ('Grupo 2', 'Grupo2'), ('Grupo 3', 'Grupo3'), ('Grupo 3', 'Grupo3'), ('Grupo 4', 'Grupo4'), ('Grupo 5', 'Grupo5')], max_length=100, verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='sup_grupo',
            field=models.CharField(max_length=100, verbose_name='Sup_grupo'),
        ),
    ]