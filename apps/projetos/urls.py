from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('recursos/', views.recursos),
    path('beneficios/', views.beneficios),
    path('precos/', views.precos),
]