from email.policy import default
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=200)
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Indefinido")
    )
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False, default=True)
    nascimento = models.DateField()
    
    
    def __str__(self):
        return "{}, ({})".format(self.nome, self.sobrenome)

    #para redirecionar a pagina para a home após o cadastro.
    def get_absolute_url(self):
        return reverse('forum:home')





