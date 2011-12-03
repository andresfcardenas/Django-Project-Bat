from django.shortcuts import render_to_response
from django.template import RequestContext

def portafolio(request):
	return render_to_response('base_portafolio.html', 
	                        {'frase': 'no hay contenido para mostrar en portafolio'},
	                        context_instance = RequestContext(request))