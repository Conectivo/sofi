# -*- coding: utf-8 -*-

from django.db import models
from evento.models import Evento
from tools.thumbs import ImageWithThumbsField
from django.utils.translation import ugettext as _

class Presentacion(models.Model):
    titulo = models.CharField(max_length=120, verbose_name=_(u'título'))
    descripcion = models.TextField(blank=True, verbose_name=_(u'descripción'))
    lugar = models.TextField(blank=True, verbose_name=_(u'lugar'))
    fecha = models.DateField(verbose_name=_(u'fecha'))
    hora = models.TimeField(verbose_name=_(u'hora'))
    url = models.URLField(blank=True, verify_exists=False)
    evento = models.ManyToManyField(Evento, verbose_name=_(u'evento'))
    archivo = models.FileField(upload_to='detalle/files', blank=True, verbose_name=_(u'archivo'))
    
    def ponentes(self):
        nombre = ""
        for i in Ponente.objects.filter(presentacion=self.pk):
            nombre += i.nombre + ", "
        return nombre
    
    def eventos(self):
        eventos = ""
        for i in self.evento.all():
            eventos += str(i) + ", "
        return eventos
        
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        ordering = ['fecha', 'hora']
        verbose_name = _(u'Presentación')
        verbose_name_plural = _(u'Presentaciones')



class Ponente(models.Model):
    nombre = models.CharField(max_length=42, verbose_name=_(u'nombre'))
    profesion = models.CharField(max_length=21, blank=True, verbose_name=_(u'profesión'))
    email = models.EmailField()
    foto = ImageWithThumbsField(upload_to='detalle/files', blank=True, sizes=((80,100),), verbose_name=_(u'foto'))
    institucion = models.CharField(max_length=50, blank=True, verbose_name=_(u'institución'))
    curriculum = models.TextField(blank=True, verbose_name=_('curriculum'))
    estado = models.CharField(max_length=15, blank= True, verbose_name=_(u'estado'))
    pais = models.CharField(max_length=10, verbose_name=_(u'país'))
    presentacion = models.ManyToManyField(Presentacion, verbose_name=_(u'presentación'))
    
    

    def eventos(self):
        nombre = ""
        for i in self.presentacion.all():
            nombre += str(i.evento) + ", "
        return nombre
    
    def presentaciones(self):
        nombre = ""
        for i in self.presentacion.all():
            nombre += str(i) + ", "
        return nombre
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = _(u'Ponente')
        verbose_name_plural = _(u'Ponentes')
        
        

