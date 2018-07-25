# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import jw_designator.cadastros.models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro',
            options={'verbose_name': 'cadastro', 'verbose_name_plural': 'cadastros'},
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='carrinho',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=30, verbose_name='carrinho'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='designacao',
            field=models.CharField(choices=[('Ancião', 'Ancião'), ('Servo Ministerial', 'Servo Ministerial'), ('Irmão Batizado', 'Irmão Batizado'), ('Publicador', 'Publicador')], max_length=30, verbose_name='designacao'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=30, verbose_name='sexo'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='telefone',
            field=models.CharField(max_length=20, validators=[jw_designator.cadastros.models.validar_tel], verbose_name='telefone'),
        ),
    ]
