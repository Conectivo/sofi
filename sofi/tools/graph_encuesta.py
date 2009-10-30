#!/usr/bin/env python

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from encuesta.models import Encuesta
import os.path

RUTA = os.path.join(os.path.dirname(__file__))

    
def generar_encuesta(evento_id, evento_nombre):

    mucho = []
    suficiente = []
    poco = []
    nada = []
    total_encuestados = Encuesta.objects.count()
    
    
    for i in range(1,15):
        mucho.append(eval("Encuesta.objects.filter(evento=%s, item%s=1).count() * 100 / total_encuestados" % (evento_id, str(i))))
        suficiente.append(eval("Encuesta.objects.filter(evento=%s, item%s=2).count()  * 100 / total_encuestados" % (evento_id, str(i))))
        poco.append(eval("Encuesta.objects.filter(evento=%s, item%s=3).count()  * 100 / total_encuestados" % (evento_id, str(i))))
        nada.append(eval("Encuesta.objects.filter(evento=%s, item%s=4).count()  * 100 / total_encuestados" % (evento_id, str(i))))
    
    ind = np.arange(14)
    width = 0.2 
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    rects1 = ax.bar(ind, mucho, width, color='#bce925', linewidth=0.1)
    rects2 = ax.bar(ind+width, suficiente, width, color='#f0d900', linewidth=0.1)
    rects3 = ax.bar(ind+width*2, poco, width, color='#e85e00', linewidth=0.1)
    rects4 = ax.bar(ind+width*3, nada, width, color='#770000', linewidth=0.1)
    
    ax.set_ylabel('Encuestados')
    ax.set_title('Encuesta %s' % (evento_nombre))
    ax.set_xticks(ind+width)
    
    ax.set_yticks((0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
    ax.set_yticklabels(('0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'))
    
    ax.set_xticklabels( ('1.1', '1.2', '1.3', '2.1', '2.2','2.3', '2.4', '2.5', '3.1', '3.2','4.1', '4.2', '4.3', '5.1') )
    
    ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('Mucho', 'Suficiente', 'Poco', 'Nada') )
    
    plt.savefig('%s/../site_media/encuesta/files/%s.png' % (RUTA, evento_id), dpi=70)
    
    return '/site_media/encuesta/files/%s.png' % (evento_id)


