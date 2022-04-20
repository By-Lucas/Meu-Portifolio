from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('site_portifolio.urls')),
    path('', include('produtos.urls')),
    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),
]
