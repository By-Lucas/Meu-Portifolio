from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('beneficios/', views.beneficios),
    path('projetos/', views.projetos, name='projetos'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.use_login, name='login')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Para carregar STATIC e as MIDIAS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)