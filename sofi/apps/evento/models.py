# -*- coding: utf-8 -*-

import datetime

from django.db import models
from tools.thumbs import ImageWithThumbsField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from tools.constantes import SINO
from django.db.models.signals import post_init


class Evento(models.Model):
    nombre = models.CharField(max_length=120, verbose_name=_(u'nombre'))
    resumen = models.TextField(verbose_name=_(u'resumen'))
    lugar = models.CharField(max_length=120, verbose_name=_(u'lugar'))
    direccion = models.TextField(verbose_name=_(u'dirección'))
    email = models.EmailField()
    fecha = models.DateField(verbose_name=_(u'fecha publicación'))
    fecha_ini = models.DateField(verbose_name=_(u'fecha inicial'))
    fecha_fin = models.DateField(verbose_name=_(u'fecha final'))
    logo = ImageWithThumbsField(upload_to='evento/files', sizes=((180,150),), help_text=_('Imagen de 940x280 pixels'))
    cta_twitter = models.CharField(max_length=50, blank=True, verbose_name=_(u'twitter'))
    pass_twitter = models.CharField(max_length=12, blank=True, verbose_name=_(u'contraseña twitter'))
    cta_facebook = models.CharField(max_length=50, blank=True, verbose_name=_(u'facebook'))
    pass_facebook = models.CharField(max_length=12, blank=True, verbose_name=_(u'contraseña facebook'))
    publicar_tf = models.BooleanField(choices=SINO, verbose_name=_(u'publicar en redes sociales'))
    presentaciones = models.BooleanField(choices=SINO, verbose_name=_(u'presentaciones'))
    suscripciones = models.BooleanField(choices=SINO, verbose_name=_(u'suscripciones'))
    suscripcionesd = models.BooleanField(choices=SINO, verbose_name=_(u'suscripciones durante el evento'))
    publicar = models.BooleanField(choices=SINO, verbose_name=_(u'publicar'))
    comentario = models.BooleanField(default=True, verbose_name=_(u'comentarios'))
    media_video = models.URLField(blank=True, verbose_name=_(u'Vídeo'))
    admin = models.ForeignKey(User)


    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['-fecha_ini', '-fecha_fin']

    @staticmethod
    def get_active():
        return Evento.objects.filter(fecha_fin__gte=datetime.date.today())

