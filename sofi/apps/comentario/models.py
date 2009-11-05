# -*- coding: utf-8 -*-
#from django.db import models

# Moderando comentarios
from django.db.models.signals import pre_save, post_save, post_init
from django.contrib.comments.models import Comment
from evento.models import Evento
from django.contrib.sites.models import Site
from tools import email

# Los comentarios no se publican automaticamente
def pre_save_comment(sender, instance, **kwargs):
    if not instance.id:
        instance.is_public = False

#Despues de cambiar el estado del comentario envia emails
def post_save_comment(sender, instance, **kwargs):
    evento = Evento.objects.get(id=instance.object_pk)
    site = Site.objects.get(id=1)

    if instance.is_public:
        try:
            if instance.content_type.name == "evento":
                asunto = u'Comentario aprobado'
                mensaje = u'Su comentario sobre el evento "%s" ha sido aprobado y publicado en:\nhttp://%s/comentario/%s/\n\nGracias...' % (evento.nombre, site.domain, evento.id)
                email.enviar_mail(asunto, mensaje, evento.email, [instance.user_email])
                
        except Exception, error:
            pass
    else:
        try:
            if instance.content_type.name == "evento":
                asunto = u'Nuevo comentario en lista de moderación'
                mensaje = u'%s ha comentado el evento "%s":\n------\n%s\n------\nPara aprobar por favor haga click en la siguiente dirección:\nhttp://%s/admin/comments/comment/%s/' % (instance.user_name, evento.nombre, instance.comment, site.domain, instance.id)
                email.enviar_mail(asunto, mensaje, evento.email, [evento.email])
                
        except Exception, error:
            pass

pre_save.connect(pre_save_comment, sender=Comment)
post_save.connect(post_save_comment, sender=Comment)
    
