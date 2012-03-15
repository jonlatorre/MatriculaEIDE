from django.contrib.auth.decorators import login_required, permission_required

from django.template.loader import render_to_string
from django.template import RequestContext

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

import StringIO
import ho.pisa as pisa


from models import *

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def ver(request, pk, password):
	matricula = get_object_or_404(Matricula, id=pk, password=password)
	

@login_required
def imprimir_matricula(request, pk):
	logger.debug("Vamos a imprimir")
	matricula = Matricula.objects.get(id=pk)
	payload = {'matricula': matricula}
	file_data = render_to_string('matricula/imprimir.pdf', payload, RequestContext(request))
	myfile = StringIO.StringIO()
	pisa.CreatePDF(file_data, myfile)
	myfile.seek(0)
	response =  HttpResponse(myfile, mimetype='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=matricula-%s.pdf'%matricula.id
	return response
