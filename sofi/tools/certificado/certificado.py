#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ImageFont, ImageDraw, Image, sys, StringIO
import md5

"""from tools.certificado.certificado import Certificado
a = Certificado()
b = a.generar('/home/olivaresa/Desktop/fondocertificados.png', 10, 10, 'alexander', '1265487')"""
 
class Certificado():
    def __init__(self):
        self.font_suscriptor = ImageFont.truetype("tools/certificado/font/DejaVuSans-Bold.ttf", 40)
        self.font_serial = ImageFont.truetype("tools/certificado/font/DejaVuSans.ttf", 10)
        self.directorio = False
    
    def generar(self, certificado, suscriptor, suscriptor_xy, key, key_xy):
        fuente = Image.open(certificado)
        fuente = fuente.convert('RGB')
        draw = ImageDraw.Draw(fuente)
        draw.text((suscriptor_xy[0],suscriptor_xy[1]), suscriptor, font=self.font_suscriptor, fill="blue")
        draw.text((key_xy[0],key_xy[1]), key, font=self.font_serial, fill="black")

        certificado = StringIO.StringIO()
        fuente.save(certificado, 'PDF')
        return certificado.getvalue()
        
