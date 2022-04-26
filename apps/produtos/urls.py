from django.urls import path, include
from . import views
#from apps.produtos.views_.pedidos_view import Meus_pedidos

urlpatterns =[
    path('produtos/', views.produtos_view, name='produtos'),
    path('produto/<int:id>/', views.produto, name='produto_id'),
    path('produtosAdmin/', views.todos_produtos, name='todos_produtos_adm'),
    path('deletarProduto/<int:id>/', views.deletar_produto, name='deletar_produto'),
    path('editarProduto/<int:id>/', views.editar_produto, name='editar_produto'),
    path('cadastrar-produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtoCarrinho/<int:produto_id>', views.Meus_pedidos, name='meu_produto'), #<int:id>
    path('produtoCcomprar/<int:produto_id>', views.enviar_pedido, name='meu_pedido'), #<int:id>
]