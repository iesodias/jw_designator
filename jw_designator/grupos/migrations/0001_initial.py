# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=100, verbose_name='nome')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('endereco', models.CharField(max_length=100, verbose_name='nome')),
                ('sup_grupo', models.CharField(max_length=100, verbose_name='nome')),
            ],
        ),
    ]
