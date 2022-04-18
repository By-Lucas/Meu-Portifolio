from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from api_pix.models import Charge

import uuid 
import random


class Imagem(models.Model):
    img = models.FileField(upload_to='img')
    def __str__(self) -> str:
        return self.img.url        
#------------------------------------------------
class Imagem_pix(models.Model):
    img_pix = models.ImageField(upload_to='img')
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

    usuario_produto = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=100, blank=False, null=False)
    produto_caregoria = models.CharField(choices=CATEGORIAS, max_length=30, null=True, blank=True)
    produto_descricao = models.TextField(max_length=500, null=False, blank=False)
    produto_img = models.ImageField(upload_to='img', null=True, blank=True)
    produto_imagens = models.ManyToManyField(Imagem)
    produto_pix = models.ImageField(upload_to='img', null=True, blank=True)
    produto_valor = models.DecimalField(max_digits=8, decimal_places=2)
    produto_dia_suporte = models.CharField(max_length=100, null=True, blank=True)
    produto_horario_suporte = models.TimeField(null=True, blank=True)
    produto_status = models.CharField(max_length=15, choices=choices_status, default="D")
    produto_numeros = models.IntegerField(default=0, help_text='Quantidade disponivels')
    produto_vendidos = models.IntegerField(default=0, null=True, blank=True)
    produto_disponiveis = models.IntegerField(default=0,null=True, blank=True)
    produto_reservados = models.IntegerField(default=0, null=True, blank=True)
    valor_total_vendidos = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, help_text='Valor total vendidos')
    data_criacao = models.DateField(auto_now=True, max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.produto_nome

class MeusPedidos(models.Model):
    def codigo_pedido (length=6):
        size = 6
        chars = ''.join(random.sample(chars, size))
        return chars

    STATUS_PEDIDO = (('PG',u'Pago'),
                    ('PD',u'Pendente'),
                    ('CL',u'Cancelado'))

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    pagamento = models.ForeignKey(Charge, on_delete=models.CASCADE, null=True)
    nome_usuario = models.CharField(max_length=25, null=True)
    nr_pedido = models.UUIDField( primary_key = True, default = uuid.uuid4().hex, editable = False, auto_created=True, unique=True)
    #nr_pedido = models.UUIDField( primary_key = True, default = shortuuid.ShortUUID().random(length=5), editable = False, auto_created=True, unique=True) 
    produto_id = models.ManyToManyField(Produto)
    quantidade = models.IntegerField(null=True, blank=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    numeros_comprados = models.CharField(max_length=10000, blank=True, null=True)
    status_pedido = models.CharField(choices=STATUS_PEDIDO, max_length=20, blank=True, null=True)
    data_Pedido = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Meu pedido'
        verbose_name_plural = 'Meus pedidos'

    def __str__(self) -> str:
        return f'Usuario: {self.usuario} | Data: {self.data_Pedido}'