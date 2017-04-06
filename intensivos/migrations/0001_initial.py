# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-28 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Horario (*)')),
            ],
        ),
        migrations.CreateModel(
            name='Intensivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('nivel', models.DecimalField(choices=[(1, 'Elementary/Upper'), (2, 'FCE/CAE'), (3, 'Todos los niveles')], decimal_places=0, max_digits=1, verbose_name=b'Nivel del curso')),
                ('dias', models.CharField(max_length=50, verbose_name='Dias')),
                ('horario', models.CharField(max_length=50, verbose_name='Horario')),
                ('inicio', models.DateField(help_text='Formato: AAAA-MM-DD(a\xf1o-mes-d\xeda)', verbose_name='Start')),
                ('fin', models.DateField(help_text='Formato: AAAA-MM-DD(a\xf1o-mes-d\xeda)', verbose_name='End')),
                ('horas', models.DecimalField(decimal_places=0, max_digits=3, verbose_name=b'Horas')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, editable=False, max_length=6, verbose_name='Password')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre (*)')),
                ('surname', models.CharField(max_length=100, verbose_name='Apellido(s) (*)')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('birth_date', models.DateField(help_text='Formato: AAAA-MM-DD(a\xf1o-mes-d\xeda)', verbose_name='Birth Date')),
                ('telephone', models.CharField(max_length=12, verbose_name=b'Tel. Fijo (*)')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email (*)')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('nivel_ingles', models.DecimalField(blank=True, choices=[(1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2.1'), (5, 'B2.2'), (6, 'C1.1'), (7, 'C1.2'), (8, 'C2')], decimal_places=0, help_text=b'', max_digits=1, null=True, verbose_name='Nivel Ingles Actual')),
                ('curso', models.DecimalField(choices=[(1, 'Elementary (A2)'), (2, 'Pre-Intermediate (B1.1)'), (3, 'Intermediate (B1.2)'), (4, 'Upper-Intermediate (B2.1)'), (5, 'First Certificate (B2.2)'), (6, 'Pre-Advanded (C1.1)'), (7, 'Advanced (C1.2)'), (8, 'Proficiency (C2)')], decimal_places=0, max_digits=1, verbose_name=b'Nivel del curso')),
                ('accept_conditions', models.BooleanField(default=True, help_text='You must accept the conditions to register', verbose_name='Accept the conditions')),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('intensivos', models.ManyToManyField(help_text=b'Recuerde que debe elegir todos los horarios que le sean posibles', to='intensivos.Intensivo')),
            ],
        ),
    ]
