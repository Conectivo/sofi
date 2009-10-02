#!/usr/bin/env python
from encuesta.models import Encuesta
from django.contrib import admin

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('evento', 'suscriptor', 'fecha')
    list_filter = ('evento',)
    
admin.site.register(Encuesta, EncuestaAdmin)


