#!/usr/bin/env python
from encuesta.models import Encuesta, Items
from django.contrib import admin

class ItemsInline(admin.TabularInline):
    model = Items


class EncuestaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'evento')
    list_filter = ('evento',)
    #search_fields = ('^suscriptor__nombres', '^suscriptor__apellidos')

    inlines = [
            ItemsInline,
        ]
    
admin.site.register(Encuesta, EncuestaAdmin)


