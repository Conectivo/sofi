from detalle.models import Presentacion, Ponente, Evento
from django.shortcuts import render_to_response
from django.contrib.sites.models import Site
from django.template import RequestContext


from suscriptor.models import UserProfile


def show(request, id, template_name='evento/evento.html'):
    evento = Evento.objects.get(id=id)
    suscriptor_profile = UserProfile.objects.get(id=request.user.id)
    is_suscribed = suscriptor_profile.is_suscribed(evento)
    template = render_to_response(template_name, {'evento': evento, 'is_suscribed': is_suscribed, 'site_name': Site.objects.get(id=1).name}, context_instance=RequestContext(request))
    return template
