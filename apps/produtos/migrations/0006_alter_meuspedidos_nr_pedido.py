# Generated by Django 4.0.2 on 2022-04-06 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_produto_produto_img_alter_meuspedidos_nr_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meuspedidos',
            name='nr_pedido',
            field=models.UUIDField(auto_created=True, default='fd2f320216414ce98b7de4327d82e6d8', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
