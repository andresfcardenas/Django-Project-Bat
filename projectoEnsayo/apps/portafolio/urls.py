from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.portafolio.views',
	url(r'^$', 'portafolio', name = 'portafolio'),
)