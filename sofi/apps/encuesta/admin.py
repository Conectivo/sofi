#!/usr/bin/env python
from encuesta.models import Encuesta
from django.contrib import admin

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('suscriptor', 'evento', 'fecha')
    list_filter = ('evento',)
    search_fields = ('^suscriptor__nombres', '^suscriptor__apellidos')
    
admin.site.register(Encuesta, EncuestaAdmin)


