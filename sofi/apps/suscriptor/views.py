from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.contrib.sites.models import Site
from evento.models import Evento
from forms import SuscriptorForm
from models import Suscriptor
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def suscribir(request, id_evento, template='suscriptor/suscriptor.html'):
    evento = Evento.objects.get(id=id_evento)
    if request.method == "POST":

        form = SuscriptorForm(request.POST)
        
        if form.is_valid():
            return form.save(evento)
    else:
        from django.forms import widgets
        form = SuscriptorForm()
        if not evento.patrocinio:
            form.fields['comida'].widget = widgets.HiddenInput()
            form.fields['transporte'].widget = widgets.HiddenInput()
            form.fields['hospedaje'].widget = widgets.HiddenInput()
        
    return render_to_response(template, {'form': form, 'evento': evento, 'site_name': Site.objects.get(id=1).name}, context_instance=RequestContext(request))
  
def reporte(request, id_evento, template='suscriptor/reporte.html'):
    evento = Evento.objects.get(id=id_evento)
    suscriptores = Suscriptor.objects.filter(evento = id_evento)
    return render_to_response(template, {'suscriptores': suscriptores, 'evento': evento, 'site_name': Site.objects.get(id=1).name}, context_instance=RequestContext(request))
    