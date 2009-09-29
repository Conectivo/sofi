from django.db import models
from evento.models import Evento
from suscriptor.models import Suscriptor

class Encuesta(models.Model):
    comentario = models.TextField()
    suscriptor = models.ForeignKey(Suscriptor)
    evento = models.ForeignKey(Evento)
    
    def __unicode__(self):
        return self.evento.nombre