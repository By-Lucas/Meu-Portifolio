# Generated by Django 4.0.2 on 2022-04-06 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_alter_meuspedidos_nr_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meuspedidos',
            name='nr_pedido',
            field=models.UUIDField(auto_created=True, default='ca10884fe8fd46b689fce84f150869cb', editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
