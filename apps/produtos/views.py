from multiprocessing import context
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.
from .models import Produto, MeusPedidos

def produtos_view(request):
    produtos = Produto.objects.all().order_by('data_criacao')
    
    context = {
        'produtos':produtos,
    }
    return render(request, 'produtos/produtos.html', context)

def produto(request, id):
    produto_ = get_object_or_404(Produto, id=id)
    # Abaixo mostra 3 produtos ( talvez voce se intereça por esses produto) imoveis com status ativo
    # Pode ser alterado para categoria ou coloca um inteligencia artificial
    sugestoes = Produto.objects.filter(produto_status=produto_.produto_status).exclude(id=id)[:3]
    context={
        'produto':produto_,
        'sugestoes':sugestoes
    }
    return render(request,'produtos/produto_id.html', context)