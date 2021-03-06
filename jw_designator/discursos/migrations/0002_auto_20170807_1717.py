# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-07 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oradores',
            options={'verbose_name': 'orador', 'verbose_name_plural': 'oradores'},
        ),
        migrations.AddField(
            model_name='oradores',
            name='contato',
            field=models.CharField(default=31992323628, max_length=100, verbose_name='Telefone'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oradores',
            name='ajuda',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=100, verbose_name='Ajuda'),
        ),
        migrations.AlterField(
            model_name='oradores',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='oradores',
            name='nota',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=100, verbose_name='Nota'),
        ),
    ]
