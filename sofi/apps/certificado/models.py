# -*- coding: utf-8 -*-

from django.db import models
from evento.models import Evento
from suscriptor.models import Suscriptor
import md5
import random
from tools import email as email_tools
from django.conf import settings
from django.contrib.sites.models import Site

SINO = (
    (True, 'Si'),
    (False, 'No')
)

class Certificado(models.Model):
    imagen_de_fondo = models.ImageField(upload_to='certificado/files')
    evento = models.ForeignKey(Evento, unique=True)
    encuesta = models.BooleanField(choices=SINO)
    posicion_x_nombre = models.IntegerField()
    posicion_y_nombre = models.IntegerField()
    posicion_x_key = models.IntegerField()
    posicion_y_key = models.IntegerField()
    
    
    def save(self, force_insert=False, force_update=False):
        super(Certificado, self).save(force_insert, force_update)
        self.__agregaCertificadoSuscriptor()
        

    def __unicode__(self):
        return self.imagen_de_fondo.url

    def __agregaCertificadoSuscriptor(self):
        lista_suscritos = Suscriptor.objects.filter(evento=self.evento)
        
        
        for i in lista_suscritos:
            suscriptor = i
            key = md5.md5("%s%s" % (i.nombre_completo(), str(random.randrange(1000, 1000000000)))).hexdigest()
            certificado = self
            certificado_suscriptor = CertificadoSuscriptor(suscriptor=suscriptor, key=key, certificado=certificado, otorgar=False)
            certificado_suscriptor.save()
            
    
class CertificadoSuscriptor(models.Model):
    suscriptor = models.ForeignKey(Suscriptor, editable=False)
    key = models.CharField(max_length=32, editable=False)
    certificado = models.ForeignKey(Certificado, editable=False)
    otorgar = models.BooleanField(choices=SINO)
    

    def save(self, force_insert=False, force_update=False):
        if self.otorgar:
            email = self.suscriptor.email
            nombre = self.suscriptor.nombre_completo()
            evento = self.suscriptor.evento.nombre
            evento_id =  self.suscriptor.evento.id
            url = 'http://%s/certificado/descargar/%s/%s/' % (Site.objects.get(id=1).domain, evento_id, self.key)
            mensaje = u'Estimado(a) %s su certificado del evento "%s", puede descargarlo en el siguiente enlace:\n%s\n\nGracias por su participación...' % (nombre, evento, url)
            
            try:
                email_tools.enviar_mail(u'Certificado de asistencia a evento', mensaje, settings.DEFAULT_FROM_EMAIL, [email])
            except Exception, error:
                pass

        super(CertificadoSuscriptor, self).save(force_insert, force_update)
        
    
    def __unicode__(self):
        return self.suscriptor.nombre_completo()