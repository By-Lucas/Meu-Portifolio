# PORTIFOLIO + FREELANCERS
## Informações
*- Portifílio mostrando minha habilidades, projetos e serviços.*

*-No portifílio adcionei tambem pagina de administração para criar, editar, deletar e acompanhar ganhos feito nas vendas dos projetos freelancers.*

*- Está sendo implementado o método de pagamento via pix automátizado, que foi criada e consumida a api do banco Ebanx para fornecer o QRcode e Chave aleatória com valor do produto selecionado.*

## TECNOLOGIAS UTILIZADAS
- Python
- Django
- Mysql
- ApiRest
- JavaScript
- Ajax
- Bootstrap
- css
- Html


## Gia para rodar o portifílo

*Instalar Virtualenv*
~~~ virtualenv
pip install virtualenv
~~~
*Criar Virtualenv*
~~~ virtualenv
python -m venv venv
~~~
*Ativar Virtualenv*
~~~ virtualenv
venv/scripts/activate
~~~

## Instalar bibliotecas e rodar a aplicação
*Instalar bibliotecas*
~~~ instalar_lib
pip install -r requirements.txt
~~~
*Rodar a aplicação*
~~~ rodar_app
python manage.py runserver
~~~

*Agora é só ir no navegador e colocar o seguinte endereço: http://127.0.0.1:8000/*

## Informações importantes

*Para ter acesso a pagina de administrador, bastar criar um super usuário com comando abaixo e seguir o passo a passo, ou pode logar com usuário padroão criado por mim (Usuário: lucasdev e a senha é: 123)*
~~~ superuser
python manage.py createsuperuser
~~~
