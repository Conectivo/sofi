# -*- coding: utf-8 -*-

from django.db import models
from evento.models import Evento
from tools.thumbs import ImageWithThumbsField

class Presentacion(models.Model):
    titulo = models.CharField(max_length=120, verbose_name='título')
    fecha = models.DateField()
    hora = models.TimeField()
    url = models.URLField(blank=True)
    lugar = models.TextField(blank=True)
    evento = models.ForeignKey(Evento)
    archivo = models.FileField(upload_to='detalle/files', blank=True)
    
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        ordering = ['fecha', 'hora']


class Ponente(models.Model):
    nombre = models.CharField(max_length=42)
    profesion = models.CharField(max_length=21, blank=True, verbose_name='profesión')
    email = models.EmailField()
    #foto = models.ImageField(upload_to='detalle/files', blank=True)
    foto = ImageWithThumbsField(upload_to='detalle/files', blank=True, sizes=((80,100),))
    institucion = models.CharField(max_length=50, blank=True, verbose_name='institución')
    estado = models.CharField(max_length=15, blank= True)
    pais = models.CharField(max_length=10, verbose_name='país')
    presentacion = models.ManyToManyField(Presentacion, verbose_name='presentación')
    
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        
        

