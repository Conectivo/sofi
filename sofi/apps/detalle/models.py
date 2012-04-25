# -*- coding: utf-8 -*-

from django.db import models
from evento.models import Evento
from tools.thumbs import ImageWithThumbsField
from django.utils.translation import ugettext as _
from suscriptor.models import UserProfile

class TipoPresentacion(models.Model):
    tipo = models.CharField(max_length=50, verbose_name=_(u'tipo de presentación'))

    def __unicode__(self):
        return self.tipo
    
    class Meta:
        ordering = ['tipo']
        verbose_name = _(u'Tipo de Presentación')
        verbose_name_plural = _(u'Tipo de Presentaciones')


class Presentacion(models.Model):
    titulo = models.CharField(max_length=120, verbose_name=_(u'título'))
    tipo = models.ForeignKey(TipoPresentacion, verbose_name=_(u'tipo de presentación'))
    descripcion = models.TextField(blank=True, verbose_name=_(u'descripción'))
    lugar = models.TextField(blank=True, verbose_name=_(u'lugar'))
    fecha = models.DateField(verbose_name=_(u'fecha'))
    hora = models.TimeField(verbose_name=_(u'hora'))
    url = models.URLField(blank=True, verify_exists=False)
    evento = models.ForeignKey(Evento, verbose_name=_(u'evento'))
    archivo = models.FileField(upload_to='detalle/files', blank=True, verbose_name=_(u'archivo'))
    media_slideshare = models.URLField(blank=True, verbose_name=_(u'Presentación SlideShare.net'))
    media_video = models.URLField(blank=True, verbose_name=_(u'Vídeo'))
    
    def ponente(self):
        nombre_ponente = ""
        for i in self.ponente_set.all():
            nombre_ponente += i.suscriptor.nombre_completo() + ", "
        return nombre_ponente
    
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        ordering = ['fecha', 'hora']
        verbose_name = _(u'Presentación')
        verbose_name_plural = _(u'Presentaciones')



class Ponente(models.Model):
    suscriptor = models.ForeignKey(UserProfile, verbose_name=_(u'suscriptor'))
    foto = ImageWithThumbsField(upload_to='detalle/files', blank=True, sizes=((80,100),), verbose_name=_(u'foto'))
    biografia = models.TextField(blank=True, verbose_name=_(u'biografía'))
    presentacion = models.ForeignKey(Presentacion, verbose_name=_(u'presentación'))
    
    
    def evento(self):
        return unicode(self.presentacion.evento)
    
    
    def __unicode__(self):
        return unicode(self.suscriptor)

    class Meta:
        ordering = ['suscriptor__user']
        verbose_name = _(u'Ponente')
        verbose_name_plural = _(u'Ponentes')
        
        

