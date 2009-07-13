from django.db import models
PUBLICAR = (
    (True, 'Si'),
    (False, 'No')
)

SUSCRIPCIONES = (
    (True, 'Si'),
    (False, 'No')
)

PRESENTACIONES = (
    (True, 'Si'),
    (False, 'No')
)

class Evento(models.Model):
    nombre = models.CharField(max_length=120)
    resumen = models.TextField()
    lugar = models.TextField(blank=True)
    presentaciones = models.CharField(max_length=4, choices=PRESENTACIONES)
    suscripciones = models.CharField(max_length=4, choices=SUSCRIPCIONES)
    publicar = models.CharField(max_length=4, choices=PUBLICAR)
    fecha_ini = models.DateField(verbose_name='fecha inicial')
    fecha_fin = models.DateField(verbose_name='fecha final')
    logo = models.ImageField(upload_to='evento/files')
    

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-fecha_ini', '-fecha_fin']

