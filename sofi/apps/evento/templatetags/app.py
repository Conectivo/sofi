# -*- coding: utf-8 -*-

from django import template
from django.conf import settings

register = template.Library()

def media_url():
        return settings.MEDIA_URL

def theme():
    return settings.THEME


register.simple_tag(media_url)
register.simple_tag(theme)