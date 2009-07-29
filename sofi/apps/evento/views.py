from evento.models import Evento
from django.shortcuts import render_to_response
from django.contrib.sites.models import Site
#Libreria que nos va a permitir realizar la paginacion
from django.core.paginator import Paginator, InvalidPage, EmptyPage

EVENTOS_PAG = 5

def listEventos(request, pagina=1, template_name='evento/evento.html'):
    
    #Obtenemos los objetos de la clase Evento y los paginamos de EVENTOS_PAG por pagina
    paginador = Paginator(Evento.objects.all(), EVENTOS_PAG)
    #Esta variable almacena el rango de las paginas encontradas
    rango_paginas = paginador.page_range

    eventos = paginador.page(pagina)
    
    #Enviamos la variable evento que contiene los eventos de la pagina seleccionada
    template = render_to_response(template_name, {'eventos': eventos,'rango_paginas':rango_paginas, 'site_name': Site.objects.get(id=1).name})
    return template
