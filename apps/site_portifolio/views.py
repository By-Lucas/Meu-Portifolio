from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

from .models import linguagems_progr, linguagens_mais_usadas
from .models_2.projetos import projeto

def index(request):
    tecnologias = linguagems_progr.objects.all()
    tecnologias_usadas = linguagens_mais_usadas.objects.all()

    context = {
        'tecnologias':tecnologias,
        'tecnologias_usadas':tecnologias_usadas
    }
    return render(request, 'index.html', context)


def sobre(request):
    return render(request, 'sobre.html')


def beneficios(request):
    return render(request, 'beneficios.html')

def projetos(request):
    projetos_all =  projeto.objects.all()

    context = {
    'projetos':projetos_all,
    }
    return render(request, 'projetos.html', context)

def use_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.add_message(request, constants.SUCCESS ,'Login efetuado com sucesso!!')
                    return redirect('/')
                if not uname and upass or  uname == '' and upass == '':
                    messages.add_message(request, constants.ERROR, 'Usuário ou senha incorreto ou campos vazio!')
        else:
            fm = AuthenticationForm()
        return render(request,'login.html',{'form':fm})
    else:
        messages.add_message(request, constants.ERROR ,'Não pode fazer o login se o usuaário já estiver logado')
        return redirect('/')

def user_logout(request):
    logout(request)
    return redirect('/')
