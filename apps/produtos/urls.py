from django.urls import path, include
from . import views

urlpatterns =[
    path('produtos/', views.produtos_view, name='produtos'),
    path('produto/<int:id>/', views.produto, name='produto_id')
]