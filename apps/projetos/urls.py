from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-projetos/', views.Cadastrar_projeto, name='cadastrar_projeto'),
    path('projetos-all', views.todos_projetos, name='todos_projetos'),
    path('editarprojeto/<int:id>/', views.editar_projeto, name='editar_projeto')
]