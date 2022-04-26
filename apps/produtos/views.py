from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone


# Create your views here.
from .modelos.pedidos import MeusPedidos
from .models import Produto
from .forms import ProdutoForm

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

@login_required
def cadastrar_produto(request):
    form = ProdutoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso!')
            return redirect(request, 'admin')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar produto!')
            return redirect(request, 'admin')
    context = {
        'form':form
    }
    return render(request, 'produtos/cadastrar_produto.html', context)

@login_required
def todos_produtos(request):
    produtos_ = Produto.objects.all().order_by("id",)

    #O código abaixo serve para a aba de pesquisar usar a variavel 'q', e buscar cliente pelo nome, cpf e email
    queryset = request.GET.get('q')
    if queryset:
        produtos_ = Produto.objects.filter(
            Q(produto_nome__icontains=queryset)|
            Q(produto_caregoria__icontains=queryset)|
            #Q(telefone__icontains=queryset)|
            Q(produto_valor__icontains=queryset)|
            Q(produto_status__icontains=queryset)
        )

    #Aqui é o código da quantidade de clientes que queremos por página
    paginator = Paginator(produtos_, 7) # Aqui pode alterar o tanto de produtos que desejar
    page = request.GET.get('page')
    produtos_todos = paginator.get_page(page)

    context = {
        'produtos_todos':produtos_todos,
        'produtos_':produtos_
    }

    return render(request,"produtos/todos_produtos.html", context)


@login_required
def editar_produto(request, id=None):
    projeto_ = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=projeto_)
    if request.method == 'POST':
        if  form.is_valid():
            obj = form.save()
            obj.save()
            messages.add_message(request, constants.SUCCESS, "Produto editado com sucesso")
            return redirect('todos_produtos_adm')
        else:
            messages.add_message(request, constants.ERROR, "Erro ao editar Produto")
            return redirect('todos_produtos_adm')
    return render(request, 'produtos/editar_produto.html', {'form':form})

@login_required
def deletar_produto(request, id=None):
    produto_remover = get_object_or_404(Produto, id=id)
    if request.method == "POST": 
        produto_remover.delete()
        messages.add_message(request, constants.SUCCESS, "Produto removido com sucesso") #cliente removido
        return redirect('todos_produtos_adm')
    return render(request, 'produtos/deletar_produto.html',{'produto_remover':produto_remover})
