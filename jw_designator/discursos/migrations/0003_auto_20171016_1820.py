# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discursos', '0002_auto_20170807_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oradores',
            name='data',
            field=models.DateField(unique=True),
        ),
    ]