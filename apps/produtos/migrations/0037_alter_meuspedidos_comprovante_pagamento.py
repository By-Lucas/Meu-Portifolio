# Generated by Django 4.0.4 on 2022-04-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0036_alter_meuspedidos_comprovante_pagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meuspedidos',
            name='comprovante_pagamento',
            field=models.FileField(blank=True, null=True, upload_to='comprovante/%Y/%m/%d'),
        ),
    ]
