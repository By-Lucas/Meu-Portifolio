from django import forms
from .models import Produto
from .modelos.pedidos import MeusPedidos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields  = [
            'usuario_produto',
            'produto_nome',
            'produto_caregoria',
            'produto_descricao',
            'produto_img',
            'produto_imagens',
            'pagamento_tempo',
            'produto_pix',
            'produto_valor',
            'produto_dia_suporte',
            'produto_horario_suporte',
            'produto_status',
            'produto_numeros',
            'produto_vendidos',
            'produto_disponiveis',
            'produto_reservados',
            'valor_total_vendidos',
            #'data_criacao',
        ]
