from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^registro/(\d+)/$', 'suscriptor.views.suscribir', name="suscriptor"),
    url(r'^reporte/(\d+)/$', 'suscriptor.views.reporte', name="reporte"),
)
