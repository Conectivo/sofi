from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from encuesta.forms import EncuestaForm
from certificado.models import CertificadoSuscriptor
from encuesta.models import Encuesta
from datetime import datetime
from django.template import RequestContext

def realizar(request, evento, key):
    
    try:
        suscriptor = CertificadoSuscriptor.objects.get(key=key)
    except Exception, error:
        suscriptor = None
    
    if suscriptor:
        evento_suscriptor = suscriptor.certificado.evento
        
        if str(evento_suscriptor.id) == evento and suscriptor.certificado.encuesta:
            
            encuesta = Encuesta.objects.filter(suscriptor=suscriptor.suscriptor, evento=evento_suscriptor)

            if encuesta:
                return HttpResponseRedirect('http://%s/certificado/descargar/%s/%s/'% (request.get_host(),evento, key))
            
            if not request.POST:
                form = EncuestaForm()
                return render_to_response('encuesta/encuesta.html', {'evento': evento_suscriptor, 'form': form}, context_instance=RequestContext(request))
            else:    
                form = EncuestaForm(request.POST)
                
                if form.is_valid():
                    form_update = form.save(commit=False)
                    form_update.evento = evento_suscriptor
                    form_update.suscriptor = suscriptor.suscriptor
                    form_update.fecha = datetime.date(datetime.now())
                    form_update.save()
                    return HttpResponseRedirect('http://%s/certificado/descargar/%s/%s/'% (request.get_host(),evento, key))
                else:
                    return render_to_response('encuesta/encuesta.html', {'evento': evento_suscriptor, 'form': form}, context_instance=RequestContext(request))
            
        
    raise Http404()

def reporte(request, evento):
    import tools.graph_encuesta
    from evento.models import Evento
    
    if Evento.objects.filter(id=evento) and Encuesta.objects.filter(evento=evento):
        evento = Evento.objects.get(id=evento)
        url = tools.graph_encuesta.generar_encuesta(evento.id, evento.nombre)
        items = ""
        
        for i in range(1,15):
            items += Encuesta._meta.fields[i].verbose_name + "\n\n"

        return render_to_response('encuesta/reporte.html', {'evento': evento, 'items': items, 'grafico': url}, context_instance=RequestContext(request))
    else:
        raise Http404
