from django.db import models
from django.conf import settings

class Charge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    txid = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=8, decimal_places=2)# Valor máximo de R$ 999 999,99
    status = models.CharField(default='AGUARDANDO', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self) -> str:
        return f'{self.user} {self.status}'