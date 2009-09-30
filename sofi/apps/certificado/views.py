# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from evento.models import Evento
from certificado.models import CertificadoSuscriptor
from tools.certificado.certificado import Certificado
import os


def descargar(request, evento, key, encuesta=None):
    
    certificado =  CertificadoSuscriptor()
    try:
        suscriptor = CertificadoSuscriptor.objects.get(key=key)
    except Exception, error:
        suscriptor = None
    
    if suscriptor and suscriptor.otorgar:
        if suscriptor.certificado.evento.id == int(evento):
            gen_certificado = Certificado()
            url = os.getcwd() + suscriptor.certificado.imagen_de_fondo.url
            nombre_suscriptor = suscriptor.suscriptor.nombre_completo()
            key = suscriptor.key
            pdf = gen_certificado.generar(url, nombre_suscriptor, (10,10), key, (100,100))
            response = HttpResponse(mimetype='application/pdf')
            response['Content-Disposition'] = ('attachment; filename=%s.pdf' % key)
            response.write(pdf)
            return response


    raise Http404()
    
