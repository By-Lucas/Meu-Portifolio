# Generated by Django 4.0.4 on 2022-04-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0014_alter_meuspedidos_nr_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meuspedidos',
            name='nr_pedido',
            field=models.UUIDField(auto_created=True, default='d8f6dc11ac2548b6a687f1b85d92ec8c', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
