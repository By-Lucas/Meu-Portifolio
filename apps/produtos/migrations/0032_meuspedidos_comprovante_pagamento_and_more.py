# Generated by Django 4.0.4 on 2022-04-27 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0031_alter_meuspedidos_nr_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='meuspedidos',
            name='comprovante_pagamento',
            field=models.FileField(blank=True, null=True, upload_to='comprovante/<django.db.models.fields.CharField>'),
        ),
        migrations.AlterField(
            model_name='meuspedidos',
            name='nr_pedido',
            field=models.UUIDField(auto_created=True, default='c3d2cd4faf964f06b0de90646cf297f0', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
