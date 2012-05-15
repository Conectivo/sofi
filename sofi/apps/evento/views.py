import datetime

from django.shortcuts import render_to_response
from django.contrib.sites.models import Site
from django.template import RequestContext
from django.conf import settings

from evento.models import Evento

def index(request, pagina=1, template_name='evento/index.html'):
    fecha_hoy = datetime.date.today()
    # Obtenemos los eventos activos a la fecha
    eventos = Evento.get_active()
    template = render_to_response(template_name, {'eventos': eventos, 'site_name': Site.objects.get(id=1).name, 'fecha_hoy': fecha_hoy}, context_instance=RequestContext(request))
    return template
