#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ImageFont, ImageDraw, Image, sys, StringIO
import md5
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape

class Certificado():
    def __init__(self):
        self.font_suscriptor = ImageFont.truetype("tools/certificado/font/DejaVuSans-Bold.ttf", 40)
        self.font_id = ImageFont.truetype("tools/certificado/font/DejaVuSans-Bold.ttf", 25)
        self.font_serial = ImageFont.truetype("tools/certificado/font/DejaVuSans.ttf", 10)
        self.directorio = False
    
    def generar(self, certificado, suscriptor, suscriptor_xy, id, id_xy, key, key_xy, tematica):
        fuente = Image.open(certificado)
        fuente = fuente.convert('RGB')
        draw = ImageDraw.Draw(fuente)
        draw.text((suscriptor_xy[0],suscriptor_xy[1]), suscriptor, font=self.font_suscriptor, fill="blue")
        draw.text((id_xy[0],id_xy[1]), id, font=self.font_id, fill="blue")
        draw.text((key_xy[0],key_xy[1]), key, font=self.font_serial, fill="black")

        certificado = StringIO.StringIO()
        
        pdf = canvas.Canvas(certificado, landscape(letter), bottomup=50)
        pdf.drawInlineImage(fuente,0,0)
        pdf.showPage()
        tematica_pdf = pdf.beginText(50,562)
        tematica_pdf.textLines(tematica.splitlines())
        pdf.drawText(tematica_pdf)
        pdf.drawString(key_xy[0],10, key)
        pdf.showPage()
        pdf.save()
        return certificado.getvalue()
        
