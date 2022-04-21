from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

from .forms import ProjetoForm
from site_portifolio.models_2.projetos import projeto

def index(request):
    return render(request, 'index.html')

def recursos(request):
    return render(request, 'recursos.html')

def beneficios(request):
    return render(request, 'beneficios.html')

def precos(request):
    return render(request, 'precos.html')

@login_required
def Cadastrar_projeto(request):
    form = ProjetoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, constants.SUCCESS, 'Projeto cadastrado com sucesso!')
        else:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar projeto!')
        return redirect(request, 'admin')
    context = {
            'form':form,
        }
    return render(request, 'cadastrar_projeto.html', context)

def todos_projetos(request):
    projetos_all = projeto.objects.all()

    context = {
        'projetos': projetos_all,
    }
    return render(request, 'todos_projetos.html', context)


@login_required
def editar_projeto(request, id=None):
    projeto_ = get_object_or_404(projeto, id=id)
    form = ProjetoForm(request.POST or None, instance=projeto_)
    if request.method == 'POST':
        if  form.is_valid():
            obj = form.save()
            obj.save()
            messages.add_message(request, constants.SUCCESS, "Projeto editado com sucesso")
            return redirect('admin')
        else:
            messages.add_message(request, constants.ERROR, "Erro ao editar projeto")
            return redirect('admin')

    return render(request, 'editar_projeto.html', {'form':form})