from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.clientes.views',
	url(r'^$', 'clientes', name = 'clientes'),
)