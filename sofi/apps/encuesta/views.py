from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from encuesta.forms import EncuestaForm
from certificado.models import CertificadoSuscriptor

def realizar(request, evento, key):
    
    try:
        suscriptor = CertificadoSuscriptor.objects.get(key=key)
    except Exception, error:
        suscriptor = None
    
    if suscriptor:
        evento_suscriptor = suscriptor.certificado.evento
        
        if str(evento_suscriptor.id) == evento and suscriptor.certificado.encuesta:
            
            if not request.POST:
                form = EncuestaForm()
                return render_to_response('encuesta/encuesta.html', {'evento': evento_suscriptor, 'form': form.as_table()})
            else:    
                form = EncuestaForm(request.POST)
                
                if form.is_valid():
                    form_update = form.save(commit=False)
                    form_update.evento = evento_suscriptor
                    form_update.suscriptor = suscriptor.suscriptor
                    form_update.save()
                    return HttpResponseRedirect('http://%s/certificado/descargar/%s/%s/'% (request.get_host(),evento, key))
                else:
                    return render_to_response('encuesta/encuesta.html', {'evento': evento_suscriptor, 'form': form.as_table()})
            
        
    raise Http404()