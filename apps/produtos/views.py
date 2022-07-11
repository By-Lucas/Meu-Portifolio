from django.http import HttpResponse
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
from users.models import Usuario_perfil
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
            return redirect('admin')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar produto!')
            return redirect('admin')
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

def Meus_pedidos(request, produto_id):
    if request.user.is_authenticated:
        perfis = Usuario_perfil.objects.filter(nome=request.user.first_name)
        user_username = request.user.username
        user_id = request.user.id
        produto = Produto.objects.get(id=produto_id)
        #print(dir(produto), print(produto.get_produto_by_id))
        for perfil in perfis:
            print(perfil.email)

        if perfis.exists():
            context = {
                'perfil':perfil,
                'produto': produto,
            }
        else:
            context = {'produto': produto,}
        return render(request, "pagamentos/pagamento_produto.html", context)
    else:
        messages.add_message(request, constants.ERROR, "Faça o login para prossegir com a compra")
        return redirect("login")

def pedidos_historico(request):
    if request.user.is_authenticated:
        m_pedidos = MeusPedidos.objects.filter(usuario=request.user.id).all()
        todos_pedidos = MeusPedidos.objects.all()
        context = {
            'todos_pedidos': todos_pedidos,
            'm_pedidos':m_pedidos
        }
        return render(request, "produtos/meus_produtos.html", context)
    else:
        messages.warning(request,'Faça o login para visualizar os conteudos')
        return redirect('/')

def enviar_pedido(request, produto_id):
    if request.user.is_authenticated:
        user_username = request.user.username
        user_id = request.user.id
        produto = Produto.objects.get(id=produto_id)
        #print(dir(produto), print(produto.get_produto_by_id))
        if request.method == "POST":
            valor_get = request.POST.get('produto')
            uploadedFile = request.FILES["comprovante_"]
            quantidade_comprado = 0
            quantidade_comprado +=1
            valor_total = int(quantidade_comprado * valor_get)

            telefone = request.POST.get('numero')
            cpf = request.POST.get('cpf')
            cep = request.POST.get('cep')
            email = request.POST.get('email')

            cpf_ = Usuario_perfil.objects.filter(cpf=cpf).all()
            email_ = Usuario_perfil.objects.filter(email=email).all()
            if cpf_.exists() or email_.exists():
                criar_pedido = MeusPedidos.objects.create(
                            quantidade=quantidade_comprado,
                            preco_unitario=produto.produto_valor,
                            valor_total=valor_total,
                            produto=produto,
                            usuario=user_id,
                            nome_usuario=user_username,
                            comprovante_pagamento=uploadedFile)
                criar_pedido.save()
                messages.add_message(request, constants.SUCCESS, f'Pedido adcionado {produto.produto_nome}' )
                return redirect('pedidos_historico')
            else:
                criar_pedido = MeusPedidos.objects.create(
                            quantidade=quantidade_comprado,
                            preco_unitario=produto.produto_valor,
                            valor_total=valor_total,
                            produto=produto,
                            usuario=user_id,
                            nome_usuario=user_username,
                            comprovante_pagamento=uploadedFile)
                criar_pedido.save()
                criar_perfil = Usuario_perfil.objects.create(
                                nome=request.user.first_name,
                                sobrenome=request.user.last_name,
                                telefone=telefone,
                                cep=cep,
                                cpf=cpf,
                                email=email)
                criar_perfil.save()
                messages.success(request, f"pedido enviado com sucesso")

                return redirect('pedidos_historico')
    context = {
        'produto': produto,
    }
    return render(request, "produtos/meus_produtos.html", context)