from django.db import models

# Create your models here.

class Objeto(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=225)
    descricao = models.TextField()
    localencontrado = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='image/', blank=True, null=True, default='')
    
    
    def __str__(self):
        return self.nome

