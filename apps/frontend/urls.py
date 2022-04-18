from django.urls import path

from .views import index

urlpatterns = [
    path('pagamento/', index, name='pagamento'),
]