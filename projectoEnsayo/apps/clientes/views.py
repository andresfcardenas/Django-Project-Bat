from django.shortcuts import render_to_response
from django.template import RequestContext

def clientes(request):
	return render_to_response('base_clientes.html', 
	                        {'frase': 'no hay contenido para mostrar en clientes'},
	                        context_instance = RequestContext(request))