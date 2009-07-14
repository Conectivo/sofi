from django.db import models
from tools.thumbs import ImageWithThumbsField

SINO = (
    (True, 'Si'),
    (False, 'No')
)

class Evento(models.Model):
    nombre = models.CharField(max_length=120)
    resumen = models.TextField()
    lugar = models.TextField(blank=True)
    presentaciones = models.BooleanField(choices=SINO)
    suscripciones = models.BooleanField(choices=SINO)
    publicar = models.BooleanField(choices=SINO)
    fecha_ini = models.DateField(verbose_name='fecha inicial')
    fecha_fin = models.DateField(verbose_name='fecha final')
    #logo = models.ImageField(upload_to='evento/files')
    logo = ImageWithThumbsField(upload_to='evento/files', sizes=((180,150),))

    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ['-fecha_ini', '-fecha_fin']

