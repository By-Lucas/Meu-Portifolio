from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from api_pix.models import Charge
from ..models import Produto

import uuid 
import random

class MeusPedidos(models.Model):

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