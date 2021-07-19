from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Objeto(models.Model):

    STATUS = (
        ('Perdido', 'Perdido'),
        ('Encontrado', 'Encontrado'),
       
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=200)
    localencontrado = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='image/', blank=True, null=True, default='')
    status = models.CharField('Categoria', max_length=15, choices=STATUS)
    
    
    
    def __str__(self):
        return self.nome

