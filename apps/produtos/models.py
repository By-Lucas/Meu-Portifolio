from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from api_pix.models import Charge
from multiselectfield import MultiSelectField

import uuid 
import random


class Imagem(models.Model):
    img = models.FileField(upload_to='img')
    def __str__(self) -> str:
        return self.img.url        
#------------------------------------------------
class Imagem_pix(models.Model):
    img_pix = models.ImageField(upload_to='img/pix')
    def __str__(self) -> str:
        return self.img_pix.url

class Produto(models.Model):
    CHOICES = (('S', 'Segunda'),
                ('T', 'Terça'),
                ('Q', 'Quarta'),
                ('QI', 'Quinta'),
                ('SE', 'Sexta'),
                ('SA', 'Sabado'),
                ('D', 'Domingo'))

    CATEGORIAS = (('imovel', 'Imoveis'),
                ('eletronicos', 'Eletrônicos'),
                ('veiculos', 'Veículos'),
                ('financeiro', 'Financeiro'),
                ('roupas', 'Roupas'),
                ('celulares', 'Celulares'),
                ('moveis', 'Moveis'),
                ('eletro_domesticos', 'Eletro Doméstico'),
                ('dinheiro', 'Dinheiro'),
                ('outros', 'Outros'))

    choices_status = (('D', 'Disponivel'),
                    ('A', 'Atualizando'),
                    ('C', 'Preenchido'))
    
    pagamento_tempo = (
        ('M', 'Mensal'),
        ('T', 'Trimestral'),
        ('A', 'Anual'),
        ('V', 'Vitalicio')
    )

    usuario_produto = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=100, blank=False, null=False)
    produto_caregoria = MultiSelectField(choices=CATEGORIAS, max_length=30, null=True, blank=True)
    produto_descricao = models.TextField(max_length=500, null=False, blank=False)
    produto_img = models.ImageField(upload_to='img', null=True, blank=True)
    produto_imagens = models.ManyToManyField(Imagem)
    pagamento_tempo = models.CharField(choices=pagamento_tempo, max_length=30, null=True, blank=True)
    produto_pix = models.ImageField(upload_to='img/pix', null=True, blank=True)
    produto_pix_codigo = models.CharField(max_length=150, null=True, blank=True)
    produto_valor = models.IntegerField()
    #produto_valor_tri = models.IntegerField()
    #produto_valor_vitalicio = models.IntegerField()
    produto_dia_suporte = models.CharField(max_length=100, null=True, blank=True)
    produto_horario_suporte = models.TimeField(null=True, blank=True)
    produto_status = models.CharField(max_length=15, choices=choices_status, default="D")
    produto_numeros = models.IntegerField(default=0, help_text='Quantidade disponivels')
    produto_vendidos = models.IntegerField(default=0, null=True, blank=True)
    produto_favorito = models.BooleanField(default=False)
    produto_disponiveis = models.IntegerField(default=0,null=True, blank=True)
    produto_reservados = models.IntegerField(default=0, null=True, blank=True)
    valor_total_vendidos = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text='Valor total vendidos')
    data_criacao = models.DateField(auto_now=True, max_length=50, blank=False, null=False)

    @staticmethod
    def get_produto_by_id(ids):
        return Produto.objects.filter(id__in =ids)
    
    @staticmethod
    def get_all_produto():
        return Produto.objects.all()
    
    @staticmethod
    def get_all_produto_by_categoryid(category_id):
        if category_id:
            return Produto.objects.filter(category = category_id)
        else:
            return Produto.get_all_produto();

    def __str__(self) -> str:
        return self.produto_nome
