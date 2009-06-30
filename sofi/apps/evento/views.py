from evento.models import Evento
from django.shortcuts import render_to_response
from django.contrib.sites.models import Site

def listEventos(request, template_name='evento/evento.html'):
    lista_eventos = Evento.objects.all()
    template = render_to_response(template_name, {'lista_eventos': lista_eventos, 'site_name': Site.objects.get(id=1).name})
    return template