from django.contrib import messages, auth
from django.shortcuts import redirect, render
from plataforma.models import MeusPedidos

def index(request, template_name = 'finaizar_pedido.html'):
    if request.user.is_authenticated:
        itens = MeusPedidos.objects.filter(usuario=request.user).last()
        total = int(itens.valor_total)
        print(type(total))
        todos_pedidos = MeusPedidos.objects.all()
        context = {
        'todos_pedidos': todos_pedidos,
        'itens':itens,
        'total': total
        }
        return render(request, template_name,context)
    else:
        messages.warning(request,'Para acessar a pagina faça o login')
        return redirect('/')
    
