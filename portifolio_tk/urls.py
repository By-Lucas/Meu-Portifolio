from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('site_portifolio.urls')),
    path('', include('produtos.urls')),
    path('', include('projetos.urls')),
    path('user/', include('users.urls')),
    path('api-pix/v1/', include('api_pix.urls')),
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
]
