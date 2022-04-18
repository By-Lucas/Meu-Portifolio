from os import link
from django.db import models
from ..models import linguagems_progr

class projeto(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    img_projeto = models.FileField(upload_to='projetos', null=True, blank=True)
    tecnologias = models.ManyToManyField(linguagems_progr, null=True, blank=True)
    link_github = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome