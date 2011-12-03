from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView

urlpatterns = patterns('apps.contacto.views',
    url(r'^$', 'contact', name = 'contacto'),
)