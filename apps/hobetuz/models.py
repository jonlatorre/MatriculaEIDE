# -*- coding: utf-8 -*-

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

from django.db import models
from django.contrib.localflavor import generic
from django.contrib.localflavor.es.forms import *
from django.core.mail import EmailMultiAlternatives

from random import choice
from string import letters
import datetime

from django.conf import settings

# favour django-mailer but fall back to django.core.mail
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail, mail_admins
else:
    from django.core.mail import send_mail, mail_admins

from django.utils.translation import gettext_lazy as _
# Create your models here.

SEXO = (
    (1, _('Male')),
    (2, _('Female')),
)

TITULACION = (
    (1, _('Sin titulación')),
    (2, _('Graduado Escolar o ESO')),
    (3, _('Bachillerato, COU o similar')),
    (4, _('Grado, Licenciatura o Diplomatura')),
)


class Curso(models.Model):
	name = models.CharField(max_length=50)
	matricula_abierta = models.BooleanField(_('Matricula Abierta'),default=datetime.date.today)
	def __unicode__(self):
		return "Curso de %s"%(self.name)
	

#Asbtract model to inherit from him
class Registration(models.Model):
	curso = models.ForeignKey(Curso,limit_choices_to = {'matricula_abierta': True})
	password = models.CharField(_('Password'),max_length=6,blank=True,editable=False)
	name = models.CharField(_('Name'),max_length=50)
	surname = models.CharField(_('Surname'),max_length=100)
	#~ address = models.CharField(_('Address'),max_length=100)
	#~ location = models.CharField(_('Location'),max_length=100)
	#~ postal_code = models.DecimalField(_('Postal Code'),max_digits=6, decimal_places=0)
	#~ sex = models.DecimalField(_('Sex'),max_digits=1, decimal_places=0,choices=SEXO)
	#~ birth_date = models.DateField(_('Birth Date'),help_text=_('Formato: DD-MM-AAAA(dia-mes-año)'))
	#dni = models.CharField(max_length=9,blank=True,help_text=_('Introduce el DNI completo con la letra sin espacios ni guiones'))
	telephone = models.CharField(_('Teléfono Fijo'),max_length=12)
	telephone2 = models.CharField(_('Teléfono Móvil'),max_length=12)
	email = models.EmailField()
	titulacion = models.DecimalField(_('Titulación'),max_digits=1, decimal_places=0,choices=TITULACION)
	
	desempleado = models.BooleanField(_('Desempleado'), help_text=_('Check this if you are an alumn of EIDE. If not please fill in your centre name'))
	fecha_desempleo = models.DateField(default=datetime.date.today, blank=True)
	
	empresa_nombre = models.CharField(_('Nombre de la empresa'),max_length=100, blank=True)
	empresa_puesto = models.CharField(_('Puesto en la empresa'),max_length=100, blank=True)
	empresa_actividad = models.CharField(_('Actividad de la empresa'),max_length=200, blank=True)
	
	registration_date = models.DateField(default=datetime.date.today, auto_now_add=True)
	
	accept_conditions = models.BooleanField(_('Accept the conditions'), help_text=_('You must accept the conditions to register'),default=True,blank=True)
	
	
	def send_confirmation_email(self):
		##Para el alumno
		subject = "Te has matriculado para un curso de HOBETUZ en EIDE"
		
		html_content = u"""

<div class="well">
    Acaba de realizar una solicitud de matrícula para: <br />
    %s 
</div>
"""%(self.curso,)
		
		message_body = html_content
		##send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [self.email])
		msg = EmailMultiAlternatives(subject, message_body, settings.DEFAULT_FROM_EMAIL, [self.email])
		msg.attach_alternative(html_content, "text/html")
		##msg.content_subtype = "html"
		#msg.send()
		 
		### Para los admins
		subject = "Hay una nueva matricula para Hobetuz %s"%self.curso
		message_body = u"""Se ha dado de alta una nueva matricula para el examen %s. 
Los datos son del alumno son: 
	Nombre: %s
	Apellidos: %s
	Telefono Fijo: %s
	Telefono Móvil: %s
	e-mail: %s
"""%(self.curso,self.name,self.surname,self.telephone,self.telephone2,self.email)
		#mail_admins(subject, message_body)
		
	def __unicode__(self):
		return "%s-%s"%(self.id,self.curso)
	def registration_name(self):
		#return "%s - %s, %s"%(self.exam,self.surname,self.name)
		#~ return "%s"%(self.exam)
		return self.__unicode__()
	#Antes de guardar ahaceos algunas cosas, como generar password y enviar un mail
	def save(self, *args, **kwargs):
		##We generate a random password
		if self.id is None:
			#We set de password, not used roght now
			self.password = ''.join([choice(letters) for i in xrange(6)])
			#We send a confirmation mail to te registrant and a advise mail to the admins
			self.send_confirmation_email()
		super(Registration, self).save(*args, **kwargs)
		
