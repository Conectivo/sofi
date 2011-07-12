# -*- coding: utf-8 -*-

from django import template
from django.utils.translation import ugettext as _
import httplib, urllib
import json

register = template.Library()

@register.simple_tag
def slideshare(url):
    try:
        conn = httplib.HTTPConnection("www.slideshare.net")
        conn.request("GET", 'http://www.slideshare.net/api/oembed/2?url=%s&format=json&maxwidth=320' % (url))
        
        response = conn.getresponse()
        if response.status == 200:
            data = json.loads(response.read())
            return data['html']
        else:
            return "Error, %s" % (response.reason)
        conn.close()
        
    except:
        return "Error, url: %s" %(url)

