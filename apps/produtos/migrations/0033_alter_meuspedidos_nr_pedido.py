# Generated by Django 4.0.4 on 2022-04-27 01:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0032_meuspedidos_comprovante_pagamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meuspedidos',
            name='nr_pedido',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
