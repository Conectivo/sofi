from django.db import models
from evento.models import Evento

class Suscriptor(models.Model):
    nombres = models.CharField(max_length=21)
    apellidos = models.CharField(max_length=21)
    cedula = models.IntegerField(max_length=8, verbose_name='c\xc3\xa9dula', unique=True)
    email = models.EmailField()
    profesion = models.CharField(max_length=21, blank=True, verbose_name='prefesi\xc3\xb3n')
    institucion = models.CharField(max_length=50, blank=True, verbose_name='instituci\xc3\xb3n')
    estado = models.CharField(max_length=15)
    pais = models.CharField(max_length=10, verbose_name='pa\xc3\xads')
    evento = models.ForeignKey(Evento)
    

    def __unicode__(self):
        return "%s %s" % (self.nombres, self.apellidos)
    
