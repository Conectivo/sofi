from evento.models import Evento
from django.contrib import admin

class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_ini', 'fecha_fin', 'presentaciones', 'suscripciones','publicar']
    search_fields = ['nombre', 'fecha_ini']
    exclude = ('fecha', 'admin')
    
admin.site.register(Evento, EventoAdmin)
