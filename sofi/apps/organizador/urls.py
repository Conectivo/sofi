from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^mis_tareas/$', direct_to_template, {'template': 'organizador/tareas.html'}),
    #url(r'^mis_tareas/$', 'organizador.views.tareas'),
)
