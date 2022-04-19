from django.db import models

class linguagens_mais_usadas(models.Model):
    NIVEL_1 = (
        ('B', 'Basico'),
        ('M', 'Intermediario'),
        ('A', 'Avancado'),
    )
    img_ling_1 = models.ImageField(upload_to ='media/img_linguagem/')
    nome_1 = models.CharField(max_length=50, null=True)
    nivel_conhecimento_1 = models.CharField(max_length=50, choices=NIVEL_1, null=True)
    descricao_1 = models.TextField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.nome_1

class linguagems_progr(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('M', 'Intermediario'),
        ('A', 'Avancado'),
    )

    img_ling = models.ImageField(upload_to ='media/img_linguagem/')
    nome = models.CharField(max_length=50, null=True)
    nivel_conhecimento = models.CharField(max_length=50, choices=NIVEL, null=True)
    descricao = models.TextField(max_length=500, null=True)

    def __str__(self) -> str:
        return self.nome