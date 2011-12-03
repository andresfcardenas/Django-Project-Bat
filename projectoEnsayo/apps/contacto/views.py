from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']
			email = form.cleaned_data['email']
			mensaje = form.cleaned_data['mensaje']			

			recipients = ['akardenasjimenez@gmail.com']
			
			from django.core.mail import send_mail
			send_mail('correo de sitio', mensaje, nombre, recipients)
			return HttpResponseRedirect('/home/')
	else:
		form = ContactForm()
	
	return render_to_response('base_contact.html',
	                        {'form': form,}, 
	                        context_instance=RequestContext(request))

