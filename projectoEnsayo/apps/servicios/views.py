from django.shortcuts import render_to_response
from django.template import RequestContext

def services(request):
	return render_to_response('base_services.html', 
	                        {'frase': 'no hay contenido para mostrar en servicios'},
	                        context_instance = RequestContext(request))
