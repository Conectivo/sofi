# -*- coding: utf-8 -*-

from django.db import models
from tools.thumbs import ImageWithThumbsField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import Signal
from datetime import datetime
from tools.constantes import SINO

class Evento(models.Model):
    nombre = models.CharField(max_length=120)
    resumen = models.TextField()
    lugar = models.TextField(blank=True)
    email = models.EmailField()
    cta_twitter = models.CharField(max_length=50, blank=True, verbose_name=_(u'twitter'))
    pass_twitter = models.CharField(max_length=12, blank=True, verbose_name=_(u'contraseña twitter'))
    cta_facebook = models.CharField(max_length=50, blank=True, verbose_name=_(u'facebook'))
    pass_facebook = models.CharField(max_length=12, blank=True, verbose_name=_(u'contraseña facebook'))
    publicar_tf = models.BooleanField(choices=SINO, verbose_name=_(u'publicar en redes sociales'))
    presentaciones = models.BooleanField(choices=SINO)
    suscripciones = models.BooleanField(choices=SINO)
    publicar = models.BooleanField(choices=SINO)
    comentario = models.BooleanField(default=True)
    fecha = models.DateField(verbose_name=_(u'fecha publicación'))
    fecha_ini = models.DateField(verbose_name=_('fecha inicial'))
    fecha_fin = models.DateField(verbose_name=_('fecha final'))
    logo = ImageWithThumbsField(upload_to='evento/files', sizes=((180,150),))
    admin = models.ForeignKey(User)

    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-fecha_ini', '-fecha_fin']



    
     

usuario = None

def get_user(sender, instance, signal, * args, **kwargs):
    global usuario
    usuario = instance

def guardar(sender, instance, signal, * args, **kwargs):
    instance.fecha = datetime.now()
    instance.admin = usuario
    
signals.post_init.connect(get_user, User)    
signals.pre_save.connect(guardar, Evento)


