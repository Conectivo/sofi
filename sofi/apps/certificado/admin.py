#!/usr/bin/env python
from certificado.models import Certificado, CertificadoSuscriptor
from django.contrib import admin


class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'imagen_de_fondo', 'encuesta',)
    
admin.site.register(Certificado, CertificadoAdmin)

class CertificadoSuscriptorAdmin(admin.ModelAdmin):
    list_display = ('suscriptor', 'key', 'evento','certificado', 'otorgar',)
    list_filter = ('certificado',)
    
admin.site.register(CertificadoSuscriptor, CertificadoSuscriptorAdmin)
