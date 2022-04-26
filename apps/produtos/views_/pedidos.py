from modelos.pedidos import MeusPedidos
from models import Produto
from functions import get_meuspedidos, getNrPedidos
from django.shortcuts import render, redirect, get_object_or_404
# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

def Meus_Sorteios(request, produto_id):
    user_id = request.user.id
    user_username = request.user.username
    produto = Produto.objects.get(id=produto_id)
    nr_pedido = getNrPedidos(request, user_id)
    nr_pedido = nr_pedido[0]['nr_pedido']
    if nr_pedido:
        nr_pedido = nr_pedido + 1
    else:
        nr_pedido = 1
    if request.method == "POST":
        dict_post = dict(request.POST)
        quantidade_2 = dict_post['numero_sorteio']
        characters = "\[]'!?"
        meus_numeros = []
        quantidade_comprado = 0
        for i in quantidade_2:
            meus_numeros.append(i)
            meus_numeros_int = ', '.join( x for x in meus_numeros if x not in characters)
            quantidade_comprado +=1

        print("NUMEROS SELECIONADOS: ",meus_numeros_int.split(','), dir(meus_numeros_int))
        valor_total = int(quantidade_comprado) * float(produto.sorteio_valor)
        criar_pedido = MeusPedidos.objects.create(nr_pedido=nr_pedido, 
                                                produto_id=produto.id, 
                                                quantidade=quantidade_comprado,
                                                preco_unitario=produto.sorteio_valor,
                                                valor_total=valor_total,
                                                numeros_comprados = meus_numeros_int,
                                                usuario_id=user_id,
                                                nome_usuario=user_username)

        messages.success(request, f"Número(s) adcionado(s) '{meus_numeros}' com sucesso!")
        
        return redirect('/pagamento')
    context = {
        'sorteio_': sorteio_,
    }
    return render(request, "meus_sorteios.html", context)