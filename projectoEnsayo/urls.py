from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectoEnsayo.views.home', name='home'),
    # url(r'^projectoEnsayo/', include('projectoEnsayo.foo.urls')),
    url(r'^clientes/', include('apps.clientes.urls')),
    url(r'^contacto/', include('apps.contacto.urls')),
    url(r'^$', include('apps.home.urls')),
    url(r'^home/', include('apps.home.urls')),
    url(r'^portafolio/', include('apps.portafolio.urls')),
    url(r'^servicios/', include('apps.servicios.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
