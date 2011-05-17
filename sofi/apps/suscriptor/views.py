from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.contrib.sites.models import Site
from evento.models import Evento
#from forms import SuscriptorForm
from models import Suscriptor, UserProfile
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect

@login_required
def suscribir(request, id_evento, template='suscriptor/suscriptor.html'):
    evento = Evento.objects.get(id=id_evento)
    
    suscriptor = UserProfile.objects.filter(user=request.user)
    if suscriptor:
        suscriptor = suscriptor.get()
        if suscriptor.nombre and suscriptor.apellido and suscriptor.cedula and suscriptor.nacionalidad:
            pass
        else:
            return HttpResponseRedirect('/profiles/edit/')
            #return direct_to_template(request, 'profiles/edit_profile.html')
    
     
    return render_to_response(template, { 'evento': evento, 'site_name': Site.objects.get(id=1).name}, context_instance=RequestContext(request))
  
def reporte(request, id_evento, template='suscriptor/reporte.html'):
    evento = Evento.objects.get(id=id_evento)
    suscriptores = Suscriptor.objects.filter(evento = id_evento)
    return render_to_response(template, {'suscriptores': suscriptores, 'evento': evento, 'site_name': Site.objects.get(id=1).name}, context_instance=RequestContext(request))
    