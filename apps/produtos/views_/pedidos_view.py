from django.http import HttpRequest
from apps.produtos.modelos.pedidos import MeusPedidos
from produtos.models import Produto
from functions import get_meuspedidos, getNrPedidos
from django.shortcuts import render, redirect, get_object_or_404
# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

def Meus_pedidos(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == "POST":
        meus_numeros = []
        quantidade_comprado = 0
        for produtos in produto:
            quantidade_comprado +=1

            valor_total = int(quantidade_comprado) * int(produto.produto_valor)
            criar_pedido = MeusPedidos.objects.create(
                                                    quantidade=quantidade_comprado,
                                                    preco_unitario=produto.produto_valor,
                                                    valor_total=valor_total,)
            criar_pedido.save()

        messages.success(request, f"Número(s) adcionado(s) '{meus_numeros}' com sucesso!")
        
        return HttpRequest('Feito com sucesso')
    context = {
        'produto': produto,
    }
    return render(request, "pagamentos/pagamento_produto.html", context)