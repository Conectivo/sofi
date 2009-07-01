from django import forms
from models import Suscriptor
from django.shortcuts import render_to_response
from tools import email
from django.conf import settings
from django.contrib.sites.models import Site

class SuscriptorForm(forms.Form):
    nombres = forms.CharField(max_length=21, widget=forms.TextInput(attrs={'size':'21'}))
    apellidos = forms.CharField(max_length=21, widget=forms.TextInput(attrs={'size':'21'}))
    cedula = forms.IntegerField(label='C\xc3\xa9dula', widget=forms.TextInput(attrs={'size':'8'}), min_value=2000000, max_value=90000000)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=21, label='Profesi\xc3\xb3n', widget=forms.TextInput(attrs={'size':'21'}), required=False)
    institucion = forms.CharField(max_length=50, label='Instituci\xc3\xb3n', widget=forms.TextInput(attrs={'size':'50'}), required=False)
    estado = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'size':'15'}))
    pais = forms.CharField(max_length=10, label='Pa\xc3\xads', widget=forms.TextInput(attrs={'size':'10'}))
    
    def save(self, evento):
        suscriptor = Suscriptor(nombres=self.cleaned_data['nombres'], apellidos=self.cleaned_data['apellidos'],
                                cedula=self.cleaned_data['cedula'], email=self.cleaned_data['email'],
                                profesion=self.cleaned_data['profesion'], institucion= self.cleaned_data['institucion'],
                                estado=self.cleaned_data['estado'], pais=self.cleaned_data['pais'], evento=evento)
        
        if not Suscriptor.objects.filter(cedula=self.cleaned_data['cedula']):
            suscriptor.save()
            
            email.enviar_mail('Suscripcion a evento', u'Estimado(a) %s %s su suscripci\xc3\xb3n al evento %s en http://%s, se ha realizado con \xc3\xa9xito.\n\ngracias...' % (self.cleaned_data['nombres'], self.cleaned_data['apellidos'], evento, Site.objects.get(id=1).domain), settings.DEFAULT_FROM_EMAIL, [self.cleaned_data['email']])
            
            return render_to_response('suscriptor/registro_ok.html', {'evento': evento, 'ok': True, 'site_name': Site.objects.get(id=1).name})
        else:
            return render_to_response('suscriptor/registro_ok.html', {'evento': evento, 'site_name': Site.objects.get(id=1).name})

    

