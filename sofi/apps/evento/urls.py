from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^$', 'evento.views.index', name="evento"),
    url(r'^(\d+)/$', 'evento.views.index', name="evento"),
)
