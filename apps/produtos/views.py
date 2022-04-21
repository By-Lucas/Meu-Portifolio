from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone


# Create your views here.
from .models import Produto, MeusPedidos
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
def lista_de_clientes(request):
    clientes_todos = Clientes.objects.all().order_by(
        "-id",
    )
    
    # Da forma acima, mostra todos os cadastros ordenado pelo ultimo adicionado
    # poderia colocar por data de cadastro

    #O código abaixo serve para a aba de pesquisar usar a variavel 'q', e buscar cliente pelo nome, cpf e email
    queryset = request.GET.get('q')
    if queryset:
        clientes_todos = Clientes.objects.filter(
            Q(nome__icontains=queryset)|
            Q(email__icontains=queryset)|
            #Q(telefone__icontains=queryset)|
            Q(cpf__icontains=queryset)|
            Q(STATUS__icontains=queryset)
        )

    #Aqui é o código da quantidade de clientes que queremos por página
    paginator = Paginator(clientes_todos, 7) # Aqui pode alterar o tanto de clientes que desejar
    page = request.GET.get('page')
    clientes_todos = paginator.get_page(page)

    return render(request,"clientes/lista_de_clientes.html",{'clientes_todos':clientes_todos})

def lista_de_clientes(request):
    clientes_todos = Clientes.objects.all().order_by(
        "-id",
    )
    
    # Da forma acima, mostra todos os cadastros ordenado pelo ultimo adicionado
    # poderia colocar por data de cadastro

    #O código abaixo serve para a aba de pesquisar usar a variavel 'q', e buscar cliente pelo nome, cpf e email
    queryset = request.GET.get('q')
    if queryset:
        clientes_todos = Clientes.objects.filter(
            Q(nome__icontains=queryset)|
            Q(email__icontains=queryset)|
            #Q(telefone__icontains=queryset)|
            Q(cpf__icontains=queryset)|
            Q(STATUS__icontains=queryset)
        )

    #Aqui é o código da quantidade de clientes que queremos por página
    paginator = Paginator(clientes_todos, 7) # Aqui pode alterar o tanto de clientes que desejar
    page = request.GET.get('page')
    clientes_todos = paginator.get_page(page)

    return render(request,"clientes/lista_de_clientes.html",{'clientes_todos':clientes_todos})

@login_required
def editar_cliente(request, id=None):
    cliente = get_object_or_404(Clientes, id=id)

    form = ClienteForm(request.POST or None, instance=cliente)

    if  form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request, "Cliente editado com sucesso") #cliente informacao
        return redirect('index')

@login_required
def editar_produto(request, id=None):
    cliente = get_object_or_404(Clientes, id=id)

    form = ClienteForm(request.POST or None, instance=cliente)

    if  form.is_valid():
        obj = form.save()
        obj.save()
        messages.info(request, "Cliente editado com sucesso") #cliente informacao
        return redirect('index')

