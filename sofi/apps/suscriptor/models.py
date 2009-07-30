# -*- coding: utf-8 -*-

from django.db import models
from evento.models import Evento

class Suscriptor(models.Model):
    nombres = models.CharField(max_length=21)
    apellidos = models.CharField(max_length=21)
    cedula = models.DecimalField(verbose_name='cédula', unique=True, max_digits=12, decimal_places=0)
    email = models.EmailField()
    profesion = models.CharField(max_length=21, blank=True, verbose_name='profesión')
    institucion = models.CharField(max_length=50, blank=True, verbose_name='institución')
    estado = models.CharField(max_length=15)
    pais = models.CharField(max_length=58, verbose_name='país')
    evento = models.ForeignKey(Evento)
    

    def __unicode__(self):
        return "%s %s" % (self.nombres, self.apellidos)
    
    class Meta:
        ordering = ['pais', 'nombres', 'apellidos']
