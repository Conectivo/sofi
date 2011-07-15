# -*- coding: utf-8 -*-
#from django.db import models

# Moderando comentarios
from django.db.models.signals import pre_save, post_save, post_init
from django.contrib.comments.models import Comment
from evento.models import Evento
from django.contrib.sites.models import Site
from tools import email
from django.utils.translation import ugettext as _

# Los comentarios no se publican automaticamente
def pre_save_comment(sender, instance, **kwargs):
    if not instance.id:
        instance.is_public = False

##Despues de cambiar el estado del comentario envia emails
def post_save_comment(sender, instance, **kwargs):

    
    site = Site.objects.get(id=1)

    #if instance.is_public:
    #    asunto = _('Comentario aprobado')
    #    para = [instance.user_email]
    #else:
    #    asunto = _(u'Nuevo comentario en lista de moderación')
    #    para =  [evento.email]
    #    
    #if instance.content_type.name == 'comment':
    #    comentario = Comment.objects.get(id=instance.object_pk)
    #    mensaje = ''
    #if instance.content_type.name == 'evento':
    #    evento = Evento.objects.get(id=instance.object_pk)
    #    mensaje = _('Su comentario sobre el evento') + '" ' + evento.nombre + '" ' + _('ha sido aprobado y publicado en:') + '\n' + site.domain + '/comentario/' +  evento.id + '/\n\n' + _('Gracias...')

    #try:
    #    email.enviar_mail(asunto, mensaje, evento.email, para)
    #except Exception, error:
    #    pass


pre_save.connect(pre_save_comment, sender=Comment)
post_save.connect(post_save_comment, sender=Comment)
    
