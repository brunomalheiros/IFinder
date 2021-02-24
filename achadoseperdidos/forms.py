from django import forms
from .models import Objeto
from django.forms import ModelForm

class ObjetoForm(forms.ModelForm):
    
    class Meta:

        model = Objeto

        fields = ('nome', 'descricao', 'localencontrado', 'imagem')

    