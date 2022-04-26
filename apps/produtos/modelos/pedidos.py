from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from api_pix.models import Charge
from ..models import Produto
from users.models import Usuario_perfil
import uuid 


class MeusPedidos(models.Model):
    usuario = models.ForeignKey(Usuario_perfil, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Charge, on_delete=models.CASCADE, null=True)
    nome_usuario = models.CharField(max_length=25, null=True)
    nr_pedido = models.UUIDField( primary_key = True, default = uuid.uuid4().hex, editable = False, auto_created=True, unique=True)
    #nr_pedido = models.UUIDField( primary_key = True, default = shortuuid.ShortUUID().random(length=5), editable = False, auto_created=True, unique=True) 
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1, null=True, blank=True)
    preco_unitario = models.IntegerField()
    valor_total = models.IntegerField()
    status_pedido = models.BooleanField(default=False)
    data_Pedido = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_meusPedidos_by_usuario(usuario_id):
        return MeusPedidos.objects.filter(usuario=usuario_id).order_by('-data_Pedido')


    class Meta:
        verbose_name = 'Meu pedido'
        verbose_name_plural = 'Meus pedidos'

    def __str__(self) -> str:
        return f'Usuario: {self.usuario} | Data: {self.data_Pedido}'