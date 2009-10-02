#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encuesta.models import Encuesta
from django.forms import ModelForm

class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        exclude = ('suscriptor', 'evento', 'fecha')




