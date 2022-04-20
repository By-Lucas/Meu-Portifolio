from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants


def novo_usuario(request):
    if request.method == 'GET':
        # Se o ususario já estiver logado, será direcionado para pagina principal
    #    if request.user.is_authenticated:
    #        messages.add_message(request, constants.ERROR, 'Não pode fazer cadastro se estiver logado')
    #        return redirect('/')
        return render(request, 'novo_usuario.html')
    if request.method == 'POST':
        #capiturar informacoes do form 'name' no html
        username_1 = request.POST.get('username')
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Se o tamanho do nome, email e senha for igual a 0, redireciona para a pagina
        # o strip() remove todos os espaços em brancos do form
        if len(username_1.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('novo_usuario')
        # Verifica se está tentando cadastrar um usuario já existente
        user = User.objects.filter(username=username_1)
        email = User.objects.filter(email=email)
        print(user) # Exibe o nome no print se ja tiver usuario cadastrado com mesmo username
        if user.exists() or email.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário ou email igual cadastrado')
            return redirect('novo_usuario')
        try:
            user = User.objects.create_user(username=username_1,
                                            first_name=nome,
                                            last_name=sobrenome,
                                            email=email, 
                                            password=senha)
            user.save()

            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('novo_usuario')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('novo_usuario')
