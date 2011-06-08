# -*- coding: utf-8 -*-

from django.db import models
from tools.thumbs import ImageWithThumbsField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from tools.constantes import SINO
from django.db.models.signals import post_init

#USUARIO = None
#
#class AdminFilter(models.Manager):
#    def get_query_set(self):
#        admin = super(AdminFilter, self).get_query_set()
#        if USUARIO.is_superuser:
#            return admin
#        else:
#            return admin.filter(admin=User.objects.get(username=USUARIO))

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
    fecha_ini = models.DateField(verbose_name=_(u'fecha inicial'))
    fecha_fin = models.DateField(verbose_name=_(u'fecha final'))
    logo = ImageWithThumbsField(upload_to='evento/files', sizes=((180,150),))
    admin = models.ForeignKey(User)
    #objects = AdminFilter()
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-fecha_ini', '-fecha_fin']

#def get_user(sender, instance, *args, **kwargs):
#    global USUARIO
#    USUARIO = instance
#    
#post_init.connect(get_user, User)
    
     


