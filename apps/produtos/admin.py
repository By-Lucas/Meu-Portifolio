from django.contrib import admin
from .models import Produto, Imagem, Imagem_pix
from .modelos.pedidos import MeusPedidos

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto_nome', 'produto_valor', 'valor_total_vendidos', 'produto_status', 'data_criacao')
    list_editable = ('produto_valor',)
    list_filter = ( 'produto_nome', 'data_criacao')
    
@admin.register(MeusPedidos)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_usuario', 'nr_pedido', 'valor_total', 'status_pedido', 'data_Pedido')
    #list_editable = ('produto_valor',)
    list_filter = ( 'nome_usuario', 'data_Pedido')

admin.site.register(Imagem)
admin.site.register(Imagem_pix)