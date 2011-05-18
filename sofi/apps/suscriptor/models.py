# -*- coding: utf-8 -*-

from django.db import models
from evento.models import Evento
from django.contrib.auth.models import User, Group
from django.db.models import signals
from django.utils.translation import ugettext as _
from tools.constantes import NACIONALIDAD, SINO

# Creación del perfil luego del registro para evitar problemas
def user_post_save(sender, instance, **kwargs):
    profile, new = UserProfile.objects.get_or_create(user=instance)


class UserProfile(models.Model):
    user = models.ForeignKey(User,unique=True,verbose_name=_(u'Usuario'))
    nombre = models.CharField(max_length=21)
    apellido = models.CharField(max_length=21)
    cedula = models.CharField(verbose_name='ID', max_length=12)
    profesion = models.CharField(max_length=21, blank=True, verbose_name=_(u'profesión'))
    organizacion = models.CharField(max_length=50, blank=True, verbose_name=_(u'organizacion'))
    nacionalidad = models.CharField(max_length=58, verbose_name=_(u'nacionalidad'), choices=NACIONALIDAD)
    cta_twitter = models.CharField(max_length=50, blank=True, verbose_name=_(u'twitter'))
    cta_facebook = models.CharField(max_length=50, blank=True, verbose_name=_(u'facebook'))
    informacion = models.BooleanField(choices=SINO, verbose_name=_(u'recibir información'))

    class Admin():
        pass
    
    def __unicode__(self):
            return unicode("%s" % self.user.username)
    
    def nombre_completo(self):
        return "%s %s" % (self.nombre.title(), self.apellido.title())

    class Meta:
        verbose_name = _(u'Perfil')
        verbose_name_plural = _(u'Perfiles')
    
signals.post_save.connect(user_post_save, User)


class Suscriptores(models.Model):
    suscriptor = models.ForeignKey(UserProfile)
    evento = models.ForeignKey(Evento)
    
    def nombre_completo(self):
        return "%s %s" % (self.suscriptor.nombre.title(), self.suscriptor.apellido.title())
    
    def __unicode__(self):
        return "%s %s" % (self.suscriptor.nombre.title(), self.suscriptor.apellido.title())
    
    class Meta:
        ordering = ['suscriptor__nacionalidad', 'suscriptor__nombre', 'suscriptor__apellido']
        
