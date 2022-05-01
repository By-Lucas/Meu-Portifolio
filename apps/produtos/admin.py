from django.contrib import admin
from .models import Produto, Imagem, Imagem_pix
from .modelos.pedidos import MeusPedidos

class ProdutoAdmin(admin.ModelAdmin):
    readonly_fields = ('usuario_produto', )
    list_display = ('produto_nome', 'produto_valor', 'valor_total_vendidos', 'produto_status', 'data_criacao')
    list_editable = ('produto_valor',)
    list_filter = ( 'produto_nome', 'data_criacao')

    def save_model(self, request, obj, form, change):
        usuario_ = request.user
        obj.usuario_produto = usuario_
        super(ProdutoAdmin, self).save_model(request, obj, form, change)
    
    # MOSTRAR APENAS CRIACOES DO USUARIO LOGADO
    #def get_queryset(self, request):
    #   qs = super(ProdutoAdmin, self).get_queryset(request)
    #    qs = qs.filter(usuario_produto=request.user)
    #    return qs
admin.site.register(Produto, ProdutoAdmin)

@admin.register(MeusPedidos)
class Pedidos_Admin(admin.ModelAdmin):
    list_display = ('nome_usuario', 'nr_pedido', 'valor_total', 'status_pedido', 'data_Pedido')
    list_filter = ( 'nome_usuario', 'data_Pedido')

admin.site.register(Imagem)
admin.site.register(Imagem_pix)