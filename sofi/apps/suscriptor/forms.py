# -*- coding: utf-8 -*-

from django import forms
from models import Suscriptor
from django.shortcuts import render_to_response
from tools import email
from django.contrib.sites.models import Site
from django.template import RequestContext

class SuscriptorForm(forms.Form):
    nombres = forms.CharField(max_length=21, widget=forms.TextInput(attrs={'size':'21'}))
    apellidos = forms.CharField(max_length=21, widget=forms.TextInput(attrs={'size':'21'}))
    cedula = forms.IntegerField(label='Cédula / #ID', widget=forms.TextInput(attrs={'size':'12'}), min_value=2000000, max_value=999999999999)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=21, label='Profesión', widget=forms.TextInput(attrs={'size':'21'}), required=False)
    institucion = forms.CharField(max_length=50, label='Institución', widget=forms.TextInput(attrs={'size':'50'}), required=False)
    estado = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'size':'15'}), label='Estado / Región')
    pais = forms.ChoiceField(label='País')
    comida = forms.BooleanField(label = 'Requiere comida', required=False)
    transporte = forms.BooleanField(label = 'Requiere transporte', required=False)
    hospedaje = forms.BooleanField(label = 'Requiere hospedaje', required=False)
    

    def save(self, evento):
        suscriptor = Suscriptor(nombres=self.cleaned_data['nombres'], apellidos=self.cleaned_data['apellidos'],
                                cedula=self.cleaned_data['cedula'], email=self.cleaned_data['email'],
                                profesion=self.cleaned_data['profesion'], institucion= self.cleaned_data['institucion'],
                                estado=self.cleaned_data['estado'], pais=self.cleaned_data['pais'], comida=self.cleaned_data['comida'],hospedaje=self.cleaned_data['hospedaje'], transporte=self.cleaned_data['transporte'],evento=evento)
        
        if not Suscriptor.objects.filter(cedula=self.cleaned_data['cedula'], evento=evento):
            suscriptor.save()
            
            try:
                email.enviar_mail(u'Suscripción a evento', u'Estimado(a) %s %s su suscripción al evento %s en http://%s, se ha realizado con Éxito.\n\ngracias...' % (self.cleaned_data['nombres'], self.cleaned_data['apellidos'], evento, Site.objects.get(id=1).domain), evento.email, [self.cleaned_data['email']])
            except Exception, error:
                pass
            finally:
                return render_to_response('suscriptor/registro_ok.html', {'evento': evento, 'ok': True, 'site_name': Site.objects.get(id=1).name}, context_instance=RequestContext(request))
        else:
            return render_to_response('suscriptor/registro_ok.html', {'evento': evento, 'site_name': Site.objects.get(id=1).name}, context_instance=RequestContext(request))

    

