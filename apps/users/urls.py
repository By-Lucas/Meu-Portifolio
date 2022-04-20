from django.urls import path, include
from . import views
from .views_2 import cadastros, index_admin

urlpatterns =[
    path('administracao/', views.administracao, name='admin'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('novo-usuario/', cadastros.novo_usuario, name='novo_usuario'),
    path('home-admin/', index_admin.home_admin, name='home_admin'),
    #path('produto/<int:id>/', views.produto, name='produto_id')
]