# -*- coding: utf-8 -*-
from django.db import models
from evento.models import Evento
#from suscriptor.models import Suscriptor
from suscriptor.models import Suscriptores as Suscriptor
from suscriptor.models import UserProfile
from django.utils.translation import ugettext as _

MSPN = (
    (1, _('Mucho')),
    (2, _('Suficiente')),
    (3, _('Poco')),
    (4, _('Nada')),
)

    
class Encuesta(models.Model):
    nombre = models.CharField(max_length=200)
    evento = models.ForeignKey(Evento)
    
    def __unicode__(self):
        return self.nombre
    
class Items(models.Model):
    nombre = models.CharField(max_length=200)
    encuesta = models.ForeignKey(Encuesta)

class Votacion(models.Model):
    fecha = models.DateField()
    respuesta = models.IntegerField(choices=MSPN)
    item = models.ForeignKey(Items)
    suscriptor = models.ForeignKey(UserProfile)
    