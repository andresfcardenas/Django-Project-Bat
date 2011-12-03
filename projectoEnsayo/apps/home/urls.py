from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.home.views',
    url(r'^$', 'home', name = 'home'),
)