# -*- coding: utf-8 -*-
from django.db import models
from evento.models import Evento
from suscriptor.models import Suscriptor

MSPN = (
    (1, 'Mucho'),
    (2, 'Suficiente'),
    (3, 'Poco'),
    (4, 'Nada'),
)

    
class Encuesta(models.Model):
    item1 = models.IntegerField(verbose_name="1.1 Los contenidos desarrollados han sido pertinentes y coherentes a la temática planteada para el evento", choices=MSPN)
    item2 = models.IntegerField(verbose_name="1.2 Los contenidos manejados son aportes adecuados a la consolidación de la idea del Conocimiento Libre", choices=MSPN)
    item3 = models.IntegerField(verbose_name="1.3 Los contenidos expuestos constituyen herramienta de reforzamiento de la reflexión sobre la temática del Conocimiento Libre y Licenciamiento en América Latina", choices=MSPN)

    item4 = models.IntegerField(verbose_name="2.1 Los medios empleados han facilitado la interacción entre los participantes, conferencistas y ponentes", choices=MSPN)
    item5 = models.IntegerField(verbose_name="2.2 Considera idoneos los medios empleados para promover la interacción entre los participantes", choices=MSPN)
    item6 = models.IntegerField(verbose_name="2.3 La moderación permitio la interacción de todos los participantes", choices=MSPN)
    item7 = models.IntegerField(verbose_name="2.4 La posibilidad de seguimiento del evento mediante actividades diferidas a través del canal video, archivos de audio facilito su participación en el evento", choices=MSPN)
    item8 = models.IntegerField(verbose_name="2.5 Emplear herramientas web, como la utilizadas en el evento democratiza el acceso a la información", choices=MSPN)

    item9 = models.IntegerField(verbose_name="3.1 Considera usted que los medios empleados para informarle de las actividades fueron efectivos", choices=MSPN)
    item10 = models.IntegerField(verbose_name="3.2 La antelación con que recibió la información le facilitó su participación en las  mismas", choices=MSPN)

    item11 = models.IntegerField(verbose_name="4.1 El empleo de tecnologías no-libres fué un obstaculo para su participación", choices=MSPN)
    item12 = models.IntegerField(verbose_name="4.4 La plataforma del evento estuvo disponible durante todo el tiempo en que se desarrollo el evento", choices=MSPN)
    item13 = models.IntegerField(verbose_name="4.5 Fue sencillo el acceso a las herramientas empleadas para el desarrollo del evento (blog, inscripciones, aulavirtual, foros, canales de tv, repositorios de audio)", choices=MSPN)
    
    item14 = models.IntegerField(verbose_name="5 Calificaría usted el desarrollo general del evento como un accionar colaborativo y cooperativo que ha generado insumos a la construcción de la idea del Conocimiento como Bien Público en América Latina", choices=MSPN)
    
    fecha = models.DateField()
    suscriptor = models.ForeignKey(Suscriptor)
    evento = models.ForeignKey(Evento)
    
    def __unicode__(self):
        return self.evento.nombre