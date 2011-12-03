from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.servicios.views',
    url(r'^$', 'services', name = 'servicios'),
)