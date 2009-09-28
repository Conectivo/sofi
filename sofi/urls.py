from django.conf.urls.defaults import *
from django.conf import settings
import os
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from tools.feed import Rss, Atom

feeds = {
    'rss': Rss,
    'atom': Atom,
}


admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('evento.urls')),
    (r'^detalle/', include('detalle.urls')),
    (r'^suscriptor/', include('suscriptor.urls')),
    (r'^acercade/', direct_to_template, {'template': 'acercade/acercade.html'}),
    (r'^licencia/', direct_to_template, {'template': 'acercade/licencia.html'}),
    (r'^admin/(.*)', admin.site.root),
    (r'^feed/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^certificado/', include('certificado.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "site_media")}),
    )
