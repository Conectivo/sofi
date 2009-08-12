from evento.models import Evento
from django.contrib import admin

class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'presentaciones', 'suscripciones','publicar', 'fecha_ini']
    search_fields = ['nombre', 'fecha_ini']

admin.site.register(Evento, EventoAdmin)
