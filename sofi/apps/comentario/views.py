from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from evento.models import Evento

def comentario(request, evento):
    if Evento.objects.filter(id=evento):
        evento = Evento.objects.get(id=evento)
        return render_to_response('comentario/comentario.html', {'evento': evento})
    else:
        raise Http404
    
