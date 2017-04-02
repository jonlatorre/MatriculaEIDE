# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-25 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebasnivel', '0002_auto_20170325_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='centre',
            field=models.CharField(blank=True, max_length=100, verbose_name='Academia/colegio/instituto/universidad'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='course',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nivel o curso escolar realizado'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='english_level',
            field=models.DecimalField(choices=[(1, 'A1'), (2, 'A2'), (3, 'B1.1'), (4, 'B1.2 (PET)'), (5, 'B2.1'), (6, 'B2.2 (FIRST)'), (7, 'C1.1'), (8, 'C1.2'), (9, 'C2 (ADVANCED)')], decimal_places=0, default=1, max_digits=1, verbose_name='English Level'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_english_certificate',
            field=models.BooleanField(default=False, verbose_name='Tienes titulaci\xf3n oficial de Cambridge English o EOI.'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_english_certificate_description',
            field=models.CharField(blank=True, max_length=100, verbose_name='Cual es la m\xe1s alta obtenida'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_english_course',
            field=models.CharField(blank=True, max_length=100, verbose_name='\xdaltimo curso de ingl\xe9s m\xe1s avanzado realizado.'),
        ),
    ]
