# -*- coding: utf-8 -*-
from django import template
from django.utils.translation import ugettext as _

from suscriptor.models import UserProfile



register = template.Library()

@register.inclusion_tag("organizador/mis_tareas.html")
def show_tareas(user):
    suscriptor_profile = UserProfile.objects.get(user=user)
    tareas = suscriptor_profile.organizador_set.all()
    return {'mis_tareas': tareas,}
