from django import forms
from django.forms import widgets
from .models import Tecnico

class TecnicoForm(forms.ModelForm):

    class Meta:
        model = Tecnico
        fields = '__all__'
        widgets = {
            'DNI': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'service_hours': forms.TextInput(attrs={'class': 'form-control'}),
        }