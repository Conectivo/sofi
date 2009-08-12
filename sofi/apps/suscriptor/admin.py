from suscriptor.models import Suscriptor
from django.contrib import admin

class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'cedula', 'email','evento']
    search_fields = ['nombres', 'apellidos', 'cedula', 'email']
    list_filter = ['evento']

admin.site.register(Suscriptor, SuscriptorAdmin)
