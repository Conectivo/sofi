# -*- coding: utf-8 -*-
from django.db import models
from evento.models import Evento
#from suscriptor.models import Suscriptor
from suscriptor.models import Suscriptores as Suscriptor
from suscriptor.models import UserProfile
from django.utils.translation import ugettext as _
from certificado.models import CertificadoSuscriptor
from tools.constantes import MSPN

class Encuesta(models.Model):
    descripcion = models.TextField()
    evento = models.ForeignKey(Evento)
    
    def __unicode__(self):
        return self.descripcion
    
class Items(models.Model):
    nombre = models.CharField(max_length=200)
    encuesta = models.ForeignKey(Encuesta)

class Votacion(models.Model):
    fecha = models.DateField()
    respuesta = models.IntegerField(choices=MSPN)
    item = models.ForeignKey(Items)
    key = models.ForeignKey(CertificadoSuscriptor)
    