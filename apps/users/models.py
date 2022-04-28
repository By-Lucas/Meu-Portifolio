from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Usuario_perfil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=20, null=True, blank=True)
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    foto_usuario = models.FileField(upload_to=f'media/image_perfil/{nome}', null=True, blank=True)
    chave_pix = models.CharField(max_length=100, null=True, blank=True, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=False, unique=False)
    cep = models.CharField(max_length=50, null=True, blank=False, unique=False)
    cpf = models.CharField(max_length=11, null=True, blank=False, unique=False)
    email = models.CharField(max_length=50, null=True, blank=False, unique=False)
    comprovante = models.FileField(upload_to='media/comprovantes',null=True, blank=True)
    data_cadastrado = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nome

    def register(self):
        self.save()

# Criar o perfil quado o usuario for criado
def create_profile(sender, instance, created, **kwargs):
    if created:
        Usuario_perfil.objects.create(user=instance)
post_save.connect(create_profile, sender=User)

