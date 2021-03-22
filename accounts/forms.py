from django import forms 
from .models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'********'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder':'********'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-input'}),
            'email': forms.EmailInput(attrs={'class':'form-input'}),
            'first_name': forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class':'form-input'}),
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['Turma', 'whatsapp',]
        widgets = {
            'Turma': forms.TextInput(attrs={'class':'form-input', 'placeholder':''}),
            'whatsapp': forms.TextInput(attrs={'class':'form-input', 'placeholder':'(77)98888-8888'}),
        }