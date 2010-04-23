from detalle.models import Presentacion, Ponente
from django.contrib import admin

class PonenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'eventos', 'presentaciones')
    search_fields = ('nombre', 'email')
    
admin.site.register(Ponente, PonenteAdmin)

class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'eventos', 'ponentes')
    search_fields = ('titulo', 'fecha')
    list_filter = ['evento']

admin.site.register(Presentacion, PresentacionAdmin)