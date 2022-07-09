from django import forms
from .models import Servicios
from django.forms import fields


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = [
            'userCliente',
            'userTecnico',
            'tipoServicio',
            'costoServicio',
            'fecha',
            'especificacionesProblem'
        ]
