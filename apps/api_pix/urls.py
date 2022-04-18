from django.urls import path

from .views import ChargeList, ChargeDetail, Notification, WebhookList, WebhookDetail


app_name = 'api-pix'

#/api-pix/v1/webhooks/

urlpatterns = [
    path('charges/', ChargeList.as_view(), name='charges'),
    path('charges/<str:txid>/status/', ChargeDetail.as_view(), name='status'),
    path('notification/', Notification.as_view(), name='notification'),
    # Remover após criar o webhook no servidor
    #path('webhooks/', WebhookList.as_view()), # Para criar e listar
    #path('webhooks/<str:webhook>/', WebhookDetail.as_view()), # Para deletar
    #
]