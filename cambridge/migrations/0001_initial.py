# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.DecimalField(choices=[(1, 'PB'), (2, 'CB'), (3, 'FS PB'), (4, 'FS CB')], decimal_places=0, max_digits=1, verbose_name='Tipo Examen')),
                ('exam_date', models.DateField(default=datetime.date.today)),
                ('registration_end_date', models.DateField(default=datetime.date.today, verbose_name='Fecha fin de la matriculaci\xf3n')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, editable=False, max_length=6, verbose_name='Password')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('postal_code', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Postal Code')),
                ('sex', models.DecimalField(choices=[(1, 'Male'), (2, 'Female')], decimal_places=0, max_digits=1, verbose_name='Sex')),
                ('birth_date', models.DateField(help_text='Formato: DD-MM-AAAA(dia-mes-a\xf1o)', verbose_name='Birth Date')),
                ('telephone', models.CharField(max_length=12, verbose_name='Telephone')),
                ('email', models.EmailField(max_length=254)),
                ('eide_alumn', models.BooleanField(help_text='Check this if you are an alumn of EIDE. If not please fill in your centre name', verbose_name='EIDE Alumn')),
                ('centre_name', models.CharField(blank=True, max_length=100, verbose_name='Centre Name')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('accept_conditions', models.BooleanField(default=True, help_text='You must accept the conditions to register', verbose_name='Accept the conditions')),
                ('accept_photo_conditions', models.BooleanField(default=True, help_text='Debes aceptar las condiciones de la la toma de foto para poder matricularte.', verbose_name='Aceptar las conficiones de la foto.')),
                ('minor', models.BooleanField(default=False, verbose_name='El candidato es menor de edad y yo soy su padre/madre o tutor legal.')),
                ('tutor_name', models.CharField(blank=True, max_length=50, verbose_name='Nombre de padre/madre o tutor.')),
                ('tutor_surname', models.CharField(blank=True, max_length=100, verbose_name='Apellido(s) del padre/madre o tutor.')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(default=b'', max_length=100, verbose_name='Description')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(default=b'', max_length=100, verbose_name='Description')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolExam',
            fields=[
                ('exam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cambridge.Exam')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cambridge.School')),
            ],
            bases=('cambridge.exam',),
        ),
        migrations.CreateModel(
            name='SchoolLevel',
            fields=[
                ('level_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cambridge.Level')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cambridge.School')),
            ],
            bases=('cambridge.level',),
        ),
        migrations.CreateModel(
            name='VenueExam',
            fields=[
                ('exam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cambridge.Exam')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cambridge.Venue')),
            ],
            bases=('cambridge.exam',),
        ),
        migrations.AddField(
            model_name='registration',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cambridge.Exam'),
        ),
        migrations.AddField(
            model_name='exam',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cambridge.Level'),
        ),
    ]