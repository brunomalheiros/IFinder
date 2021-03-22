from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Objeto(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    localencontrado = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='image/', blank=True, null=True, default='')
    
    
    def __str__(self):
        return self.nome

