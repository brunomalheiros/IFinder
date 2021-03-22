from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    turma = models.CharField('Turma', max_length=10)
    whatsapp = models.CharField('Whatsapp', max_length=15)


    def __str__(self):
        return self.usuario.username