# Generated by Django 4.0.4 on 2022-04-26 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario_perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=20, null=True)),
                ('sobrenome', models.CharField(blank=True, max_length=50, null=True)),
                ('foto_usuario', models.FileField(blank=True, null=True, upload_to='media/image_perfil/<django.db.models.fields.CharField>')),
                ('chave_pix', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('telefone', models.CharField(max_length=50, null=True)),
                ('comprovante', models.FileField(blank=True, null=True, upload_to='media/comprovantes')),
                ('data_cadastrado', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
